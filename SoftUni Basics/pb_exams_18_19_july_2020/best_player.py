command = input()
goals = int(input())

best_player = ""
goals_scored = 0
hattrick = False

while True:

    if command == "END":
        break

    if goals > 9:
        best_player = command
        goals_scored = goals
        hattrick = True
        break

    if goals > goals_scored:
        best_player = command
        goals_scored = goals

    if goals_scored >= 3:
        hattrick = True

    command = input()
    if command == "END":
        break
    goals = int(input())


print(f"{best_player} is the best player!")

if hattrick:
    print(f"He has scored {goals_scored} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_scored} goals.")






