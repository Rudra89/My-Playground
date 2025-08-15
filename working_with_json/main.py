import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for index, question in enumerate(data):
    print(f"Question {index + 1} - {question['question_text']}")
    for i, option in enumerate(question["options"]):
        print(f"Option {i + 1} - {option}")
    user_choice = int(input("Enter the choice: "))
    question['user_choice'] = user_choice
    if user_choice == question['correct_answer']:
        score += 1

print(f"Your score is {score}/{len(data)}")