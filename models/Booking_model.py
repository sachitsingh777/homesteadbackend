class Booking:
    def __init__(self, property_id, host_id, check_in, check_out, total_price):
        self.property_id = property_id
        self.host_id = host_id 
        self.check_in = check_in
        self.check_out = check_out
        self.total_price = total_price

    def to_dict(self):
        return {
            "property_id": self.property_id,
            "host_id": self.host_id,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "total_price": self.total_price
        }
