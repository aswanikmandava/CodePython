class Team:
    def __init__(self, name, conference):
        self.name = name
        self.conference = conference
        self.players = list()
    
    def get_name(self):
        return self.name
    
    def get_conference(self):
        return self.conference
    
    def get_players(self):
        return self.players
    
    def add_player(self, obj):
        self.players.append(obj)

    def populate_teams(team_data):
        teams = list()
        for team_info in team_data:
            t = Team(team_info[0], team_info[1])
            teams.append(t)
        return teams

    def print_team(self):
        print(f"Team name: {self.get_name()}, Conference: {self.get_conference()}")

    def print_team_data(self):
        print("------------------------------")
        self.print_team()
        print("------------------------------")
        for p in self.get_players():
            p.print_player()