# second way of importing
from calculator import add
# First way of importing
import calculator
# Third way of importing
from calculator import *
# Creating Alias
import calculator as cal

print(calculator.add(4, 2))
print(calculator.sub(4, 2))
print(calculator.multiply(4, 2))
print(calculator.divide(4, 2))
print(cal.sub(3, 2))
print(add(2, 5))
