import time

print('Hey, there')
money=2000
if money<2000:
    print('need to save more')
elif money>=2000:
    print('buy mac os')
print('   / |')
print('  /  |')
print(' /   |')
print('/____|')
character_age = 145
character_name = 'James'
is_male = True
print(character_name +  ' is a web dev')
print('He loves writing code using the pycharm IDE' + ',' + ' he is' + str(character_age) +' years old' + '.')
print(type(character_name))
print(type(character_age))
phrase = 'Joel'
print(phrase + ' is his brother')
print(phrase.upper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(character_name))
print(phrase[0])
print(character_name.index('s'))
print(character_name.replace('James', 'Allan'))
print(6 % 2)
my_num = 7
print(pow(my_num, 3))
print(abs(character_age))
print(round(character_age))

from math import *

print(floor(character_age))
print(ceil(character_age))
print(sqrt(my_num))
name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hey '  + name)
print('You are ' + age)


num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
result = float(num1) + float(num2)
print(result)

ages = [23, 43, 66, 12, 17, 22, 18]
friends = ["Aaron", "Rita", "Godfrey", "Tyson","Tyson", "Patrick"]
ages2 = [32, 33, 45, 56, 67, 78, 89]
friends[1] = 'John'
print(friends[1:3])

#designing a simple madlibs game

animal =input('Animals name: ')
trait = input("What are its traits: ")
colour = input("What is its colour: ")
character = input("Is it friendly: ")

print("I love the animal, " + animal)
print("Its traits are " + trait)
print("They are usually of the colour " + colour)
print("They are usually very " + character)
friends.append('James')
friends.insert(1, 'oscar')
friends.sort()
ages.reverse()
friends.count("Tyson")
ages2 = ages.copy()
print(ages2)
print(ages)
print(friends)


def sayhi(name, age,):

    sayhi(Peter, 23)
    sayhi(pato, 32)
    print("Hey " + name, + " you are, " + age)

def maxnum(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(maxnum(32, 56, 23))

#Using if, elif, else, while loops and for loops

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("invalid operand")

j = 20
while j < 30:
    print(j)
    j = j+1
print("End of loop")


tall = True
male = True
if tall and male:
    print("You are a tall male")
elif tall and not male:
    print("You are tall but not male")
elif not tall and male:
    print("You are male but not tall")
else:
    print("You are neither male nor tall")

first_name = "James"
last_name = "Chebet"
print("Hello, {} {} hope you are well".format(last_name, first_name))
def sqrt(num):
    return num1*num2

print(sqrt(7))

#Building a translator using if statements and for loops

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "R"
            else:
                translation = translation + "r"
        else:
            translation = translation + letter
    return translation
translate(phrase)

print(translate(input("Enter a phrase: ")))

# Reading, writing and appending files

school_list = open("schools.txt", "r")
school_list.readline()[2]
school_list.close()

# creating data types using classes and objects

from student import student

student1 = student("Alpha", 34, "female", True)
student2 = student("Peter", 21, "male", True)
print(student2.sex)
print(student2.is_over_eighteen())

# building a multiple choice quiz

question_prompts = [
    "What color are apples?\n(a) Blue\n(b) Green\n(c) Orange\n\n",
    "What color are bananas?\n(a) Yellow\n(b) Red\n(c) White\n\n",
    "What color are mangoes?\n(a) Green\n(b) Black\n(c) Magenta\n\n",

]

from Questions import Question

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),

]

def runtest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1

            print("You get " + str(score) + "/" + str(len(questions)) + " questions correct" )

runtest(questions)

#Inheritance in python

from chef import chef
from chinesechef import chinesechef

mychef = chef()
mychinesechef = chinesechef()

mychef.make_chicken()
mychinesechef.make_vegs()

#Building a basic guessing game

secret_word = "Angel"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses, you lose")
else:
    print("Congratulations, You WIN!!!")

# Guess the number using the random module in python

    from random import randint

def computer_number(min_num, max_num):

        return randint(min_num, max_num)

def player_guess(min_num, max_num):
        user_input = int(input(f"Enter a number between {min_num} and {max_num}: "))
        return user_input

def play():
        low = 0
        high = 10
        computer_choice = computer_number(low, high)
        player_choice = player_guess(low, high)

        while player_choice != computer_choice:
            if player_choice > computer_choice:
                player_choice = int(input("Number is too high, please try again: "))
            elif player_choice < computer_choice:
                player_choice = int(input("Number is too low, please try again: "))
        return play()





