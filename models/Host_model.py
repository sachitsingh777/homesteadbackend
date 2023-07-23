class Host:
    def __init__(self, name, email, password, image):
        self.name = name
        self.email = email
        self.password = password
        self.image = image

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "image": self.image
        }

    def is_valid(self):
        # Check if all required fields are filled
        if not self.name or not self.email or not self.password or not self.image:
            return False
        return True
