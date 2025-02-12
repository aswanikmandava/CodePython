from Team import Team
from Player import Player
from Game import Game

class Main:
    games = list()
    def main():
        games = Main.create_games()
        Main.print_games(games)

    def create_games():
        teams = Main.create_teams()
        game_data = [[1, "2025-02-01", 0, 1, 20455]]
        games = Game.populate_game(teams, game_data)
        Main.games.extend(games)
        return Main.games

    def print_games(games):
        for game in games:
            game.print_game_details()

    def create_teams():
        # define team data
        team_data = [
            ["Kamala", "Conf 1"],
            ["Sarma", "Conf 2"]
        ]
        teams = Team.populate_teams(team_data)

        # Create players for each team
        Main.create_players(teams)
        return teams

    def create_players(teams):
        player_list = [
            ["0", "Aswani Kumar", "1"],
            ["0", "Anil Kumar", "2"],
            ["0", "Mruthyunjay", "3"],
            ["0", "Vinay Kumar", "4"],
            ["0", "Vijay Kumar", "5"],
            ["1", "Hari Krishna", "6"],
            ["1", "Srinivas", "7"],
            ["1", "Amarnath", "8"],
            ["1", "Brahmaji", "9"],
            ["1", "Faridh", "10"]
        ]
        # Populate players into the teams
        team_index = 0
        for team in teams:
            team_players = Player.populate_players(player_list, team_index)
            for player in team_players:
                team.add_player(player)
            team_index += 1

    def print_teams_info(obj_list):
        for obj in obj_list:
            obj.print_team_data()



if __name__ == "__main__":
    Main.main()