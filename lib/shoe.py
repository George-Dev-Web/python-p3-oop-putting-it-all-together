# shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use an internal attribute
        self.size = size  # Call the setter
        self.condition = "Old"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"