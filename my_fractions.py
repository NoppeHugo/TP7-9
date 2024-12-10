class Fraction:
    """Class representing a fraction and operations on it."""

    def __init__(self, num: int = 0, den: int = 1):
        """Initializes a fraction with numerator and denominator.

        PRE : den != 0
        POST : The fraction is reduced to its simplest form.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self.num = num
        self.den = den
        self._reduce()

    def _reduce(self):
        """Reduces the fraction to its simplest form."""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
        if self.den < 0:  # Ensure denominator is always positive
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self):
        """Returns the numerator of the fraction."""
        return self.num

    @property
    def denominator(self):
        """Returns the denominator of the fraction."""
        return self.den

    def __str__(self):
        """Returns a textual representation of the fraction."""
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def as_mixed_number(self):
        """Returns the fraction as a mixed number."""
        whole_part = self.num // self.den
        remainder = abs(self.num % self.den)
        if remainder == 0:
            return str(whole_part)
        return f"{whole_part} {remainder}/{self.den}" if whole_part != 0 else f"{self.num}/{self.den}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """Adds two fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only add another Fraction.")
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtracts two fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract another Fraction.")
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiplies two fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply by another Fraction.")
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Divides two fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide by another Fraction.")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator 0.")
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __eq__(self, other: "Fraction") -> bool:
        """Checks equality of two fractions."""
        return self.num == other.num and self.den == other.den

    def __float__(self):
        """Converts the fraction to a decimal value."""
        return self.num / self.den

    def is_zero(self):
        """Checks if the fraction is zero."""
        return self.num == 0

    def is_integer(self):
        """Checks if the fraction is an integer."""
        return self.num % self.den == 0

    def is_proper(self):
        """Checks if the fraction is proper (absolute value < 1)."""
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Checks if the fraction is a unit fraction (numerator = 1)."""
        return abs(self.num) == 1

    def is_adjacent_to(self, other: "Fraction") -> bool:
        """Checks if two fractions are adjacent (difference is a unit fraction)."""
        diff = self - other
        return abs(diff.num) == 1 and diff.den == 1
