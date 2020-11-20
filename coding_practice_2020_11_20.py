color = input("What is your favourite color? ")
print(f"Wow! {color}?! That is also my favourite color!")

can = int(input("How many cans are in a pack? "))
pack = int(input("How many packs are there? "))
print(f"You have total of {can * pack} cans.")

length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
print(f"Volume: {length * width * height}")

user = input("Did you just join a Google Meet and mute the teacher? ")
if user == "Yes" or user == "yes":
    print("That's probably not a good idea.")
elif user == "No" or user == "no":
    print("Ok. Good.")
