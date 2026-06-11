# General Knowledge Quiz Game

score = 0

print("Welcome to the General Knowledge Quiz!")
print("--------------------------------------")

# Question 1
answer1 = input("1. What is the capital of France? ")

if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer2 = input("2. Which planet is known as the Red Planet? ")

if answer2.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer3 = input("3. How many days are there in a week? ")

if answer3 == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final Score
print("--------------------------------------")
print("Quiz Finished!")
print("Your final score is:", score, "/ 3")