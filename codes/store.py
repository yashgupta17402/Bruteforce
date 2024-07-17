from pymongo import MongoClient

# Replace <username>, <password>, and <dbname> with your MongoDB Atlas credentials and database name
client = MongoClient('mongodb+srv://yashgupta514:2fXMnsw2h9InLGI1@bruteforce.wqf9kmc.mongodb.net/')
# Connect to your database
db = client['bruteforce']

# Connect to your collection
collection = db['bruteforce']

# The output you want to store
output_word = "Hello"

# Insert the output into the collection
collection.insert_one({"output": output_word})

print("Output stored in MongoDB Atlas")
