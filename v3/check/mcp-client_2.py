from fastmcp import Client
import httpx
import asyncio


transport = httpx.AsyncHTTPTransport(verify=False)
http_client = httpx.AsyncClient(transport=transport)

client = Client("https://34.13.120.204/mcp", auth="token-from-idp")


async def main():
    async with client:
        result = await client.call_tool(
            "list_products_products_get",
            {"category": "Electronics", "max_price": 100}
        )
        print(f"Affordable electronics: {result.data}")

        result = await client.call_tool("get_product", {"product_id": 2})
        print(result)


asyncio.run(main())
