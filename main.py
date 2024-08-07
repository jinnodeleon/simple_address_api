from fastapi import FastAPI
import uvicorn
from endpoints import address


app = FastAPI()
app.include_router(address.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)