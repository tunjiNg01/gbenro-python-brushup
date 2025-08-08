
class Dog:
    """A basic Dog class."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def get_info(self):
        print(f"Dog Name: {self.name}, Age: {self.age}")


class BullDog(Dog):
    """A BullDog is a type of Dog with its own behavior."""

    def __init__(self, name: str, age: int, weight: float):
        super().__init__(name, age)  # Call Dog's constructor
        self.weight = weight

    def bark(self):
        # Override the bark method for a deeper bark
        print(f"{self.name} says: WOOF! (in a deep BullDog voice)")

    def get_info(self):
        # Override to include weight
        print(f"BullDog Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg")