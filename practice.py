'''

num1 = float(input("Enter first number:"))
op = input("Enter operator:")
num2 = float(input("Enter second number:"))

if op == "+":
    print(num1+num2)
elif op == "*":
    print(num1*num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Operator")
'''
'''
monthconversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(monthconversions.get("Feb"))
'''
'''
#While loop concept

i = 1
while i <= 10:
    print(i)
    i += 1


for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim","Karen","Oscar"]
for friend in friends:
    print(friend)
'''
'''
#Exponent function =

print(2**3)

def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4,3))

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[1])

#Nested for loop=
for row in number_grid:
    for col in row:
        print(col)
'''
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phase: ")))

#TRY EXCEPT =

try:
    number = int(input("Enter a number : "))
    print(number)
except:
    print("Invalid Input")
'''

