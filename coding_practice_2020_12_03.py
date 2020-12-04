# 1
def add_3(a: int, b: int, c: int) -> int:
    return a + b + c
# 2
def info(name: str, age: int) -> str:
    return f"{name} is {age} years old."

# 3
def average(a: int, b: int) -> int:
    return (a + b)/2

# 4
def biggest(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c
    else:
        if a == b and b == c:
            return a, b, c
        elif a == c and a > b:
            return a, c
        elif a == b and a > c:
            return a, b
        else:
            return b,c

# 5
def first_two(word: str) -> str:
    return(word[:2])

sum = add_3(4, 16, 27)
print(sum)

name_age = info("Kevin", 16)
print(name_age)

result = average(672, 32657)
print(result)

largest = biggest(4, 2, 4)
print(largest)

two_letter = first_two("dinosaur")
print(two_letter)
