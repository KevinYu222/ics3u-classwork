def main():
    string = input("Please Enter a String: ")
    while True:
        try:
            width = int(input("Please Enter Length of the Width: "))
            if width < len(string):
                raise ValueError
            break
        except ValueError:
            print("Invalid, Please Enter a number.")
    print(center_string(string, width))

def center_string(string: str, width: int):
    spaces = round((width - len(string))/2)
    output = ""
    for i in range(spaces):
        output += " "
    return output + string

def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    print("all passed!")


if __name__ == "__main__":
    tests()
