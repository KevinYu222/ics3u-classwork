import math
# 81
def hypotenuse (a:int, b:int):
    return round(math.sqrt(a*a + b*b), 2)
try:
    a = int(input("Enter length a: "))
    b = int(input("Enter length b: "))
    print(f"{hypotenuse(a, b)} cm")
except ValueError:
    print("Invalid, Please enter a number")
    print()

# 82
base_fare = 4
mileage = 0.25
def total_fare (distance: int):
    return (((distance-(distance%130))/130) * 0.25) + base_fare
distance = int(input("Enter mileage: "))
print(f"{total_fare(distance)}")

# 83
def total_shipping_charge (number_of_items: int):
    return round((10.95 + ((number_of_items - 1) * 2.95)), 2)

number_of_items = int(input("Enter the number of items: "))
print(f"Shiping Charge: ${total_shipping_charge(number_of_items)}")
