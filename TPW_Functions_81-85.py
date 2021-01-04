import math
# 81
error = True
def hypotenuse (a:int, b:int):
    return round(math.sqrt(a*a + b*b), 2)
while error == True:
    try:
        a = int(input("Enter length a: "))
        b = int(input("Enter length b: "))
        print(f"{hypotenuse(a, b)} cm")
        exit = input("Press ENTER to continue or X to exit >>> ").lower()
        if exit == "x":
            error = False
        print()
    except ValueError:
        print("Invalid, Please enter a number")
        print()

# 82
base_fare = 4
mileage = 0.25
def total_fare (distance: int):
    return (((distance-(distance%140))/140) * 0.25) + base_fare
distance = int(input("Enter mileage: ")) * 1000
print(f"{total_fare(distance)}")

# 83
def total_shipping_charge (number_of_items: int):
    return round((10.95 + ((number_of_items - 1) * 2.95)), 2)

number_of_items = int(input("Enter the number of items: "))
print(f"Shiping Charge: ${total_shipping_charge(number_of_items)}")

# 84
def find_median (a:int, b:int, c:int):
    number_list = [a, b, c]
    number_list.remove(max(number_list))
    return max(number_list) 
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print(f"Median: {find_median(a, b, c)}")
