import random


def game():
    count = 0
    random_number = random.randint(1, 100)

    while True:
        count += 1
        guess = int(input("숫자를 입력하세요 : "))
        if guess < random_number:
            print("UP!")
        elif guess > random_number:
            print("DOWN!")
        else:
            print("You win!")
            print(f"You took {count} guesses")
            break

    return count


max_count = 0
while True:
    count = game()
    if count > max_count:
        max_count = count

    again = input("다시 하시겠어요? (y/n) : ")
    if again == "n":
        print(f"가장 많이 시도한 횟수 : {max_count}")
        break