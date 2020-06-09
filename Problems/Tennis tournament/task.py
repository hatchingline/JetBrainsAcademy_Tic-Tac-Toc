num_match = int(input())
statics = [input().split() for count in range(num_match)]
list_player = [player[0] for player in statics if player[1] == "win"]
print(f"{list_player}\n{len(list_player)}")
