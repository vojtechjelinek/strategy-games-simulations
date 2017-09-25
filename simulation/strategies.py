# -*- coding: utf-8 -*-

import random

from simulation.rules import Rules

class Strategy:

    def __init__(self):
        self.__points = 0
        self.previous_choices = []

    def decide(self, current_round, enemy_previous_choices):
        pass

    def save_decision(self, choice):
        self.previous_choices.append(choice)

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value



class AlwaysCooperate(Strategy):

    def decide(self, current_round, enemy_previous_choices):
        return Rules.COOPERATE


class AlwaysDefect(Strategy):

    def decide(self, current_round, enemy_previous_choices):
        return Rules.DEFECT


class Random(Strategy):

    def decide(self, current_round, enemy_previous_choices):
        return random.choice((0, 1))
