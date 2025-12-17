from fastmcp import Client
import asyncio

client = Client("http://34.44.185.206/mcp")

async def main():
    async with client:
        result = await client.call_tool("list_users", headers={"X-My-Header": "12345"})
        print(result)


asyncio.run(main())
