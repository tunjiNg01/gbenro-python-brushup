class InstanceTracker:
    """A class that tracks how many active instances exist."""

    active_count = 0  # Class variable to track active instances

    def __init__(self, name: str):
        self.name = name
        InstanceTracker.active_count += 1
        print(f"Instance '{self.name}' created. Active count: {InstanceTracker.active_count}")

    def __del__(self):
        InstanceTracker.active_count -= 1
        print(f"Instance '{self.name}' deleted. Active count: {InstanceTracker.active_count}")

    @classmethod
    def get_active_count(cls):
        """Return the number of active instances."""
        return cls.active_count


# Example 
if __name__ == "__main__":
    a = InstanceTracker("First")
    b = InstanceTracker("Second")
    print("Currently active:", InstanceTracker.get_active_count())
    del a
    print("Currently active:", InstanceTracker.get_active_count())