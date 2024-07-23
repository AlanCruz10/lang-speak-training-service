import fastapi

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return fastapi.responses.JSONResponse(content={"message": "Hello, world 2!"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)
