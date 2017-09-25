# -*- coding: utf-8 -*-

from simulation.rules import Rules

class Game:

    def __init__(self, player1, player2, n_rounds):
        self.player1 = player1
        self.player2 = player2
        self.n_rounds = n_rounds

    def play(self):
        for current_round in range(self.n_rounds):
            decision1 = self.player1.decide(
                current_round, self.player2.previous_choices)
            decision2 = self.player2.decide(
                current_round, self.player1.previous_choices)
            self.player1.save_decision(decision1)
            self.player2.save_decision(decision2)

            payoff1, payoff2 = Rules.evaluate(decision1, decision2)

            self.player1.points += payoff1
            self.player2.points += payoff2
