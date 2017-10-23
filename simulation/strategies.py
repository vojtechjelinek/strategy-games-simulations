# -*- coding: utf-8 -*-

from simulation.rules import Rules

class Strategy:

    name = ""

    def __init__(self):
        self.__points = 0
        self.__total_points = 0
        self.__games_won = 0
        self.__previous_choices = []

    def decide(self, current_round, enemy_previous_choices):
        pass

    def save_decision(self, choice):
        self.__previous_choices.append(choice)

    def complete_duel(self, win):
        self.__total_points += self.__points
        self.__previous_choices = []
        self.__points = 0
        self.__games_won += win

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value

    @property
    def total_points(self):
        return self.__total_points

    @property
    def games_won(self):
        return self.__games_won

    @property
    def previous_choices(self):
        return self.__previous_choices

    @property
    def previous_choices_str(self):
        return " ".join(
            Rules.CHOICES_STR[choice] for choice in self.__previous_choices)

    def __str__(self):
        return self.name


class AlwaysCooperate(Strategy):

    name = "Cooperate"

    def decide(self, current_round, enemy_previous_choices):
        return Rules.COOPERATE


class AlwaysDefect(Strategy):

    name = "Defect"

    def decide(self, current_round, enemy_previous_choices):
        return Rules.DEFECT


class RacionalKind(Strategy):

    name = "Kind Racional"

    def decide(self, current_round, enemy_previous_choices):
        if enemy_previous_choices:
            if enemy_previous_choices[-1] == Rules.COOPERATE:
                return Rules.COOPERATE
            else:
                if (len(enemy_previous_choices) >= 2 and
                        enemy_previous_choices[-2] == Rules.COOPERATE):
                    return Rules.COOPERATE
                return Rules.DEFECT

        return Rules.COOPERATE

class RacionalEvil(Strategy):

    name = "Evil Racional"

    def decide(self, current_round, enemy_previous_choices):
        if enemy_previous_choices:
            if enemy_previous_choices[-1] == Rules.COOPERATE:
                if (len(enemy_previous_choices) >= 2 and
                        enemy_previous_choices[-2] == Rules.COOPERATE):
                    return Rules.DEFECT
                return Rules.COOPERATE
            else:
                return Rules.DEFECT

        return Rules.COOPERATE


class Copy(Strategy):

    name = "Copy"

    def decide(self, current_round, enemy_previous_choices):
        if enemy_previous_choices:
            return enemy_previous_choices[-1]
        return Rules.COOPERATE
