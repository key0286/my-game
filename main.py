print("hello, welcome to my quiz")

answer = input("Are you ready to play? (yes/no): ")
score = 0
total_q = 6
mark = 0

while mark < 50 and answer.lower().strip() == "yes":

    answer = input("1. how long have i been gaming?")
    if answer.strip() == "30 years":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("2. do i have any kids?")
    if answer.strip() == "yes":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("3. am i married?")
    if answer.lower().strip() == "yes":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("4. what's my favourite game?")
    if answer.lower().strip() == "super mario world" or "minecraft" or "sonic 1" or "sonic":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("5. what star sign am i?")
    if answer.lower().strip() == "scorpio":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("6. Which is my favourite wine red or white?")
    if answer.lower().strip() == "red":
        score += 1
        print("correct")
    else:
        print("incorrect")

    print("thank you for playing you got", score, "questions correct")
    mark = (score / total_q) * 100

    print("mark: ", mark)

    if mark < 50:
        score = 0
        answer = input("would you like to play again? (yes/no)")

print("goodbye")
