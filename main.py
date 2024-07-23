import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return fastapi.responses.JSONResponse(content={"message": "Hello, world!"})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8082)
