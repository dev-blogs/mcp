from fastmcp import Client
import asyncio

client = Client("http://34.68.113.56:8000/mcp", auth="token-from-idp")

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
