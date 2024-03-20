import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

collection = db["rohit"]

data = [
    {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
    {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
    {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
]

result = collection.insert_many(data)

print("Inserted ID:", result.inserted_id)
