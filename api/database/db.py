from motor import  motor_asyncio
from model.article import Article
from decouple import config


client = motor_asyncio.AsyncIOMotorClient(config("MONGO_ACCESS"))
database = client.Articles
collection = database.articles

async def fetch_one_article(id: int):
    document = await collection.find_one({"id": id})
    return document

async def fetch_all_articles(_limit: int, _skip: int = 0):
    articles = []
    cursor = collection.find({}).limit(_limit).skip(_skip)
    async for document in cursor:
        articles.append(Article(**document))
    return articles

async def create_article(article):
    document = article.dict()
    result = await collection.insert_one(document)
    return document


async def update_article(id: int, payload: dict):
    document = await collection.find_one({"id": id})
    if document: 
        updated_document = await collection.update_one({"id": id}, {"$set": payload})
        if updated_document:
            return payload

async def remove_article(id: int):
    await collection.delete_one({"id": id})
    return True

async def do_count():
    count = await collection.count_documents({})
    return count
