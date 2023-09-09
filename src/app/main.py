import requests

from fastapi import FastAPI
from typing import Dict
from fastapi import HTTPException


app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/healthcheck")
async def healthscheck():
    return {"message": "Pokedex Up"}


def pokedex_call_by_id(id: int) -> Dict:
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(
            url=url,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()  # response.json is a python dict
    except requests.exceptions.HTTPError as err:
        raise HTTPException(status_code=response.status_code, detail=f"{err}")
    except requests.exceptions.SSLError as err:
        raise HTTPException(status_code=response.status_code, detail=f"{err}")
    except requests.exceptions.Timeout as err:
        raise HTTPException(status_code=response.status_code, detail=f"{err}")
    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=response.status_code, detail=f"{err}")
    except Exception as err:
        raise HTTPException(status_code=response.status_code, detail=f"{err}")


@app.get("/pokedex/{id}")
async def pokedex_by_id(id: int) -> Dict:
    return pokedex_call_by_id(id=id)
