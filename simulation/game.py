# -*- coding: utf-8 -*-

from simulation.rules import Rules

class Game:

    def __init__(self, player1, player2, n_rounds, rules):
        self.player1 = player1
        self.player2 = player2
        self.n_rounds = n_rounds
        self.rules = rules

    def play(self, verbose):
        for current_round in range(self.n_rounds):
            decision1 = self.player1.decide(
                current_round, self.player2.previous_choices)
            decision2 = self.player2.decide(
                current_round, self.player1.previous_choices)
            self.player1.save_decision(decision1)
            self.player2.save_decision(decision2)

            payoff1, payoff2 = Rules.evaluate(self.rules, decision1, decision2)

            self.player1.points += payoff1
            self.player2.points += payoff2

        if verbose:
            print("Duel {} (p1) versus {} (p2):".format(
                str(self.player1), str(self.player2)))
            print("p1 choices: {}".format(self.player1.previous_choices_str))
            print("p2 choices: {}".format(self.player2.previous_choices_str))
            print("p1 got {} points".format(self.player1.points))
            print("p2 got {} points".format(self.player2.points))
            print("\n")

        if self.player1.points > self.player2.points:
            self.player1.complete_duel(1)
            self.player2.complete_duel(0)
        elif self.player1.points < self.player2.points:
            self.player1.complete_duel(0)
            self.player2.complete_duel(1)
        else:
            self.player1.complete_duel(0.5)
            self.player2.complete_duel(0.5)
