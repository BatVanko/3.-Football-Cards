team_A = list(range(1, 12))
team_B = list(range(1, 12))

actions = input().split(" ")
for action in actions:
    team, card = action.split("-")
    if team == "A" and int(card) in team_A:
        team_A.remove(int(card))
    elif team == "B" and int(card) in team_B:
        team_B.remove(int(card))
    if len(team_A) < 7 or len(team_B) < 7 :
        break

if len(team_A) < 7 or len(team_B) < 7:
    result = f"Team A - {len(team_A)}; Team B - {len(team_B)} \n Game was terminated"
else:
    result = f"Team A - {len(team_A)}; Team B - {len(team_B)}"

print(result)
