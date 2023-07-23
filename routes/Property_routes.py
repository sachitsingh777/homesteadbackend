from flask import Blueprint, request, jsonify
from models.Property_model import Property
from models.Host_model import Host  # Import the Host model
from bson import ObjectId
import bcrypt
import jwt
import datetime
from config.app_config import get_property_collection

properties_collection = get_property_collection()
properties_route = Blueprint("properties", __name__)

# Create a new property
@properties_route.route("/create", methods=["POST"])
def create_property():
    data = request.get_json()
    host_id = data.get("host_id")  # Get the host_id from the request data
    property_type = data.get("property_type")
    location = data.get("location")
    description = data.get("description")
    max_guests = data.get("max_guests")
    amenities = data.get("amenities")
    image = data.get("image") 
    price = data.get("price")
 
    new_property = Property(host_id, property_type, location, description, max_guests, amenities, image, price)

    # Insert the new property into the database (Replace `properties_collection` with your MongoDB collection)
    result = properties_collection.insert_one(new_property.to_dict())

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Property created successfully!"}), 201

# Retrieve all properties
@properties_route.route("/allproperties", methods=["GET"])
def get_all_properties():
    # Retrieve all properties from the database (Replace `properties_collection` with your MongoDB collection)
    all_properties = properties_collection.find()

    # Convert the MongoDB documents to a list of dictionaries
    properties_list = []
    for property_data in all_properties:
        properties_list.append({
            "id": str(property_data["_id"]),
            "host_id": property_data["host_id"],
            "property_type": property_data["property_type"],
            "location": property_data["location"],
            "description": property_data["description"],
            "max_guests": property_data["max_guests"],
            "amenities": property_data["amenities"],
            "image": property_data["image"],
            "price": property_data["price"]
        })

    # Replace the return statement with appropriate responses
    return jsonify(properties_list), 200

# Retrieve a property by ID
@properties_route.route("/properties/<string:property_id>", methods=["GET"])
def get_property_by_id(property_id):
    # Retrieve the property document from the database based on the property_id (Replace `properties_collection` with your MongoDB collection)
    property_data = properties_collection.find_one({"_id": ObjectId(property_id)})

    if property_data:
        property_obj = {
            "id": str(property_data["_id"]),
            "host_id": property_data["host_id"],
            "property_type": property_data["property_type"],
            "location": property_data["location"],
            "description": property_data["description"],
            "max_guests": property_data["max_guests"],
            "amenities": property_data["amenities"],
            "image": property_data["image"],
            "price": property_data["price"]
        }
        return jsonify(property_obj), 200
    else:
        return jsonify({"message": "Property not found"}), 404

# Update a property by ID
@properties_route.route("/properties/<string:property_id>", methods=["PUT"])
def update_property(property_id):
    data = request.get_json()
    host_id = data.get("host_id")  # Get the host_id from the request data
    property_type = data.get("property_type")
    location = data.get("location")
    description = data.get("description")
    max_guests = data.get("max_guests")
    amenities = data.get("amenities")
    image = data.get("image") 
    price = data.get("price")  # Get the image URL from the request data

    updated_property = Property(host_id, property_type, location, description, max_guests, amenities, image, price)

    # Update the property document in the database based on the property_id (Replace `properties_collection` with your MongoDB collection)
    result = properties_collection.update_one({"_id": ObjectId(property_id)}, {"$set": updated_property.to_dict()})

    if result.modified_count > 0:
        return jsonify({"message": "Property updated successfully!"}), 200
    else:
        return jsonify({"message": "Property not found"}), 404

# Delete a property by ID
@properties_route.route("/properties/<string:property_id>", methods=["DELETE"])
def delete_property(property_id):
    # Delete the property document from the database based on the property_id (Replace `properties_collection` with your MongoDB collection)
    result = properties_collection.delete_one({"_id": ObjectId(property_id)})

    if result.deleted_count > 0:
        return jsonify({"message": "Property deleted successfully!"}), 200
    else:
        return jsonify({"message": "Property not found"}), 404



@properties_route.route("/hostproperties/<string:host_id>", methods=["GET"])
def get_properties_by_guest(host_id):
    # Retrieve all bookings from the database associated with the given guest_id (Replace `bookings_collection` with your MongoDB collection)
    all_property = properties_collection.find({"host_id": host_id})

    # Convert the MongoDB documents to a list of dictionaries
    property_list = []
    for property_data in all_property:
        property_list.append({
            "id": str(property_data["_id"]),
            "host_id": property_data["host_id"],
            "property_type": property_data["property_type"],
            "location": property_data["location"],
            "description": property_data["description"],
            "max_guests": property_data["max_guests"],
            "amenities": property_data["amenities"],
            "image": property_data["image"],
            "price": property_data["price"]
        })

    # Replace the return statement with appropriate responses
    return jsonify(property_list), 200
