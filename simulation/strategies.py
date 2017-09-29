# -*- coding: utf-8 -*-

from simulation.rules import Rules

class Strategy:


    def __init__(self):
        self.__points = 0
        self.__total_points = 0
        self.__points_for_matches = 0
        self.__previous_choices = []

    def decide(self, current_round, enemy_previous_choices):
        pass

    def save_decision(self, choice):
        self.__previous_choices.append(choice)

    def complete_duel(self, win):
        self.__total_points += self.__points
        self.__previous_choices = []
        self.__points = 0
        self.__points_for_matches += win

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
    def points_for_matches(self):
        return self.__points_for_matches

    @property
    def previous_choices(self):
        return self.__previous_choices


class AlwaysCooperate(Strategy):

    name = "Cooperator"

    def decide(self, current_round, enemy_previous_choices):
        return Rules.COOPERATE


class AlwaysDefect(Strategy):

    name = "Defector"

    def decide(self, current_round, enemy_previous_choices):
        return Rules.DEFECT


class Racional(Strategy):

    name = "Racionator"

    def decide(self, current_round, enemy_previous_choices):
        if enemy_previous_choices:
            if enemy_previous_choices[-1] == Rules.COOPERATE:
                return Rules.COOPERATE
            else:
                if (len(enemy_previous_choices) == 2 and
                        enemy_previous_choices[-2] == Rules.COOPERATE):
                    return Rules.COOPERATE
                return Rules.DEFECT

        return Rules.COOPERATE




class Copy(Strategy):

    name = "Copycat"

    def decide(self, current_round, enemy_previous_choices):
        if enemy_previous_choices:
            return enemy_previous_choices[-1]
        return Rules.COOPERATE
