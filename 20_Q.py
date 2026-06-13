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

possible_answers = [cat, dog]
possible_questions = list (cat.keys())
possible_questions.pop(0)   #removes the name of the dictionary so only keys to boolean values remain
game_is_going = True
count = 0
response = ""
answer: bool = True


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
    response = ""
    count += 1

    for i in range(len(possible_answers)):
        print(possible_answers[i]["name"] + " is a possible answer")
    