import requests
import json
import pprint
import random
import html

url = "https://opentdb.com/api.php?amount=1"
endgame = ""

while endgame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endgame = input("Sorry, there was a problem retriving the question. Press enter to try again or type 'quit' to quit the game: ")
    else:
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " +html.unescape(answer))
            answer_number += 1

        user_answer = input("\nType the number of the correct answer: ")

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulations! You answered correctly! The correct answer was: " + html.unescape(correct_answer))
        else:
            print("Sorry, " + html.unescape(user_answer) + " is the incorrect. The correct answer is: " + html.unescape(correct_answer))

        endgame = input("\nPress enter to play again or press 'quit' to quit the game.").lower()

print("\nThanks for playing.")