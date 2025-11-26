FROM python:3.11

RUN mkdir -p /tmp/app

WORKDIR /tmp/app

USER root

COPY src/ /tmp/app/
COPY requirements.txt /tmp/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "fastmcp run mcp_server.py:mcp --transport http --host 0.0.0.0 --port 8000 2>&1"]
