from flask import Blueprint, request, jsonify
from models.Booking_model import Booking
from models.Host_model import Host  # Import the Guest model
from bson import ObjectId
import bcrypt
import jwt
import datetime
from config.app_config import get_bookings_collection

bookings_collection = get_bookings_collection()
bookings_route = Blueprint("bookings", __name__)

# Create a new booking
@bookings_route.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    property_id = data.get("property_id")
    host_id = data.get("host_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    total_price = data.get("total_price")

    # Create a new Booking instance with the guest_id
    new_booking = Booking(property_id, host_id, check_in, check_out, total_price)

    # Insert the new booking into the database (Replace `bookings_collection` with your MongoDB collection)
    result = bookings_collection.insert_one(new_booking.to_dict())

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Booking created successfully!"}), 201


# Retrieve all bookings of a specific guest
@bookings_route.route("/bookings/<string:host_id>", methods=["GET"])
def get_bookings_by_guest(host_id):
    # Retrieve all bookings from the database associated with the given guest_id (Replace `bookings_collection` with your MongoDB collection)
    all_bookings = bookings_collection.find({"host_id": host_id})

    # Convert the MongoDB documents to a list of dictionaries
    bookings_list = []
    for booking_data in all_bookings:
        bookings_list.append({
            "id": str(booking_data["_id"]),
            "property_id": booking_data["property_id"],
            "host_id": booking_data["host_id"],
            "check_in": booking_data["check_in"],
            "check_out": booking_data["check_out"],
            "total_price": booking_data["total_price"]
        })

    # Replace the return statement with appropriate responses
    return jsonify(bookings_list), 200


# Retrieve all bookings
@bookings_route.route("/bookings", methods=["GET"])
def get_all_bookings():
    # Retrieve all bookings from the database (Replace `bookings_collection` with your MongoDB collection)
    all_bookings = bookings_collection.find()

    # Convert the MongoDB documents to a list of dictionaries
    bookings_list = []
    for booking_data in all_bookings:
        bookings_list.append({
            "id": str(booking_data["_id"]),
            "property_id": booking_data["property_id"],
            "host_id": booking_data["host_id"],
            "check_in": booking_data["check_in"],
            "check_out": booking_data["check_out"],
            "total_price": booking_data["total_price"]
        })

    # Replace the return statement with appropriate responses
    return jsonify(bookings_list), 200


# Retrieve a booking by ID
@bookings_route.route("/bookings/<string:booking_id>", methods=["GET"])
def get_booking_by_id(booking_id):
    # Retrieve the booking document from the database based on the booking_id (Replace `bookings_collection` with your MongoDB collection)
    booking_data = bookings_collection.find_one({"_id": ObjectId(booking_id)})

    if booking_data:
        booking_obj = {
            "id": str(booking_data["_id"]),
            "property_id": booking_data["property_id"],
            "host_id": booking_data["host_id"],
            "check_in": booking_data["check_in"],
            "check_out": booking_data["check_out"],
            "total_price": booking_data["total_price"]
        }
        return jsonify(booking_obj), 200
    else:
        return jsonify({"message": "Booking not found"}), 404


# Update a booking by ID
@bookings_route.route("/bookings/<string:booking_id>", methods=["PUT"])
def update_booking(booking_id):
    data = request.get_json()
    property_id = data.get("property_id")
    host_id = data.get("host_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    total_price = data.get("total_price")

    updated_booking = Booking(property_id, host_id, check_in, check_out, total_price)

    # Update the booking document in the database based on the booking_id (Replace `bookings_collection` with your MongoDB collection)
    result = bookings_collection.update_one({"_id": ObjectId(booking_id)}, {"$set": updated_booking.to_dict()})

    if result.modified_count > 0:
        return jsonify({"message": "Booking updated successfully!"}), 200
    else:
        return jsonify({"message": "Booking not found"}), 404

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Booking updated successfully!"}), 200


# Delete a booking by ID
@bookings_route.route("/bookings/<string:booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    # Delete the booking document from the database based on the booking_id (Replace `bookings_collection` with your MongoDB collection)
    result = bookings_collection.delete_one({"_id": ObjectId(booking_id)})

    if result.deleted_count > 0:
        return jsonify({"message": "Booking deleted successfully!"}), 200
    else:
        return jsonify({"message": "Booking not found"}), 404

    # Replace the return statement with appropriate responses
    return jsonify({"message": "Booking deleted successfully!"}), 200






# from flask import Blueprint, request, jsonify
# from models.Booking_model import Booking
# from bson import ObjectId
# import bcrypt
# import jwt
# import datetime
# bookings_route = Blueprint("bookings", __name__)

# # Create a new booking
# @bookings_route.route("/bookings", methods=["POST"])
# def create_booking():
#     data = request.get_json()
#     property_id = data.get("property_id")
#     guest_id = data.get("guest_id")
#     check_in = data.get("check_in")
#     check_out = data.get("check_out")
#     total_price = data.get("total_price")

#     new_booking = Booking(property_id, guest_id, check_in, check_out, total_price)

#     # Insert the new booking into the database (Replace `bookings_collection` with your MongoDB collection)
#     # result = bookings_collection.insert_one(new_booking.to_dict())
    
#     # Replace the return statement with appropriate responses
#     return jsonify({"message": "Booking created successfully!"}), 201


# # Retrieve all bookings
# @bookings_route.route("/bookings", methods=["GET"])
# def get_all_bookings():
#     # Retrieve all bookings from the database (Replace `bookings_collection` with your MongoDB collection)
#     # all_bookings = bookings_collection.find()
    
#     # Convert the MongoDB documents to a list of dictionaries
#     bookings_list = []
#     for booking_data in get_all_bookings:
#         bookings_list.append({
#             "id": str(booking_data["_id"]),
#             "property_id": booking_data["property_id"],
#             "guest_id": booking_data["guest_id"],
#             "check_in": booking_data["check_in"],
#             "check_out": booking_data["check_out"],
#             "total_price": booking_data["total_price"]
#         })
    
#     # Replace the return statement with appropriate responses
#     return jsonify(bookings_list), 200


# # Retrieve a booking by ID
# @bookings_route.route("/bookings/<string:booking_id>", methods=["GET"])
# def get_booking_by_id(booking_id):
#     # Retrieve the booking document from the database based on the booking_id (Replace `bookings_collection` with your MongoDB collection)
#     booking_data = bookings_collection.find_one({"_id": ObjectId(booking_id)})
    
#     if booking_data:
#         booking_obj = {
#             "id": str(booking_data["_id"]),
#             "property_id": booking_data["property_id"],
#             "guest_id": booking_data["guest_id"],
#             "check_in": booking_data["check_in"],
#             "check_out": booking_data["check_out"],
#             "total_price": booking_data["total_price"]
#         }
#         return jsonify(booking_obj), 200
#     else:
#         return jsonify({"message": "Booking not found"}), 404

#     # Replace the return statement with appropriate responses
#     return jsonify({"message": "Booking not found"}), 404


# # Update a booking by ID
# @bookings_route.route("/bookings/<string:booking_id>", methods=["PUT"])
# def update_booking(booking_id):
#     data = request.get_json()
#     property_id = data.get("property_id")
#     guest_id = data.get("guest_id")
#     check_in = data.get("check_in")
#     check_out = data.get("check_out")
#     total_price = data.get("total_price")

#     updated_booking = Booking(property_id, guest_id, check_in, check_out, total_price)

#     # Update the booking document in the database based on the booking_id (Replace `bookings_collection` with your MongoDB collection)
#     # result = bookings_collection.update_one({"_id": ObjectId(booking_id)}, {"$set": updated_booking.to_dict()})
    
#     # if result.modified_count > 0:
#     #     return jsonify({"message": "Booking updated successfully!"}), 200
#     # else:
#     #     return jsonify({"message": "Booking not found"}), 404

#     # Replace the return statement with appropriate responses
#     return jsonify({"message": "Booking updated successfully!"}), 200


# # Delete a booking by ID
# @bookings_route.route("/bookings/<string:booking_id>", methods=["DELETE"])
# def delete_booking(booking_id):
#     # Delete the booking document from the database based on the booking_id (Replace `bookings_collection` with your MongoDB collection)
#     # result = bookings_collection.delete_one({"_id": ObjectId(booking_id)})
    
#     # if result.deleted_count > 0:
#     #     return jsonify({"message": "Booking deleted successfully!"}), 200
#     # else:
#     #     return jsonify({"message": "Booking not found"}), 404

#     # Replace the return statement with appropriate responses
#     return jsonify({"message": "Booking deleted successfully!"}), 200
