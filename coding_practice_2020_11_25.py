# Exercise 35
while True:
    try:
        human_years = int(input("Enter human years: "))
        if human_years < 0:
            print("Error")
        elif human_years <= 2:
            print(f"{human_years * 10.5} dog years old.")
            break
        else:
            print(f"{21 + ((human_years - 2)* 4)} dog years old.")
            break
    except ValueError:
        print("You're suppose to enter a number.")

# Exercise 44
print("Check for fixed Holiday")
while True:
    month = input("Month: ").lower
    day = int(input("Day: "))

    if month == "january" and day == 1:
        print("It's New Year's Day")
        break
    elif month == "july" and day == 1:
        print("It's Canada's Day")
        break
    elif month == "december" and day == 25:
        print("It's Christmas Day")
        break
    else:
        print("There is no fixed holiday that day.")
        
