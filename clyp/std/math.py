import math

E = math.e
PI = math.pi
TAU = 2 * math.pi

def sqrt(x: float) -> float:
    """
    Return the square root of a number.
    """
    return math.sqrt(x)

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def sub(a, b):
    """Return the difference of a and b."""
    return a - b

def mul(a, b):
    """Return the product of a and b."""
    return a * b

def div(a, b):
    """Return the quotient of a and b."""
    return a / b

def sin(x: float) -> float:
    """
    Return the sine of an angle (in radians).
    """
    return math.sin(x)

def cos(x: float) -> float:
    """
    Return the cosine of an angle (in radians).
    """
    return math.cos(x)

def tan(x: float) -> float:
    """
    Return the tangent of an angle (in radians).
    """
    return math.tan(x)

def log(x: float, base: float = math.e) -> float:
    """
    Return the logarithm of a number with a given base.
    """
    return math.log(x, base)

def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def exp(x: float) -> float:
    """
    Return the exponential of a number.
    """
    return math.exp(x)

def pow(base: float, exp: float) -> float:
    """
    Return the power of a number.
    """
    return math.pow(base, exp)

def floor(x: float) -> int:
    """
    Return the largest integer less than or equal to x.
    """
    return math.floor(x)

def ceil(x: float) -> int:
    """
    Return the smallest integer greater than or equal to x.
    """
    return math.ceil(x)

def hypot(x: float, y: float) -> float:
    """
    Return the Euclidean norm, sqrt(x^2 + y^2).
    """
    return math.hypot(x, y)

def radians(degrees: float) -> float:
    """
    Convert an angle from degrees to radians.
    """
    return degrees * (PI / 180)

def degrees(radians: float) -> float:
    """
    Convert an angle from radians to degrees.
    """
    return radians * (180 / PI)
