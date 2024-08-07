from pydantic import BaseModel
from fastapi import APIRouter
from dependencies.sqlite import SQLiteDependency

class Address(BaseModel):
    name: str
    address: str
    longitude: float
    latitude: float

router = APIRouter()

sqlite = SQLiteDependency()

@router.post("/address")
async def create_address(address: Address):
    new_data = {
        "values": [
            address.name,
            address.longitude,
            address.latitude,
            address.address
        ]
    }
    result = sqlite.create(new_data)

    if result:
        return {"status_code": 201, "message": "Creation Successful", "content": result}

    return {"status_code": 404, "message": "Not Found"}


@router.get("/address/{id}")
async def get_address(id: str):
    result = sqlite.read({"id": id})
    if result:
        return result
    return {"status_code": 404, "message": "Not Found"}

@router.get("/address")
async def list_address(proximity: int, longitude: float, latitude: float):
    #for proximity/distance filtering we would need a haversine formula or something similar for checking the distance. 
    #not sure if im allowed to search this as this is not part of normal documentation.

    #if allowed, the idea would be to list all the records and then filtering for the distance/proximity on the backend 
    result = sqlite.read()
    if result:
        return result
    return {"status_code": 404, "message": "Not Found"}


@router.patch("/address/{id}")
async def update_address(id: str, address: Address):
    print(f"Address: {address}")
    update_data = {
        "id": id,
        "values": [
            address.name,
            address.longitude,
            address.latitude,
            address.address
        ]
    }
    result = sqlite.update(update_data)

    if result:
        return {"status_code": 200, "message": "Update Successful", "content": result}

    return {"status_code": 404, "message": "Not Found"}


@router.delete("/address/{id}")
async def delete_address(id: str, address: Address):
    result = sqlite.delete({"id": id})
    if result:
        return {"status_code": 200, "message": "Deletion Successful", "content": result}

    return {"status_code": 404, "message": "Not Found"}