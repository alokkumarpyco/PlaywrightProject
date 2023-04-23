"""
Please complete the following assignment in the object-oriented language of your choice
(C#/Java/Python/...)
1 Dollar = 130.90 Yen
Write a class CurrencyConverter that contains the following methods:
• double YenToDollar(double yen, double dollar)
• double DollarToYen(double yen, double dollar)
Use a testing framework (e.g. NUnit/JUnit) to write an extensive test suite for this class.
Please submit your answer as code snippets on Github gists.
Sample:
YenToDollar(10,100) = return (10*(1/130.9) + 100) = 100.076
DollarToYen(10,100) = return (10 + (100*130.9)) = 13100
"""

class CurrencyConverter:
    def __init__(self, yenVal, dolVal, currentYenValue=130.9):
        self.yenVal = round(yenVal,2)
        self.dolVal = round(dolVal,2)
        self.currentYenValue = currentYenValue

    def YenToDollar(self):
        
        return round((self.dolVal*(1/self.currentYenValue) + self.dolVal), 2)

    def DollarToYen(self):

        return round((self.dolVal + (self.dolVal * self.currentYenValue)), 2)







