# -*- coding: utf-8 -*-

import itertools

import simulation.strategies as strategies
from simulation.game import Game

def run():
    players = [strategy() for strategy in strategies.Strategy.__subclasses__()]
    for (p1, p2) in itertools.combinations(players, 2):
        game = Game(p1, p2, 10)
        game.play()

    print("Final score:")
    for p in players:
        print("{} got {} points and got {} match points".format(
            p.name, p.total_points, p.points_for_matches))

if __name__ == "__main__":
    run()
