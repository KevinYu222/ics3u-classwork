def make_out_word(out, word):
  outside_1 = out[0:2]
  outside_2 = out[2:4]
  make_out_word = outside_1 + word + outside_2
  return make_out_word

def extra_end(str):
  new_str = str[-2:len(str)]
  extra_end = new_str + new_str + new_str
  return extra_end

def first_two(str):
  first_two = str[0:2]
  return first_two

def first_half(str):
  first_half = str[0:(len(str)/2)]
  return first_half

def without_end(str):
  without_end = str[1:-1]
  return without_end

def left2(str):
  left = str[2:len(str)]
  right = str[0:2]
  left2 = left + right
  return left2

def make_tags(tag, word):
  make_tags = "<" + tag + ">" + word + "</" + tag + ">"
  return make_tags

def combo_string(a, b):
  if len(a) > len(b):
    combo_string = b + a + b
  else:
    combo_string = a + b + a
  return combo_string

def make_abba(a, b):
  make_abba = a + b + b + a
  return make_abba

def non_start(a, b):
  a = a[1:len(a)]
  b = b[1:len(b)]
  non_start = a + b
  return non_start

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

#Exercise38
a = ["January", "March", "May", "July", "August", "October", "December"]
user_month = input("Enter a month: ")
if user_month in a:
  print("It has 31 days.")
elif user_month == "Febuary":
  print("It has 28 or 29 days.")
else:
  print("It has 30 days.")

#Exercise39
decibal = int(input("How loud is it? "))
if decibal > 130:
  print("It is way too loud!")
elif decibal < 40:
  print("Shhh, it's too quiet.")
elif decibal <= 130 and decibal > 106:
  if decibal == 130:
    print("Jackhammer.")
  else:
    print("Between Jackhammer and gas lawnmover.")
elif decibal <= 106 and decibal > 70:
  if decibal == 106:
    print("Gas lawnmover.")
  else:
    print("Between gas lawnmover and alarm clock.")
elif decibal <= 70 and decibal >= 40:
  if decibal == 70:
    print("Alarm clock.")
  elif decibal == 40:
    print("Quiet room.")
  else:
    print("Between the alarm clock and a quiet room.")

#Exercise40
side1 = int(input("Enter the side length: "))
side2 = int(input("Enter the side length: "))
side3 = int(input("Enter the side length: "))
if side1 == side2 and side2 == side3:
  triangle = "equalateral"
elif side1 != side2 and side1 != side3 and side2 != side3:
  triangle = "scalene"
else:
  triangle = "isoceles"
print (f"This is a {triangle} triangle.")

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

# Exercise 45
location = input("Enter position: ").lower()
if location[0] == "a" or location[0] == "c" or location[0] == "e" or  location[0] == "g":
    if int(location[1]) % 2 == 1:
        print("The square is black.")
    else:
        print("The square is white.")
else:
    if int(location[1]) % 2 == 1:
        print("The square is white.")
    else:
         print("The square is black.")

# Exercise 48:
zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare", "Dragon", "Snake", "Horse", "Sheep"]
year = int(input("Enter year: "))
print(f"This the year of {zodiac[year % 12]}.")

# Exercise 57:
year = int(input("Enter year: "))
if year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
