from email.mime import image
from unittest import result
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi_pagination import Page, add_pagination, paginate


class User(BaseModel):
    userId: str
    id: int
    title: str
    image: str
    details: str
    completed: str
    
user_db = [
     {
         
         "userId": "33568",
         "id": "1001",
         "title": "artistry",
         "image": "img1.jpg",
         "details":"นางเงือกไม่ใช่นาย",
         "completed": "Y"
     },
     {
         
         "userId": "33569",
         "id": "1002",
         "title": "artistry",
         "image": "img2.jpg",
         "details":"สิงโตว่าซั่น",
         "completed": "N"
     },
     {
         
         "userId": "33570",
         "id": "1003",
         "title": "artistry",
         "image": "img3.jpg",
         "details":"เป่ายิงฉุบ",
         "completed": "Y"
     },
     {
         
         "userId": "33571",
         "id": "1004",
         "title": "artistry",
         "image": "img4.jpg",
         "details":"กินข้าวหรือยัง",
         "completed": "Y"
     },
     {
         
         "userId": "33572",
         "id": "1005",
         "title": "artistry",
         "image": "img5.jpg",
         "details":"เกี๋ยวเตี๋ยวไก่ไข่เป็ด",
         "completed": "Y"
     },
     {
         
         "userId": "33573",
         "id": "1006",
         "title": "artistry",
         "image": "img6.jpg",
         "details":"ทางที่ดีคือทางอะไร",
         "completed": "Y"
     }
 ]

app = FastAPI()

#show all data
@app.get('/')
async def all_user():
    return user_db

#add data to database
@app.post('/user')
async def create_user(user: User):
    user = user_db.append(user)
    return user_db[-1]

#show data by id
@app.get('/user/{id}')
async def user_by_id(id: int):
    user = user_db[id - 1]
    return user

#edit data and update to database
@app.put('/user/{id}')
async def update_user(id: int, user: User):
    user_db[id - 1].update(**user.dict())
    result = {'msg', f"user Id {id} Update Successful!!.."}
    return result

#delete data by id
@app.delete('/user/{id}')
async def delete_user(id: int):
    user = user_db[id - 1]
    user_db.pop(id - 1)
    result = {'msg', f"{user['userId']} was delete!.."}
    return result

#show data by page number and limit data
@app.get('/user', response_model = Page[User])
async def page_limit_data():
    return paginate(user_db)

add_pagination(app)
