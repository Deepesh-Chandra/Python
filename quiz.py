def quiz_function(name):
    questions_list = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "a": "func",
            "b": "define",
            "c": "def",
            "d": "function"
        },
        "correct_answer": "c"
    },
    {
        "question": "Which data type is used to store a collection of key-value pairs?",
        "options": {
            "a": "List",
            "b": "Tuple",
            "c": "Set",
            "d": "Dictionary"
        },
        "correct_answer": "d"
    },
    {
        "question": "What does len() return?",
        "options": {
            "a": "The last item of a collection",
            "b": "The number of items in a collection",
            "c": "The data type of a variable",
            "d": "The largest item in a collection"
        },
        "correct_answer": "b"
    },
    {
        "question": "Which symbol is used to write a comment in Python?",
        "options": {
            "a": "//",
            "b": "<!--",
            "c": "#",
            "d": "/*"
        },
        "correct_answer": "c"
    },
    {
        "question": "Which loop is commonly used to iterate through every item in a list?",
        "options": {
            "a": "repeat",
            "b": "for",
            "c": "loop",
            "d": "iterate"
        },
        "correct_answer": "b"
    }
]

    marks = 0;
    for index, data in enumerate(questions_list):
        print(f"Question {index+1}: {data['question']}")

        print('Options: Respond with (a, b, c or d) only')
        for key, value in data['options'].items():
            print(f"{key}: {value}")

        user_input = input("Your answer:").lower()

        if(user_input==data['correct_answer']):
            marks +=2;

    print(f"{name} your marks are {marks}/10")


def quiz_start_function(usersays, name):
    if(usersays == 'Yes'):
        quiz_function(name)
    else:
        return

user_name = input('What is your name: ')
quizstart_not = input("Do you want to start the quiz?(Yes/No)")
quiz_start_function(quizstart_not, user_name)

