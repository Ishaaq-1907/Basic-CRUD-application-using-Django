from pymongo import MongoClient

client = MongoClient("mongodb+srv://Fardeen:mohamedishaaq1907@cluster0.medb8he.mongodb.net/")
db = client["datas"]
col = db["users"]
