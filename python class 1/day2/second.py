#While Loop
'''while condition:
basic syntax of a while loop
'''
'''num = 1
while num <= 10:
    print(num)
    num += 1'''

'''secret_word = "Perpetual"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Guess limit exceeded, YOU LOSE!")
else:
    print("You Win!")'''
'''import random
secret_number = random.randint(0,10)
guess = " "
guess_count = 0
guess_limit = 5
out_of_guesses = False
while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter secret number: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Exceeded Guess Limit, YOU LOOSE!")
else:
    print("You Win!")'''

#For Loops.
'''when you write For you create a different varialbe and say something likee 
for letter in "Giraffe Academy":
    print(letter)'''
'''name = ["Osborn", "Oje", "Perpetual", "Atuogu"] 
for num in range(5,11):
    print(num)'''
'''name = ["Aisha", "Amina", "Bello", "Vanessa", "Victory", "David"]
for names in name:
    if names != "Amina":
        print("It's not the legit name!")
    else:
        print("The name is legit!")'''
#Exponent Function
'''def exponetialfunc(basenum, pownum):
    result = 3
    for soln in range(pownum):
        result = result * basenum
    return result
print(exponetialfunc(2,8))'''
#2 dimensional list and nested loops
'''name_list = [
    ["Oje","Osborn","Anthony"],
    ["Perpetual", "Adaugo","Twinkie"],
    ["Gabzy","Jessie Baby", "Joskidz"],
]
print(name_list[1][2])
for row in name_list:
    for col in row:
        print(col)'''
#Building A BAsic Translator


#All Vowels becomes K

def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "T"
            else:
                translation = translation + "t"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))