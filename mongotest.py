import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

collection = db["rohit"]

data = [
    {"name": "Rohit Rawat", "email": "john.doe@example.com", "age": 910},
    {"name": "Nidhi Semwal", "email": "nidhi.semwal@example.com", "age": 33},
    {"name": "Soumya Bisht", "email": "soumya.bisht@example.com", "age": 221}
]

filter_criteria = {"age": {"$lt": 220}}
update_operation = {"$set": {"name": "rohan"}}

result = collection.update_one(filter_criteria, update_operation)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)
