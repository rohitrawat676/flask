import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

collection = db["mycollection"]

data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

result = collection.insert_one(data)

print("Inserted ID:", result.inserted_id)
