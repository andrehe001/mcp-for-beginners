from mcp import ClientSession, StdioServerParameters
from mcp.types import AnyUrl
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

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
            for tool in tools.tools:
                print("Tool: ", tool.name)
            # Read a resource
            print("READING RESOURCE")
            content, mime_type = await session.read_resource(AnyUrl("greeting://Andre"))

            # Call a tool
            print("CALL TOOL")
            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print(result.content)
            
            result = await session.call_tool("calculate_bmi", arguments={"weight_kg": 70, "height_m": 1.75})
            print(result.content)
            result = await session.call_tool("divide", arguments={"a": 10, "b": 2})
            print(result.content)
            result = await session.call_tool("multiply", arguments={"a": 3, "b": 4})
            print(result.content)
            result = await session.call_tool("subtract", arguments={"a": 10, "b": 5})
            print(result.content)        

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
    