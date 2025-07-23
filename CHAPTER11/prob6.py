#write a class vector n dimensions .overload the + and* which calculate sum and(.) product of them

class Vector:
    def __init__(self, *args):
        """Initialize a vector with n dimensions."""
        self.components = args

    def __add__(self, other):
        """Overload the + operator to add two vectors."""
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __mul__(self, scalar):
        """Overload the * operator to multiply a vector by a scalar."""
        return Vector(*(a * scalar for a in self.components))

    def __str__(self):
        """Return a string representation of the vector."""
        return ' + '.join(f"{c}i" for c in self.components)