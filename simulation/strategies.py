#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from simulation.rules import Rules

class Strategy:

    def __init__(self):
        self.points = 0
        self.previous_choices = []

    def decide(self, current_round, enemy_previous_choices):
        pass

class AlwaysCooperates(Strategy):

    def __init__(self):
        super().__init__(self)

    def decide(self, current_round, enemy_previous_choices):
        return Rules.COOPERATE
