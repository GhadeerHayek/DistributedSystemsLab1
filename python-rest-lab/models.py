"""
    models.py contains the definition of models.
    User Model:
        id: int
        name: str
        email: str
"""

class User:
    def __init__(self, id, name, email):
        # Initialize a User object
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        # String representation of a User object
        return f'<User {self.id} {self.name} {self.email}>'

    def to_dict(self):
        # Helper function to convert a User object to a dictionary
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }