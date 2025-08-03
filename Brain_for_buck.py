import random
Questions=[
    {
        "Question":"What is smallest prime number?",
        "Options" : ["A. 0","B. 1","C. 2","D. 5"],
        "Answer" : "C"
    },
    {
        "Question":"Which country is known as the Land of Rising Sun?",
        "Options":["A. China","B. South Korea","C.Thailand" ,"D.Japan"],
        "Answer": "D"
    },
    {
        "Question":"What is chemical symbol of Water?",
        "Options":["A. H2O","B. O2","C.NaCl" ,"D.KHNo3"],
        "Answer": "A"
    },
    {
        "Question":"What is the largest planet in the solar system?",
        "Options":["A. Saturn","B. Jupiter","C.Earth" ,"D.Mars"],
        "Answer": "A"
    },
    {
        "Question":"Independence year of Pakistan?",
        "Options":["A. 1940","B. 1947","C.1969" ,"D.1923"],
        "Answer": "B"
    }, 
    {
        "Question": "How many continents are there in the world?",
        "Options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "Answer": "C"
    },
    {
        "Question": "Which device is used to measure temperature?",
        "Options": ["A. Barometer", "B. Thermometer", "C. Speedometer", "D. Altimeter"],
        "Answer": "B"
    },
    {
        "Question": "What is the capital city of Saudi Arabia?",
        "Options": ["A. Dubai", "B. Mecca", "C. Jeddah", "D. Riyadh"],
        "Answer": "D"
    }
]
def game():
       selected_questions=random.sample(Questions,5)
       score=0
       for i, q in enumerate(selected_questions):
             print(f"Qno{i+1}:{q['Question']}")
             for opt in q['Options']:
                   print(opt)
             user_answer=input("Select option from (A,B,C,D): ").strip().upper()     
             if user_answer==q['Answer']:
                   print("Correct Answer")
                   score+=1
             else:
                  print("Wrong Answer.""Game Over")
                  break
       if score == 5:
        print("🎉 Congratulations! You won 1 Million Rupees!")
       else:
        print(f"Your score is {score}.Better luck next time!")

print("Welcome to the games of Millioniares!")
print("Choose the correct option to win 1 Million Rupees!")
user_input=input("Press enter to start game!")
if user_input== "":
    game()