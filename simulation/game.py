#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Game:

    def __init__(self, strategy1, strategy2, n_rounds, rules):
        self.player1 = strategy1
        self.player2 = strategy2
        self.n_rounds = n_rounds
        self.rules = rules

    def play(self):
        for current_round in range(self.n_rounds):

            decision1 = self.player1.decide(current_round)
            decision2 = self.player2.decide(current_round)
            payoff1, payoff2 = self.rules.evaluate(decision1, decision2)

            self.player1.points += payoff1
            self.player2.points += payoff2
