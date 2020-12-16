from typing import List, Any

def main():
    location = ["giant box", "box 1", "box 2", "box 3", "plane", "boss battle"]
    inventory = [["Teddy bear", "Nerf gun", "Wineglasses", "Big blanket", 
    "Racecar", "20-volt battery", "Bag of fortune cookies"], # Red Box
    ["Roll of wire", "Chain and lock", "Camping rain tarp","Picnic basket", "Batman lego set","Baseball bat","Key ring with 5 keys","String"], #Blue
    ["Box of razor blades", "Steel pipes", "Acrylic paints", "Zipline harness", "Sony Noise-Cancelling headphones", "Tranquilizer darts",
    "Spider-man Comic Book"], # Green Box
    [] # your inventory
    ] 

    print("You are an amazon employee. Due to the inhumane work conditions and low pay, you decide to unionize; unfortunately, Jeff Bezos knows all. He trapped you in his room of sadness, a giant cardboard box filled with all sorts of Christmas gifts for the season being flown in a giant delivery drone. You must escape, for the sake of your freedom, and fair labor practices.")
    print()
    current_location = location[0]
    if current_location == "giant box":
        giant_box(location, inventory)
    

def giant_box(location: List[str], inventory: List[str]):
    print("You are inside a giant box.")
    print("There is a door with 2 lock. A noraml key lock and a pasword lock, or maybe you can find some other ways to crack your way through...")
    print("There are 3 boxes in front of you")
    print("[1] Red box")
    print("[2] Blue box")
    print("[3] Green Box")
    choice = int(input("Choice >>> "))
    print()

    if choice == 1:
        red_box(location, inventory)
   

def red_box(location: List[str], inventory: List[Any]):
    print("You are the red box")
    while True:
        print(f"Items you have: {inventory[3]}")
        print(f"Items in the box:")
        for i in range(len(inventory[0])):
            print(f"[{i + 1}] {inventory[0][i]}")
        print("[b]ack")
        choice = (input("Choice >>> "))
        if choice == "b":
            return
        else:
            inventory[3].append(inventory[0][int(choice) - 1])
            inventory[0].remove(inventory[0][int(choice) - 1])
        print()

def blue_box():
    pass

def green_box():
    pass

def plane():
    pass

def boss_fight():
    pass

def inventory():
    pass

if __name__ == "__main__":
    main()
