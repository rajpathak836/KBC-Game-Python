questions = [
    ["Which of the following corresponds to ‘ek bataa do’?",
     "(A) Pura", "(B) Sawa", "(C) Adha", "(D) Pauna", 3],

    ["Which of the following gods is also known as ‘Gauri Nandan’?",
     "(A) Agni", "(B) Indra", "(C) Hanuman", "(D) Ganesha", 4],

    ["In the game of ludo the discs or tokens are of how many colours?",
     "(A) One", "(B) Two", "(C) Three", "(D) Four", 4]
]

levels = [1000, 50000, 100000]
money = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    reply = int(input("Enter your answer (1-4) or 0 to quit: "))

    if reply == 0:
        money = levels[i-1] if i > 0 else 0
        break

    if reply == q[5]:
        print("Correct answer!")
        money = levels[i]
    else:
        print("Wrong answer!")
        break

print(f"\nYour take home money is Rs.{money}")
