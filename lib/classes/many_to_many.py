from statistics import mean


class Game:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self, "title") and isinstance(title, str) and len(title) > 0:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        return mean(
            [result.score for result in self.results() if result.player is player]
        )


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return any([result.game == game for result in self.results()])

    def num_times_played(self, game):
        return sum([result.game == game for result in self.results()])

    @classmethod
    def highest_scored(cls, game):
        max_average = 0
        highest = None
        for player in cls.all:
            ave = game.average_score(player)
            if ave > max_average:
                max_average = ave
                highest = player
        return highest


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not hasattr(self, "score") and isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
