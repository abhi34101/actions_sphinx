class Calculator:
    """
    A simple utility class for basic arithmetic operations.

    This class demonstrates how to use docstrings that are recognized
    by Sphinx's autodoc extension.
    """

    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers.

        :param a: The first number.
        :param b: The second number.
        :return: The sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts the second number from the first.

        :param a: The first number (minuend).
        :param b: The second number (subtrahend).
        :return: The difference between a and b.
        """
        return a - int(b)

    def multiply(self, a: float, b: float) -> float:
        """
        Multiplies the two input numbers.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        divides the first number with the second number.
        """
        return a / int(b)
