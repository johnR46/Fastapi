# Result Test Createder-Back-End
## Path 1
- basic github (0/1)
    - fork this repository
    - clone and coding
    - push and pull request to this repository 
 

## Path 2
- connect database (0/1)
    - `Database` : `sqlite3` or Other you can do

### Part 3 : Data Schema
- main schema
    ```json
    {
    "userId": ?
    "id": ?
    "title":?
    "image": ?
    "details": ?
    "completed": ?
    }
    ```
    - schema (1/1)
    - data type ที่มาพร้อม schema (0/1) ( field "completed" ควรจะเป็น boolean มั้ย)
## Part 4 : CRUD Endpoint (Create, Read, Update and Delete)
- swagger ui (1/1)
- add data to database (1/1)
  - ใส่ได้ก็จริง แต่ว่า ตอน add ทำไม field "id" ตอนใส่ไปทำไม type เป็น int
  - id,userId ควรจะเป็น pk จาก database 
- show all data (1/1)
- show data by id (0/1)
 - search by id ไม่ถูกต้อง
 - input ที่รับมา search ไม่ตรงกับ field data ที่จะค้นหา 
- edit data and update to database (0/1)
 - วิธีการค้นหา id มาเพื่อ update ไม่ถูก
 - input ที่รับมา update ไม่ตรงกับ field data ที่จะค้นหา
 - การ update data ไม่ควรจะ update pk 
- delete data by id (0/1)
 - วิธีการค้นหา id มาเพื่อ delete ไม่ถูก
- sort by last time created (0/1)
- sort by last time updated (0/1)
- select completed only (0/1)
- you can do (extra)
### Part 2 : Pagination (Extra)
- show 5 data by page number (0/1)
- show data by page number and limit data (extra) (1/1)
    - show x data by page number ; x = limit data

## รวมคะแนนจากผลลัพธ์ 5/15
## comment code
    - data type ไม่ make sense (Ex. "completed":"y" ทำไมไม่ใช่ type boolean)
    - ทำ api ทำไม ไม่ต่อ database
    - ไม่เขียน readme (อธิบายว่าโค้ดนี้ทำอะไร) ใส่มาใน github
    - search by id , delete by id , update by id logic ไม่ถูก
