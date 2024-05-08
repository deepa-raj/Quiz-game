# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
#
# while quiz.still_has_question():
#     quiz.next_question()
#
# print("You have completed the quiz!")
# print(f"Your final score is: {quiz.score}/{quiz.question_number} ")
#
#
# # print(question_bank)
#
#
#
#
# # question_bank = []
# # for question in question_data:
# #     question_text = question["text"]
# #     question_answer = question["answer"]
# #     new_question = Question(q_text=question_text, q_answer=question_answer)
# #     question_bank.append(new_question)
#







# TODO: PRACTICE PROBLEM ON MY OWN
# -----------------------------------------------------------------------------------------------------------------------------






# TODO: 1. Get question bank -----> main
# TODO: 2. save question with their answer -----> Main
# TODO: 3. check if your guess is equal to the answer either True or False -----> quiz brain
# TODO: 4. If your answer is correct increase the score -----> quizz brain
# TODO: 5. Keep on asking qns until you reach to the end -----> quiz brain




from question_model import Questions
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was {quiz.score} /{quiz.question_number}")

