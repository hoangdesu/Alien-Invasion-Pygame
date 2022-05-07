import json


with open('./top_players.json', 'r') as file:
    players_list = json.load(file)
    print("Top 5 players now:")
    for i in range(len(players_list)):
        player = players_list[i]
        print(f"{i+1}. Player: {player['name']} - Score: {player['score']}")
    name = input("Enter your name: ")
    score = int(input("Enter your score: "))
    
    inserted = False
    for i in range(len(players_list)):
        # Insert before the current index if the score if greater
        if score > players_list[i]['score']:
            players_list.insert(i, {
                "name": name,
                "score": score
            })
            inserted = True
            break
    
    if not inserted:
        players_list.append({
                "name": name,
                "score": score
            })
            

    print("Top 5 players new:")
    for i in range(len(players_list)):
        player = players_list[i]
        print(f"{i+1}. Player: {player['name']} - Score: {player['score']}")
    
    with open('./top_players.json', 'w') as fileWr:
        json.dump(players_list, fileWr, indent=4)
        fileWr.close()
        
    file.close()
    
    
    