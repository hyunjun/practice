#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from models import Todo

app = FastAPI()


#   https://www.youtube.com/watch?v=cbASjoZZGIw
#   http://127.0.0.1:8000/docs
#   http://127.0.0.1:8000/redoc


#   https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []


#   Get all todos
#   ❯ curl 'http://127.0.0.1:8000/todos'
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#   Get single todo
#   ❯ curl 'http://127.0.0.1:8000/todos/1'
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}

#   Create a todo
'''
❯ curl --request POST 'http://127.0.0.1:8000/todos' \
--header 'Content-Type: application/json' \
--data-raw '{
      "id": 1,
      "item": "Edit a blog post"
}'
{"message":"Todo has been added"}
'''
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

#   Update a todo
'''
❯ curl --request PUT 'http://127.0.0.1:8000/todos/1' \
--header 'Content-Type: application/json' \
--data-raw '{
      "id": 1,
      "item": "Delete a blog post"
}'
{"todo":{"id":1,"item":"Delete a blog post"}}
'''
@app.put("/todos/{todo_id}")
async def update_todos(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "Todo has been added"}

#   Delete a todo
#   ❯ curl --request DELETE 'http://127.0.0.1:8000/todos/1'
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": 'Todo has been deleted'}
    return {"message": "No todos found"}
