class Game:
    def __init__(self, game_number, game_date, home_team, away_team, people_count):
        self.game_number = game_number
        self.game_date = game_date
        self.home_team = home_team
        self.away_team = away_team
        self.people_count = people_count

    def get_home_team(self):
        return self.home_team
    
    def get_away_team(self):
        return self.away_team
    
    # populate game
    def populate_game(teams, game_data):
        games = list()
        for data in game_data:
            game_number = int(data[0])
            game_date = data[1]
            home_team = teams[int(data[2])]
            away_team = teams[int(data[3])]
            people_count = int(data[4])

            # create and add game to it
            game = Game(game_number, game_date, home_team, away_team, people_count)
            games.append(game)
        return games

    # print game details
    def print_game_details(self):
        print(f"Game #{self.game_number}")
        print(f"Date: {self.game_date}")
        print(f"Attendance: {self.people_count}")
        print(f"Home Team: {self.home_team.get_name()}")
        {self.home_team.print_team_data()}
        print(f"Away Team: {self.away_team.get_name()}")
        self.away_team.print_team_data()