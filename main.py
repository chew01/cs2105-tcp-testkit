import socket

import uvicorn
from fastapi import FastAPI, HTTPException

from models import Query, MethodEnum, DestEnum

app = FastAPI()
app.server_port = 8888

@app.get("/port")
async def get_port():
    return {"port": app.server_port}

@app.post("/port")
async def set_port(port: int):
    if port < 1024:
        raise HTTPException(status_code=400, detail="cannot use port below 1024")
    app.server_port = port
    return {"message": f"server port set to {app.server_port}"}


@app.get("/key")
async def get_key(path: str):
    try:
        q = Query(method=MethodEnum.get, dest=DestEnum.key, path=path)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", app.server_port))
            s.send(q.to_bytes())
            received = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return received
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/counter")
async def get_counter(path: str):
    try:
        q = Query(method=MethodEnum.get, dest=DestEnum.counter, path=path)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", app.server_port))
            s.send(q.to_bytes())
            received = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return received
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/key")
async def post_key(path: str, content: str, force_content_length: bool = False):
    try:
        q = Query(method=MethodEnum.post, dest=DestEnum.key, path=path, content=content, force_content_length=force_content_length)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", app.server_port))
            s.send(q.to_bytes())
            received = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return received
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/counter")
async def post_counter(path: str, content: str, force_content_length: bool = False):
    try:
        q = Query(method=MethodEnum.post, dest=DestEnum.counter, path=path, content=content, force_content_length=force_content_length)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", app.server_port))
            s.send(q.to_bytes())
            received = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return received
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/key")
async def delete_key(path: str):
    try:
        q = Query(method=MethodEnum.delete, dest=DestEnum.key, path=path)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", app.server_port))
            s.send(q.to_bytes())
            received = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return received
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/counter")
async def delete_counter(path: str):
    try:
        q = Query(method=MethodEnum.delete, dest=DestEnum.counter, path=path)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", app.server_port))
            s.send(q.to_bytes())
            received = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return received
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def serve():
    """Serve the web application."""
    print("check out http://127.0.0.1:8000/docs")
    uvicorn.run(app, port=8000)

if __name__ == "__main__":
    serve()