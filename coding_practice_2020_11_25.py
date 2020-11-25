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
        
