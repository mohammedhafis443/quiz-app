from quiz import Quiz,Question
from user import User


quiz=Quiz()

q1=Question ("what is the capital of india ?",["mumbai","delhi","bihar"],"delhi")
q2=Question ("which is the bigest animal ?",["elephant","tiger","lion"],"elephant")

quiz.add_question(q1)
quiz.add_question(q2)


# get user info and start quiz
name= input("enter your name")
user=User(name)
user.take_quiz(quiz)




