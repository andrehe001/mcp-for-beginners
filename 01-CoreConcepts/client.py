from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# llm
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
# from azure.identity import DefaultAzureCredential
import json

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

GITHUB_TOKEN = "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"

def call_llm(prompt, functions):
    token = GITHUB_TOKEN
    # credential = DefaultAzureCredential()
    endpoint = "https://models.inference.ai.azure.com"
    #endpoint = "https://azureai-foundry.openai.azure.com/"  # Replace with your actual endpoint
    model_name = "gpt-4o"

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
        # credential=credential,
    )

    print("CALLING LLM")
    response = client.complete(
        messages=[
            {
            "role": "system",
            "content": "You are a calculation assistant.",
            },
            {
            "role": "user",
            "content": prompt,
            },
        ],
        model=model_name,
        tools = functions,
        # Optional parameters
        temperature=1.,
        max_tokens=1000,
        top_p=1.    
    )

    response_message = response.choices[0].message
    
    functions_to_call = []

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            print("TOOL: ", tool_call)
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            functions_to_call.append({ "name": name, "args": args })

    return functions_to_call

def convert_to_llm_tool(tool):
    tool_schema = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "type": "function",
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
            }
        }
    }
    
    return tool_schema

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available resources
            resources = await session.list_resources()
            print("LISTING RESOURCES")
            for resource in resources:
                print("Resource: ", resource)

            # List available tools
            tools = await session.list_tools()
            print("LISTING TOOLS")

            functions = []

            for tool in tools.tools:
                print("Tool: ", tool.name)
                print("Tool", tool.inputSchema["properties"])
                functions.append(convert_to_llm_tool(tool))
            
           # prompt = "Add 2 to 20"
            prompt = "Calculate the BMI for a person with a weight of 70 kg and a height of 1.75 m. What is the sum of 300 * 2 and 100 / 4? What is the result of 10 - 5? What is the result of 3 * 4? What is the result of 10 / 2? What is the result of 1 + 7?"
            # ask LLM what tools to all, if any
            functions_to_call = call_llm(prompt, functions)

            # call suggested functions
            for f in functions_to_call:
                result = await session.call_tool(f["name"], arguments=f["args"])
                print("TOOLS result: ", result.content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())