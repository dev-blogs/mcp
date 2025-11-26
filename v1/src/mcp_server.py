import sqlite3
from fastmcp import FastMCP

mcp = FastMCP("UserDBServer")


def init_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    users = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
    ]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
    conn.commit()
    return conn


db = init_db()


@mcp.tool()
def test(sql: str) -> str:
    """
    Run a SQL query against the database and return rows as JSON
    """
    return f"test, {sql}!"
    

@mcp.tool()
def list_users() -> list[dict]:
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]


@mcp.resource("db://schema")
def schema() -> str:
    """
    Return the database schema.
    """
    cur.execute("SELECT id FROM users WHERE name='test1'")
    return "\n".join(row[0] for row in cur.fetchall())


if __name__ == "__main__":
    mcp.run()
