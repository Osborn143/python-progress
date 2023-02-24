#Drawing a shape with print statement
'''print("/ |")
print("  /  |")
print(" /   |")
print("/____|")'''

#variable and data types
'''character_name = "John"
character_food = "yam"
print("There once was a man named "+ character_name + ",")
print("he was the youngest amongst everyone.")
print("He loved egg, ")
print("but didn't like fish.")'''

#Working with strings
'''print("I am a Boy.")
#creating a new line
print("I love beans and eba \nbut no joy in the streets")
#Conactenation and creating string variables
name = "Osborn"
print(name + " Is Smart.")
#using functions
print(name.lower())
print(name.upper())
print(len(name))
print(name.index("b"))
print(name[5])
print(name.replace("Osb","Pep"))'''

#Working with numbers
'''num = 5
num2 = 5 * 6
num3 = 8 + 2
print("The numbers are ", num, num2, num3)'''

#Getting inputs from user
'''name = input("Enter name: ")
age = input("Enter Your Age: ")
print("Your name is ", name)
print("Hello " + name + "!" + " You Are " + age)
'''
# Building a basic Calculator
'''build a basic calculator that adds two numbers'''
'''num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
sum = float(num1+num2)
print(sum)'''
#Mad libs game
'''color_of_rose = str(input("Enter color of rose: "))
color_of_violet = str(input("Enter color if violet:  "))
noun = str(input("Enter noun: "))
person = str(input("Enter name of person: "))
adjective = str(input("Enter the adjective: "))
noun_2 = str(input("Enter noun two: "))
adjective_2 = str(input("Enter Adjective 2: "))
food = str(input("Enter name of food: "))
adjective_3 = str(input("Enter adjective 3: "))
adjective_4 = str(input("Enter adjective 4: "))
noun_3 = str(input("Enter Third noun: "))
person_2 = str(input("Enter name: "))

print("Roses are " + color_of_rose + "," + "Violets are " + color_of_violet + "." + "It's Valentine's Day and my heart is filled with " + noun + ". \n" + "At school, we are passing out Valentine's Day cards. I made a special one for " + person + "this year. I want them to know how "+ adjective + "they are to me and how much I love their " + noun_2 )'''
#Lists 
'''food = ["Yam", " Ewah", "Garri", "Dodo", "Corn", "Abgado"]
numbers = [9, 3, 12, 21, 44, 54]
numbers.extend(food)
numbers.append("no Obi")
food.insert(5,"meat")
food.remove("Abgado")
food.pop()
food.insert(2,"meat")
food.insert(5,"Yam")
#food.sort()
print(food[2:4])
print(numbers)
print(food)
print(food.sort())'''
#turples
'''coordinates = [(5,4),(78,6),(34,55),(23,8)]
print(coordinates[0])'''
#functions
'''def sayhi():
    print("Hi User")
sayhi()'''
'''def biography(name, age, school, state,):
    print("My name Is "+ name + ", " + "I am " + age + " years old" + " I attend " + school + " and I am from " + state + " state.")
biography("Okon Ginle", "30", "Uniport", "Rivers")'''
#return statement
'''def calculator(num1,num2):
    return num1 + num2
result = calculator(4,6)
print(result)'''
#Conditional Statement
'''gender = str(input("Are you Male Or Female? Yes or No \n"))
if gender == "Yes":
    print("I am a male")
elif gender == "No":
    print("I am a female")'''

'''gender = bool(input("Are you a Male or a Female? Yes or No\n"))
height = bool(input("Are you Tall or Short? Yes or No\n"))
if (gender == True) and (height == True):
    print("You are a Male and You are Tall!")
elif (gender == False) and (height == False):
    print("You are a Female and you are Short!")
elif (gender == True) and (height == False):
    print("You are a Male and You are Short!")
elif (gender == False) and (height == True):
    print("You are a Female and You are Tall!")
'''
'''is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a Male and you are Tall!")
elif is_male and not(is_tall):
    print("You are a short Male!")
elif not(is_male) and is_tall:
    print("She is a Tall Girl!")
else:
    print("You are neither male nor Tall")'''
#conditional statements and comparison
'''def maxnum(num1, num2, num3):
    if num1 >= (num2 and num3):
        return num1
    elif num2 >= (num1 and num3):
        return num2
    else:
        return num3
print(maxnum(7,4,9))'''
#building a better calculator
'''num1 = float(input("Enter First numer: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter operator! ")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Invalid Operator Used!")
'''
#Dictionaries
'''monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions.get("Dec"))'''