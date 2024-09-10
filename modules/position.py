"""Module for handling 2D positions."""


from dataclasses import dataclass


@dataclass
class Point2D:
    """Base class for 2D points."""
    x: float
    y: float

    def update(self, new_x: float, new_y: float):
        """Update the position of this point."""
        self.x = new_x
        self.y = new_y
    
    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return False


@dataclass
class Point3D:
    """Base class for 2D points."""
    x: float
    y: float
    z: float

    def update(self, new_x: float, new_y: float, new_z: float):
        """Update the position of this point."""
        self.x = new_x
        self.y = new_y
        self.z = new_z
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, tuple) and len(other) == 3:
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        return False