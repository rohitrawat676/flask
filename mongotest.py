import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

collection = db["rohit"]

data = [
    {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
    {"name": "John Doe", "email": "john.doe@example.com", "age": 39},
    {"name": "John Doe", "email": "john.doe@example.com", "age": 40}
]

filter_criteria = {"age": {"$lt": 37}}
update_operation = {"$set": {"name": "rohit"}}

result = collection.update_many(filter_criteria, update_operation)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)
