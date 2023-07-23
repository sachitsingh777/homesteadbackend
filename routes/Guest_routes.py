from flask import Blueprint, request, jsonify
from models.Guest_model import Guest 
from bson import ObjectId
import bcrypt
import jwt
import datetime
from config.app_config import get_hosts_collection

guests_collection = get_hosts_collection()
guests_route = Blueprint("guests", __name__)

# Create a new guest
@guests_route.route("/guests", methods=["POST"])
def create_guest():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    new_guest = Guest(name, email, phone)

    # Insert the new guest into the database (Replace `guests_collection` with your MongoDB collection)
    # result = guests_collection.insert_one(new_guest.to_dict())
    
    # Replace the return statement with appropriate responses
    return jsonify({"message": "Guest created successfully!"}), 201


# Retrieve all guests
@guests_route.route("/guests", methods=["GET"])
def get_all_guests():
    # Retrieve all guests from the database (Replace `guests_collection` with your MongoDB collection)
    all_guests = guests_collection.find()
    
    # Convert the MongoDB documents to a list of dictionaries
    guests_list = []
    for guest_data in all_guests:
        guests_list.append({
            "id": str(guest_data["_id"]),
            "name": guest_data["name"],
            "email": guest_data["email"],
            "phone": guest_data["phone"]
        })
    
    # Replace the return statement with appropriate responses
    return jsonify(guests_list), 200


# Retrieve a guest by ID
@guests_route.route("/guests/<string:guest_id>", methods=["GET"])
def get_guest_by_id(guest_id):
    # Retrieve the guest document from the database based on the guest_id (Replace `guests_collection` with your MongoDB collection)
    guest_data = guests_collection.find_one({"_id": ObjectId(guest_id)})
    
    if guest_data:
        guest_obj = {
            "id": str(guest_data["_id"]),
            "name": guest_data["name"],
            "email": guest_data["email"],
            "phone": guest_data["phone"]
        }
        return jsonify(guest_obj), 200
    else:
        return jsonify({"message": "Guest not found"}), 404

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Guest not found"}), 404


# Update a guest by ID
@guests_route.route("/guests/<string:guest_id>", methods=["PUT"])
def update_guest(guest_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    updated_guest = Guest(name, email, phone)

    # Update the guest document in the database based on the guest_id (Replace `guests_collection` with your MongoDB collection)
    # result = guests_collection.update_one({"_id": ObjectId(guest_id)}, {"$set": updated_guest.to_dict()})
    
    # if result.modified_count > 0:
    #     return jsonify({"message": "Guest updated successfully!"}), 200
    # else:
    #     return jsonify({"message": "Guest not found"}), 404

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Guest updated successfully!"}), 200


# Delete a guest by ID
@guests_route.route("/guests/<string:guest_id>", methods=["DELETE"])
def delete_guest(guest_id):
    # Delete the guest document from the database based on the guest_id (Replace `guests_collection` with your MongoDB collection)
    # result = guests_collection.delete_one({"_id": ObjectId(guest_id)})
    
    # if result.deleted_count > 0:
    #     return jsonify({"message": "Guest deleted successfully!"}), 200
    # else:
    #     return jsonify({"message": "Guest not found"}), 404

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Guest deleted successfully!"}), 200
