# CREATE A BASE ROUTE

# import class FastAPI
from fastapi import FastAPI

# create an object/instance of the class FastAPI 
app = FastAPI()

# minimal app - get request
# create a router decorator 
@app.get("/", tags = ['ROOT'])
async def root():
    return "ICE CREAM SHOP"

# OTHERS HTTP METHODS OR OPERATIONS (CRUD)  

# variables
flavors = [
    {"flavor_id": "1",
    "Flavor": "Chocolat"},
    {"flavor_id": "2",
    "Flavor": "Cream"},
    {"flavor_id": "3",
    "Flavor": "Strawberry"},
    {"flavor_id": "4",
    "Flavor": "Passionfruit"},
]

# Create - Post
@app.post("/flavors", tags = ['flavors'])
async def add_new_favor(flavor:dict) -> dict:
    flavors.append(flavor)
    return {"data": "A new flavor has been added!"}

# Read - Get
@app.get("/flavors", tags = ['flavors'])
async def get_flavors() -> dict:
    return {"data": flavors}

# Update - Put
@app.put("/flavors/{flavor_id}", tags = ['flavors'])
async def update_flavor(flavor_id:int, body:dict) -> dict:
    for flavor in flavors: 
        if int(flavor['flavor_id']) == flavor_id:
            flavor["Flavor"] = body["Flavor"]
            return {"data": f"The flavor correspondent to the id {flavor_id} has been updated!"}
        else:
            return {"data": f"The id {flavor_id} was not found!"}

# Delete - Delete
@app.delete("/flavors/{flavor_id}", tags = ['flavors'])
async def delete_flavor(flavor_id:int) -> dict:
    for flavor in flavors: 
        if int(flavor['flavor_id']) == flavor_id:
            flavors.remove(flavor)
            return {"data": f"The flavor correspondent to the id {flavor_id} has been deleted!"}
        else:
            return {"data": f"The id {flavor_id} was not found!"}
