x1, x2, x3, x4 = 42, 4, 2, -2
try:
    y = x1/(x2+x3*x4)
except ZeroDivisionError:
    y = "Division by 0 is impossible"
print("Result of 42/(4+2*(-2)) = ", y)