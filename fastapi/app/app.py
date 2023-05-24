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
    {"id": "1",
    "Flavor": "Chocolat"},
    {"id": "2",
    "Flavor": "Cream"},
    {"id": "3",
    "Flavor": "Strawberry"},
    {"id": "4",
    "Flavor": "Passionfruit"},
]

# Create - Post
@app.post("/flavors", tags = ['flavors'])
async def add_new_favor(flavor:dict) -> dict:
    flavors.append(flavor)
    return {"data": "A new flavor have been added!"}

# Read - Get
@app.get("/flavors", tags = ['flavors'])
async def get_flavors() -> dict:
    return {"data": flavors}

# Update - Put
@app.put("/flavors/{id}", tags = ['flavors'])
async def update_flavor(id:int, body:dict) -> dict:
    for flavor in flavors: 
        if int(flavor['id']) == id:
            flavor["Flavor"] = body["Flavor"]
            return {"data": f"The flavor correspondent to the id {id} has been updated!"}
        else:
            return {"data": f"The id {id} was no found!"}

# Delete - Delete
@app.delete("/flavors/{id}", tags = ['flavors'])
async def delete_flavor(id:int) -> dict:
    for flavor in flavors: 
        if int(flavor['id']) == id:
            flavor.remove(flavor)
            return {"data": "Flavor has been deleted!"}
        else:
            return {"data": "The entered id was no found!"}
