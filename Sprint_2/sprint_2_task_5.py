# -*- coding: utf-8 -*-


class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):
        return f"Общее колличество очков: {self.victories * 3 + self.draws}"


class Hockey(Results):
    def number_of_wins(self):
        return f"Хокейных побед: {self.victories}"

    def number_of_draws(self):
        return f"Хокейных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Хокейных поражений: {self.losses}"

    def total_points(self):
        return f"Общее колличество очков: {self.victories * 2 + self.draws}"


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

methods = ["number_of_wins", "number_of_draws", "number_of_losses", "total_points"]


for team in (football_team, hockey_team):
    for method in methods:
        func = getattr(team, method)
        print(func())
