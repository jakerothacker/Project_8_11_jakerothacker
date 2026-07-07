"""
20_Questions
Jake Rothacker
This file contains a proof of concept for a 20 questions game that can be expended.
6-26-2026
"""
import random
#replace dictionaries with inheriting classes to store attributes
cat: dict[str,any] = {
    "name": "cat",
    "Is it an animal?": True,
    "Does it have four legs?": True,
    "Is it a plant?": False,
    "Is it a canine?": False,
    "Is it a feline?": True,
    "Can it be brown?": True,
    "Is it round?": False,
    "Is it an animal?": True,
    "Is it red?": False,
    "Is it orange?": False,
    "Is it green?": False,
}
dog: dict[str,any] = {
    "name": "dog",
    "Is it an animal?": True,
    "Does it have four legs?": True,
    "Is it a plant?": False,
    "Is it a canine?": True,
    "Is it a feline?": False,
    "Can it be brown?": True,
    "Is it round?": False,
    "Is it an animal?": True,
    "Is it red?": False,
    "Is it orange?": False,
    "Is it green?": False,
}
apple: dict[str,any] = {
    "name": "apple",
    "Is it an animal?": False,
    "Does it have four legs?": False,
    "Is it a plant?": True,
    "Is it a canine?": False,
    "Is it a feline?": False,
    "Can it be brown?": False,
    "Is it round?": True,
    "Is it an animal?": False,
    "Is it red?": True,
    "Is it orange?": False,
    "Is it green?": False,
}
orange: dict[str,any] = {
    "name": "orange",
    "Is it an animal?": False,
    "Does it have four legs?": False,
    "Is it a plant?": True,
    "Is it a canine?": False,
    "Is it a feline?": False,
    "Can it be brown?": False,
    "Is it round?": True,
    "Is it an animal?": False,
    "Is it red?": False,
    "Is it orange?": True,
    "Is it green?": False,
}
tree: dict[str,any] = {
    "name": "tree",
    "Is it an animal?": False,
    "Does it have four legs?": False,
    "Is it a plant?": True,
    "Is it a canine?": False,
    "Is it a feline?": False,
    "Can it be brown?": True,
    "Is it round?": False,
    "Is it an animal?": False,
    "Is it red?": False,
    "Is it orange?": False,
    "Is it green?": True,
}

#This block will likely change 
# possible_answers = [cat, dog, apple, orange, tree] 
# possible_questions = list (cat.keys())
# possible_questions.pop(0)   # Removes the name of the dictionary so only keys to boolean values remain
# random.shuffle(possible_questions) 


game_is_going = False
#This game setup will become a function
print("Let's play 20 questions!")
while game_is_going == False:
    solution = input("What are you thinking of? ")
    for answer in possible_answers:
        if answer["name"] == solution:
            current_answer = answer
            game_is_going = True
            break
        elif solution == "Help":
            current_answer = "Help"
            for answer in possible_answers:
                print(answer["name"])
            break
        else:
            current_answer = "None"
    if current_answer == "None":
        print("Sorry, I don't know what you're thinking of. Type 'Help' for possible answers.")
        

count = 0
response = ""
answer: bool = True

#The running of the game will be a function
while game_is_going:

    while response != "T" and response != "F":
        response = input("T or F: " + possible_questions[count])
        if response == "T":
            answer = True
        elif response == "F":
            answer = False
        elif response == "Quit":
            game_is_going = False
            break
        else:
            print("Invalid input: Please enter T or F")


    l = len(possible_answers)
    i=0
    while i<l: 
        if possible_answers[i][possible_questions[count]] != answer:
            possible_answers.pop(i)
            i -= 1
        i += 1
        l = len(possible_answers)
    
    
    # Gets ready for the next question
    response = ""
    count += 1


    if len(possible_answers) == 1:
        print("The answer is: " + possible_answers[0]["name"])
        game_is_going = False 
    elif len(possible_answers) == 0:
        print("You stumped me. I don't know what you're thinking of. Please try again.")
        game_is_going = False