# Import the mean function from the statistics module
from statistics import mean



# defining the Player class
class Player:
    
    # list to store all Player instances
    all = []  

    # initialize a new Player instance
    def __init__(self, name):
        # sets the username of the player
        self.username = name  
        # add the new player to the list of all players
        self.all.append(self)  

    # property decorator allows us to define a method but access it like it is an attribute
    @property
    def username(self):
        return self._username 

    # setter for username property
    @username.setter
    def username(self, name):
        # checks if the username is a string and its length is between 2 and 16 characters
        if isinstance(name, str) and 2 <= len(name) <= 16:
            # Setting the username of the player
            self._username = name  
        else:# Raise an exception if the username is not valid
            raise Exception("Username must be a string between 2 and 16 characters.")  



    # method to get the results of the player
    def results(self):
        # returns a list of results where the player is the current player...
        return [result for result in Result.all if result.player is self]



    # method to get the games played by the player
    def games_played(self):
        # returns a list of unique games that the player has played
        return list({result.game for result in self.results()})




    # Method to check if the player has played a specific game
    def played_game(self, game):
        # teturns True if the game is in the list of games played by the player, False otherwise
        return game in self.games_played()

    # Method to get the number of times the player has played a specific game
    def num_times_played(self, game):
        # Get a list of games played by the player
        games_played = [result.game for result in self.results()]
        # Return the count of the specific game in the list of games played
        return games_played.count(game)



    # classmethod to get the player with the highest score in a specific game
    @classmethod
    def highest_scored(cls, game):
        averages = [(game.average_score(player), player) for player in cls.all]
        # If there are no averages, return None
        if not averages:
            return None
        # Get the tuple with the highest average score
        highest_record_tuple = max(averages, key=lambda tup: tup[0])
        # Return the player from the tuple with the highest average score
        return highest_record_tuple[1]


# Define the Game class
class Game:
    all = []  # List to store all Game instances

    # Initialize a new Game instance
    def __init__(self, name):
        self.title = name  # Set the title of the game
        self.all.append(self)  # Add the new game to the list of all games

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def title(self):
        return self._title  # Return the title of the game

    # Setter for title property
    @title.setter
    def title(self, name):
        # Check if the title is a string and it is not empty
        if isinstance(name, str) and not hasattr(self, "title") and name:
            self._title = name  # Set the title of the game
        else:  # Raise an exception if the title is not valid or is changed
            raise Exception("Title must be a string and cannot be changed once set.")  

    # Method to get the results of the game
    def results(self):
        # Return a list of results where the game is the current game
        return [result for result in Result.all if result.game is self]

    # Method to get the players of the game
    def players(self):
        # Return a list of unique players who have results in the current game
        return list({result.player for result in self.results()})

    # Method to get the average score of a player in the game
    def average_score(self, player):
        # Get a list of scores of the player in the game
        scores = [result.score for result in player.results() if result.game is self]
        # Return the mean of the scores if there are scores, 0 otherwise
        return mean(scores) if len(scores) else 0


# Define the Result class
class Result:
    all = []  # List to store all Result instances

    # Initialize a new Result instance
    def __init__(self, player, game, score):
        self.player = player  # Set the player of the result
        self.game = game  # Set the game of the result
        self.score = score  # Set the score of the result
        self.all.append(self)  # Add the new result to the list of all results

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def score(self):
        return self._score  # Return the score of the result







    # Setter for score property
    @score.setter
    def score(self, score):
        # Check if the score is an integer and its value is between 1 and 5000
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5002:
            self._score = score  # Set the score of the result
        else:# Raise an exception if the score is not valid
            raise Exception("Score must be an integer between 1 and 5000.")  

        

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def player(self):
        return self._player  # Return the player of the result

    # Setter for player property
    @player.setter
    def player(self, player):
        # Check if the player is an instance of the Player class
        if isinstance(player, Player):
            self._player = player  # Set the player of the result

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def game(self):
        return self._game  # Return the game of the result

    # Setter for game property
    @game.setter
    def game(self, game):
        # Check if the game is an instance of the Game class
        if isinstance(game, Game):
            self._game = game  # Set the game of the result
