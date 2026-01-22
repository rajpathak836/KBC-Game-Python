questions = [
    ["Which of the following corresponds to ‘ek bataa do’? ", '(A) Pura', '(B) Sawa',
     '(C) Adha', '(D) Pauna', 3]
    ["Which of the following gods is also known as ‘Gauri Nandan’?", '(A) Agni', '(B) Indra',
     '(C) Hanuman', ' (D) Ganesha', 3]
    ["In the game of ludo the discs or tokens are of how many colours?", '(A) One', '(B) Two',
     '(C) Three', '(D) Four', 3]
]

levels = [1000, 50000, 100000000, 200000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n question for Rs.{levels[i]}")
    print(f"a.question[1]               b.question[2] ")
    print(f"c.question[3]               d.question[4] ")
    reply = int(input("Enter your answer(1-4) or 0 to quit: \n"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer ,you have won Rs.{levels[i]}")
        if (i == 2):
            money = 50000
        elif (i == 3):
            money = 10000000
        else:
            print("Wrong answer")
print(f"your take home money is {money}")
