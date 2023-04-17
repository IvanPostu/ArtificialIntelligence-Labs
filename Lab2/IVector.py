import array

class IVector:
    def __init__(self, values):
        self.values = values

    def norm(self):
        return sum(x**2 for x in self.values) ** 0.5

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be the same length")
        return IVector([x + y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be the same length")
        return IVector([x - y for x, y in zip(self.values, other.values)])

    def __mul__(self, scalar):
        return IVector([x * scalar for x in self.values])

    def __truediv__(self, scalar):
        return IVector([x / scalar for x in self.values])

    def dot(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be the same length")
        return sum(x * y for x, y in zip(self.values, other.values))

    def cross(self, other):
        if len(self.values) != 3 or len(other.values) != 3:
            raise ValueError("Cross product is only defined for 3-dimensional vectors")
        x1, y1, z1 = self.values
        x2, y2, z2 = other.values
        return IVector([y1 * z2 - y2 * z1, z1 * x2 - z2 * x1, x1 * y2 - x2 * y1])

    def __str__(self):
        return "Vector({})".format(self.values)


v1 = IVector(array.array('f', [1, 2, 3]))
v2 = IVector([4, 5, 6])
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 2
v6 = v2 / 2
dot_product = v1.dot(v2)
cross_product = v1.cross(v2)

print(v1, v2, v3, v4, v5, v6, dot_product, cross_product)
