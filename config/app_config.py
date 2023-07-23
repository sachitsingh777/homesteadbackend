import os
from dotenv import load_dotenv
load_dotenv()  # Load the environment variables from the .env file
from pymongo import MongoClient

def get_mongo_client():
    MONGO_URL = os.getenv("MONGO_URL")
    client = MongoClient(MONGO_URL)
    return client

def get_users_collection():
    client = get_mongo_client()
    db = client["Homestead"]
    users_collection = db["users"]
    return users_collection

def get_guests_collection():
    client = get_mongo_client()
    db = client["Homestead"]
    hosts_collection = db["guests"]
    return hosts_collection

def get_property_collection():
    client = get_mongo_client()
    db = client["Homestead"]
    hosts_collection = db["property"]
    return hosts_collection

def get_bookings_collection():
    client = get_mongo_client()
    db = client["Homestead"]
    hosts_collection = db["bookings"]
    return hosts_collection

def get_hosts_collection():
    client = get_mongo_client()
    db = client["Homestead"]
    hosts_collection = db["hosts"]
    return hosts_collection