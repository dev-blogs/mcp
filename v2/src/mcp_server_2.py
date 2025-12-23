from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastmcp import FastMCP
from fastapi import Depends, Header


app = FastAPI(title="E-commerce API", version="1.0.0")


@app.get("/products/{product_id}", operation_id="get_product", response_model=str)
def get_product(product_id: int):
    """Get a specific product by ID."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]


@app.get("/test", operation_id="get_test")
def test(sql: str) -> str:
    """
    Run a SQL query against the database and return rows as JSON
    """
    return f"test, {sql}!"
    

@app.get("/list_users", operation_id="list_users")
def list_users() -> list[dict]:    
    return [
        {"id": 1, "name": "test1", "email": "gcp.learn00007@gmail.com"}
    ]


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
    

mcp = FastMCP.from_fastapi(app=app)


if __name__ == "__main__":
    mcp.run()
