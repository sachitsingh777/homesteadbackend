class Property:
    def __init__(self, host_id, property_type, location, description, max_guests, amenities, image, price):
        self.host_id = host_id
        self.property_type = property_type
        self.location = location
        self.description = description
        self.max_guests = max_guests
        self.amenities = amenities
        self.image = image
        self.price=price

    def to_dict(self):
        return {
            "host_id": self.host_id,
            "property_type": self.property_type,
            "location": self.location,
            "description": self.description,
            "max_guests": self.max_guests,
            "amenities": self.amenities,
            "image": self.image,
            "price":self.price
        }
