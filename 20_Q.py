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


#game constants that are needed for game_setup and game_main_section go here until I find a better way
possible_answers = []

def game_setup():

    print("Let's play 20 questions!")
    while True:
        response = input("What are you thinking of? ")
        for answer in possible_answers:
            if answer == response:
                return response 
        if response == "Help" or response == "help":
            print(f"The possible answers are {possible_answers}")
        else:
            print("Sorry, I don't know what you're thinking of. Type 'Help' for possible answers.")

        
def game_main_section(solution):

    count = 0
    response = ""
    while True:

        while response != "T" and response != "F":
            response = input("T or F: " + possible_questions[count])#this text will change when the classes are working
            if response == "T":
                answer = True
            elif response == "F":
                answer = False
            elif response == "Quit":
                return print("The game was exited")
            else:
                print("Invalid input: Please enter T or F")


        #this text will change when the classes are working
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
            return 
        elif len(possible_answers) == 0:
            print("You stumped me. I don't know what you're thinking of. Please try again.")
            return


