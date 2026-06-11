"""Load questions from JSON."""

import json, random

def load_questions(level):
    questions = ""
    file = f"data/level{str(level)}_questions.json"
    print(file)

    with open(file) as json_file:
        questions = json.load(json_file)

    return questions

def random_question(level):
    questions = load_questions(level)

    random_number = random.randint(0, 19)
    return questions[random_number]
