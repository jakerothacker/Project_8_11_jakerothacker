cat: dict[str,any] = {
    "name": "cat",
    "Is it physical?": True,
    "Is it an animal?": True,
    "Does it have four legs?": True,
    "Is it a plant?": False,
    "Is it a canine?": False,
    "Is it a feline?": True,
    "Can it be brown?": True
}
dog: dict[str,any] = {
    "name": "dog",
    "Is it physical?": True,
    "Is it an animal?": True,
    "Does it have four legs?": True,
    "Is it a plant?": False,
    "Is it a canine?": True,
    "Is it a feline?": False,
    "Can it be brown?": True
}

possible_answers = [cat, dog] # List of answers as dictionaries so info is stored
possible_questions = list (cat.keys())
possible_questions.pop(0)   # Removes the name of the dictionary so only keys to boolean values remain
game_is_going = False
# Player picks an solution 
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


while game_is_going:


  # Player responds to the question
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


# Remove answers that don't match the current question
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

# For when one possible answer remains
    if len(possible_answers) == 1:
        print("The answer is: " + possible_answers[0]["name"])
        game_is_going = False 