from s28 import Question
question_prompts = [
    "What colors are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colors are bananas?\n(a) Teal\n(b) Magenta|n(c) Yellow\n\n",
    "What colors are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]
def run_test(question):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)