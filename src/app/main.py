from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/healthcheck")
async def healthscheck():
    return {"message": "Pokedex Up"}
