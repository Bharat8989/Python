class Cricket:

    data = [
        {"id": 1, "name": "Virat Kohli", "iplteam": "RCB", "run": 8450, "match": 260, "strikerate": 131.5},
        {"id": 2, "name": "Rajat Patidar", "iplteam": "RCB", "run": 1120, "match": 40, "strikerate": 142.3},
        {"id": 3, "name": "Glenn Maxwell", "iplteam": "RCB", "run": 2950, "match": 130, "strikerate": 155.8},
        {"id": 4, "name": "Mohammed Siraj", "iplteam": "RCB", "run": 110, "match": 95, "strikerate": 85.4},
        {"id": 5, "name": "Dinesh Karthik", "iplteam": "RCB", "run": 4840, "match": 250, "strikerate": 135.2},
        
        {"id": 6, "name": "Rohit Sharma", "iplteam": "MI", "run": 9620, "match": 255, "strikerate": 141.2},
        {"id": 7, "name": "Suryakumar Yadav", "iplteam": "MI", "run": 3650, "match": 145, "strikerate": 143.6},
        {"id": 8, "name": "Ishan Kishan", "iplteam": "MI", "run": 2640, "match": 105, "strikerate": 134.8},
        {"id": 9, "name": "Hardik Pandya", "iplteam": "MI", "run": 2520, "match": 135, "strikerate": 144.5},
        {"id": 10, "name": "Jasprit Bumrah", "iplteam": "MI", "run": 75, "match": 130, "strikerate": 92.1},
        
        {"id": 11, "name": "MS Dhoni", "iplteam": "CSK", "run": 5250, "match": 262, "strikerate": 136.4},
        {"id": 12, "name": "Ruturaj Gaikwad", "iplteam": "CSK", "run": 2420, "match": 65, "strikerate": 137.9},
        {"id": 13, "name": "Ravindra Jadeja", "iplteam": "CSK", "run": 2900, "match": 240, "strikerate": 129.2},
        {"id": 14, "name": "Shivam Dube", "iplteam": "CSK", "run": 1580, "match": 60, "strikerate": 141.4},
        {"id": 15, "name": "Matheesha Pathirana", "iplteam": "CSK", "run": 10, "match": 25, "strikerate": 65.0},
        
        {"id": 16, "name": "Shubman Gill", "iplteam": "GT", "run": 3210, "match": 100, "strikerate": 135.1},
        {"id": 17, "name": "Sai Sudharsan", "iplteam": "GT", "run": 1050, "match": 30, "strikerate": 139.2},
        {"id": 18, "name": "Rashid Khan", "iplteam": "GT", "run": 550, "match": 120, "strikerate": 138.4},
        {"id": 19, "name": "Rahul Tewatia", "iplteam": "GT", "run": 980, "match": 90, "strikerate": 132.6},
        {"id": 20, "name": "David Miller", "iplteam": "GT", "run": 2850, "match": 132, "strikerate": 137.8},
        
        {"id": 21, "name": "Shreyas Iyer", "iplteam": "KKR", "run": 3250, "match": 115, "strikerate": 124.6},
        {"id": 22, "name": "Rinku Singh", "iplteam": "KKR", "run": 950, "match": 45, "strikerate": 144.2},
        {"id": 23, "name": "Andre Russell", "iplteam": "KKR", "run": 2480, "match": 125, "strikerate": 174.0},
        {"id": 24, "name": "Sunil Narine", "iplteam": "KKR", "run": 1520, "match": 175, "strikerate": 165.5},
        {"id": 25, "name": "Nitish Rana", "iplteam": "KKR", "run": 2650, "match": 110, "strikerate": 131.0},
        
        {"id": 26, "name": "Sanju Samson", "iplteam": "RR", "run": 4450, "match": 165, "strikerate": 138.5},
        {"id": 27, "name": "Yashasvi Jaiswal", "iplteam": "RR", "run": 1650, "match": 50, "strikerate": 148.0},
        {"id": 28, "name": "Jos Buttler", "iplteam": "RR", "run": 3600, "match": 110, "strikerate": 146.2},
        {"id": 29, "name": "Riyan Parag", "iplteam": "RR", "run": 1180, "match": 65, "strikerate": 135.4},
        {"id": 30, "name": "Yuzvendra Chahal", "iplteam": "RR", "run": 50, "match": 160, "strikerate": 70.2}
    ]
    
    # CRUD operations
    
    # create operation add new player

    def __init__(self, id, name, iplteam, run, match, strikerate):
        self.id = id
        self.name = name
        self.iplteam = iplteam
        self.run = run
        self.match = match
        self.strikerate = strikerate

        new_player = {
            "id": id,
            "name": name,
            "iplteam": iplteam,
            "run": run,
            "match": match,
            "strikerate": strikerate
        }
        Cricket.data.append(new_player)
        
    
    #Read operations     
         
    def display(self):
        for player in Cricket.data:
            # print(player)
            print(f"ID:{player['id']}, name:{player['name']} , IPLTeam:{player['iplteam']}")
            print("----------------------------------------")
    
    # read operation using the id 
    
    def read_player(self, player_id):
        print(f"\n--- Searching Player with ID: {player_id} ---")
        for player in Cricket.data:
            if player['id'] == player_id:
                print(f"name: {player['name']} | team: {player['iplteam']} | runs: {player['run']}")
                return
        print("not found the id ")
    #  Update operations 

    def update_player(self,player_id,new_runs,new_matches):
        for player in Cricket.data:
            if player['id']==player_id:
                player['run'] = new_runs
                player['match'] = new_matches
                print(f'player add successfully:{player['name']}')
                return
        print('not found the id ')
      
    #   Delete operations 
    def delete_player(self, player_id):
        for player in Cricket.data:
            if player['id'] == player_id:
                Cricket.data.remove(player)
                print(f"\n Delete player ID {player_id} ")
                return
        print('not found the id ')
                     
      # current player list       
            
    def display_all(self):
        print("current player list ")
        for player in Cricket.data:
            print(f"ID: {player['id']} | Name: {player['name']} | Runs: {player['run']}")
    
    def filter_by_team(self,team_name):
            print(" player from team :",{team_name})
            for player in Cricket.data:
                if player['iplteam']==team_name:
                    print(f"Name: {player['name']}, Runs: {player['run']}, SR: {player['strikerate']}")
            print("----------------------------------------")
            
    def highest_runs(self):
        print("\n=== run score ===")
        max_player = Cricket.data[0]
        for player in Cricket.data:
            if player['run'] > max_player['run']:
                max_player = player
            print(f"Player: {max_player['name']} | Team: {max_player['iplteam']} | Total Runs: {max_player['run']}")
            print("----------------------------------------")
            
    
    
        
obj=Cricket(31,'Bharat Kadam','MI',2344,34,123)
obj.display()
obj.update_player(31,5000,100)
obj.read_player(31)

obj.delete_player(31)

obj.display_all()

# obj.update_player(31,5000,100)

# obj.filter_by_team("MI")
# obj.highest_runs()
