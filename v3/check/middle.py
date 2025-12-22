from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI(title="Mock IAP")

# Секрет для теста
EXPECTED_TOKEN = "token-from-idp"

@app.middleware("http")
async def mock_iap_middleware(request: Request, call_next):
    auth = request.headers.get("Authorization")
    print('auth')
    print(auth)

    if not auth or auth != f"Bearer {EXPECTED_TOKEN}":
        raise HTTPException(status_code=403, detail="Forbidden by mock IAP")

    # Можно добавить заголовки, как делает реальный IAP
    request.state.iap_user = "serviceAccount:mock-sa@example.com"

    response = await call_next(request)
    return response


@app.api_route("/mcp/{path:path}", methods=["GET", "POST"])
async def proxy_mcp(path: str, request: Request):
    return {
        "message": f"Request passed through mock IAP to MCP path: {path}",
        "iap_user": request.state.iap_user
    }


@app.get("/mcp/{path:path}")
async def proxy_mcp(path: str, request: Request):
    # Здесь можно вызвать реальный MCP сервер или просто эмулировать
    return {
        "message": f"Request passed through mock IAP to MCP path: {path}",
        "iap_user": request.state.iap_user
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
