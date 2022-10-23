
from fastapi import APIRouter

router=APIRouter()




@router.get("/users/", tags=["users"])
async def read_user():
    return [{"username":"Rick"},{"username":"Monty"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username":"fakeusername"}

@router.get("/users/{username}", tags=["users"])
async def read_user(username:str):
    return {"username":username}
