import math

class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def getdata(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))

    def show(self):
        common_factor = math.gcd(self.numerator, self.denominator)
        simplified_numerator = self.numerator // common_factor
        simplified_denominator = self.denominator // common_factor
        print(f"Simplified Fraction: {simplified_numerator}/{simplified_denominator}")

# Example usage:
fraction = Fraction()
fraction.getdata()
fraction.show()
