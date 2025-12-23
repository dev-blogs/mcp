from fastmcp import Client
import asyncio

client = Client("http://34.172.4.201:8000/mcp")
#client = Client("http://localhost:8000/mcp")

async def main():
    async with client:
        result = await client.call_tool("list_users")
        print(result)


asyncio.run(main())
