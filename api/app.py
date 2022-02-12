from fastapi import FastAPI, HTTPException, Body
from typing import Optional
from article import Article
from db import (
    fetch_one_article,
    fetch_all_articles,
    create_article,
    update_article,
    remove_article,
)

app = FastAPI()


@app.get("/", status_code=200)
async def root():
     return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}


@app.get("/articles/")
async def get_articles(_limit: int, _skip: Optional[int] = None):
    if _limit <= 50:
        response = await fetch_all_articles(_limit, _skip)
        return response 
    return {"message": "limit should be equal or less than 50"}
    

@app.get("/articles/{id}", response_model=Article)
async def get_articles_by_id(id: int):
    response = await fetch_one_article(id)
    if response:
        return response
    raise HTTPException(404, f"There is no article with the id {id}")

@app.post("/articles/", response_model=Article)
async def post_article(article: Article):
    response = await create_article(article)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/articles/{id}")
async def put_article(id: int, payload: Article = Body(...)):
    payload = {k: v for k, v in payload.dict().items() if v is not None}
    response = await update_article(id, payload)
    if response:
        return response
    raise HTTPException(404, f"There is no article with the id {id}")


@app.delete("/articles/{id}")
async def delete_article(id: int):
    response = await remove_article(id)
    if response:
        return "Successfully deleted article"
    raise HTTPException(404, f"There is no article with the id {id}")