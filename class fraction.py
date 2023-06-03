class fraction:
    def init(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    def simplify(self):
        common_divisor = self.gcd(self.numerator,self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def gcd(self,a,b):
        while b != 0:
            a,b = b,a % b
            return a
        
    def subtract(self,other_fraction):
        new_numerator= (self.numerator*other_fraction.denominator)-(other_fraction.numerator*self.denominator)
        new_denominator = self.denominator * other_fraction.denominator
        result = fraction(new_numerator,new_denominator)
        result.simplify()
        return result
    def divide(self,other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        result = fraction(new_numerator,new_denominator)
        result.simplify()
        return result
    
class fractionCalculator:
    def init(self):
        self.fraction1 = None
        self.fraction2 = None

    def get_fraction(self):
        numerator1 = int(input("Enter the numerator of the first fraction:"))
        denominator1 = int(input("Enter the denominator of the first fraction:"))
        numerator2 = int(input("Enter the numerator of the second fraction:"))
        denominator2 = int(input("Enter the denominator of the second fraction:"))
        self.fraction1 = fraction(numerator1,denominator1)
        self.fraction2 = fraction(numerator2,denominator2)

    def subtract_fraction(self):
        result = self.fraction1.subtract(self.fraction2)
        print("subtraction result:" , result.numerator,"/", result.denominator)
    def divide_fractions(self):
        result = self.fraction1.divide(self.fraction2)
        print("Division result:",result.numerator,"/",result.denominator)

#Usage Example
calculator = fractionCalculator()
calculator.get_fraction()
calculator.subtract_fraction()
calculator.divide_fractions()