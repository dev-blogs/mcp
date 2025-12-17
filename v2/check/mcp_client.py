from fastmcp import Client
import asyncio

client = Client("http://34.46.54.254/mcp")
#client = Client("http://localhost:8000/mcp")

async def main():
    async with client:
        result = await client.call_tool("list_users")
        print(result)


asyncio.run(main())
