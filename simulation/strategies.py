# -*- coding: utf-8 -*-

import random

from simulation.rules import Rules

class Strategy:


    def __init__(self):
        self.__points = 0
        self.__total_points = 0
        self.previous_choices = []

    def decide(self, current_round, enemy_previous_choices):
        pass

    def save_decision(self, choice):
        self.previous_choices.append(choice)

    def complete_duel(self):
        self.__total_points += self.__points
        self.__points = 0

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value


class AlwaysCooperate(Strategy):

    name = "Cooperator"

    def decide(self, current_round, enemy_previous_choices):
        return Rules.COOPERATE


class AlwaysDefect(Strategy):

    name = "Defector"

    def decide(self, current_round, enemy_previous_choices):
        return Rules.DEFECT


"""class Random(Strategy):

    name = "Randomer"

    def decide(self, current_round, enemy_previous_choices):
        return random.choice((Rules.DEFECT, Rules.COOPERATE))"""


class Copy(Strategy):

    name = "Copycat"

    def decide(self, current_round, enemy_previous_choices):
        if enemy_previous_choices:
            return enemy_previous_choices[-1]
        return Rules.COOPERATE
