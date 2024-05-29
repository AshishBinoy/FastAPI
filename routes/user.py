from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schema.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.local.user.find())

@user.get('/{id}')
async def find_specific_user(id):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))



@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())  
 
@user.delete('/{id}')
async def delete_user(id):
    conn.local.user.delete_one({"_id": ObjectId(id)})
    return usersEntity(conn.local.user.find())

