from fastmcp import FastMCP
from fastapi import Request
from google.cloud import bigquery

mcp = FastMCP("UserDBServer")

client = bigquery.Client()
TABLE = "mig-test-project-456610.test_dataset.users"


@mcp.tool()
def test(sql: str) -> str:
    """
    Run a SQL query against the database and return rows as JSON
    """
    return f"test, {sql}!"
    

@mcp.tool()
def list_users(request: Request) -> list[dict]:
    custom_header = request.headers.get("X-My-Header")
    print('custom_header')
    print(custom_header)
    query = f"SELECT id, name, email FROM `{TABLE}` LIMIT 10"
    rows = client.query(query).result()

    return [
        {"id": r.id, "name": r.name, "email": r.email}
        for r in rows
    ]


@mcp.resource("db://schema")
def schema() -> str:
    """Return the database schema."""
    cur.execute("SELECT sql FROM sqlite_master WHERE type='table'")
    return "\n".join(row[0] for row in cur.fetchall())


if __name__ == "__main__":
    mcp.run()
