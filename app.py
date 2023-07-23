from flask import Flask,request,jsonify
from flask_cors import CORS
from routes.User_routes import users_Detail
from routes.Host_routes import hosts_Detail
from routes.Guest_routes import guests_route
from routes.Booking_routes import bookings_route
from routes.Property_routes import properties_route
import os
PORT = os.getenv("PORT")
app = Flask(__name__)
CORS(app, origins='*')


app.register_blueprint(users_Detail, url_prefix="/users")
app.register_blueprint(hosts_Detail, url_prefix="/hosts")
app.register_blueprint(bookings_route, url_prefix="/booking")
app.register_blueprint(guests_route, url_prefix="/guests")
app.register_blueprint(properties_route, url_prefix="/properties")

@app.route('/')
def hello_world():
    return jsonify('Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)