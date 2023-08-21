from fastapi import FastAPI

from routers import supplies_router

app = FastAPI()

app.include_router(supplies_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}