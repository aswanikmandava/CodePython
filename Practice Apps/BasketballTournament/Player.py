class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def populate_players(player_data, team_id):
        # structure of the input data is a list of 2-item lists
        players = list()
        for player in player_data:
            t_id = int(player[0])
            if team_id == t_id:
                p = Player(player[1], player[2])
                players.append(p)
        return players
    
    def print_player(self):
        print(f"Player Name: {self.get_name()}, Player Number: {self.get_number()}")