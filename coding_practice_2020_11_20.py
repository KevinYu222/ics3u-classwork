color = input("What is your favourite color? ")
print(f"Wow! {color}?! That is also my favourite color!")

can_per_pack = int(input("How many cans are in a pack? "))
pack = int(input("How many packs are there? "))
print(f"You have total of {can * pack} cans.")

length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
print(f"Volume: {length * width * height}")

answer = input("Did you just join a Google Meet and mute the teacher? ")
if answer == "Yes" or user == "yes":
    print("That's probably not a good idea.")
elif answer == "No" or user == "no":
    print("Ok. Good.")
