from fastapi import FastAPI, Response, Request, HTTPException

app = FastAPI()


@app.get("/ping")
def ping() :
    return Response(content="pong", status_code=200, media_type="text/plain")

