class Fraction:
    """Classe représentant une fraction et les opérations associées."""

    def __init__(self, num: int = 0, den: int = 1):
        """Initialise une fraction avec un numérateur et un dénominateur.

        PRÉCONDITION : den != 0
        POSTCONDITION : La fraction est réduite à sa forme la plus simple.
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être nul.")
        self.num = num
        self.den = den
        self._reduce()

    def _reduce(self):
        """Réduit la fraction à sa forme la plus simple."""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        commun = gcd(self.num, self.den)
        self.num //= commun
        self.den //= commun
        if self.den < 0:  # Assure que le dénominateur est toujours positif
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self):
        """Retourne le numérateur de la fraction."""
        return self.num

    @property
    def denominator(self):
        """Retourne le dénominateur de la fraction."""
        return self.den

    def __str__(self):
        """Retourne une représentation textuelle de la fraction."""
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def as_mixed_number(self):
        """
        Retourne la représentation de la fraction en nombre mixte.

        RETOUR :
            str : La représentation en nombre mixte de la fraction.
        """
        if self.num % self.den == 0:
            return str(self.num // self.den)
        entier = self.num // self.den
        reste = abs(self.num % self.den)
        if entier == 0:
            return f"{reste}/{self.den}"
        return f"{entier} {reste}/{self.den}" if self.num > 0 else f"{entier} {reste}/{self.den}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Additionne deux fractions.

        PRÉCONDITION :
            other est une instance de Fraction.
        RETOUR :
            Fraction : La somme des deux fractions.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Soustrait deux fractions.

        PRÉCONDITION :
            other est une instance de Fraction.
        RETOUR :
            Fraction : La différence entre les deux fractions.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Multiplie deux fractions.

        PRÉCONDITION :
            other est une instance de Fraction.
        RETOUR :
            Fraction : Le produit des deux fractions.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Divise deux fractions.

        PRÉCONDITION :
            other est une instance de Fraction et other.num != 0.
        RETOUR :
            Fraction : Le quotient des deux fractions.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        if other.num == 0:
            raise ZeroDivisionError("Division par une fraction avec numérateur nul impossible.")
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __eq__(self, other: "Fraction") -> bool:
        """
        Vérifie l'égalité de deux fractions.

        PRÉCONDITION :
            other est une instance de Fraction.
        RETOUR :
            bool : True si les fractions sont égales, False sinon.
        """
        return self.num == other.num and self.den == other.den

    def __float__(self):
        """Convertit la fraction en une valeur décimale."""
        return self.num / self.den

    def is_zero(self):
        """Vérifie si la fraction est égale à zéro."""
        return self.num == 0

    def is_integer(self):
        """Vérifie si la fraction est un entier."""
        return self.num % self.den == 0

    def is_proper(self):
        """Vérifie si la fraction est propre (valeur absolue < 1)."""
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Vérifie si la fraction est une fraction unitaire (numérateur = 1)."""
        return abs(self.num) == 1

    def is_adjacent_to(self, other):
        """
        Vérifie si la fraction est adjacente à une autre fraction.

        ARGUMENTS :
            other (Fraction) : La fraction à comparer.

        RETOUR :
            bool : True si les fractions sont adjacentes, False sinon.
        """
        return abs(self.num * other.den - other.num * self.den) == 1
