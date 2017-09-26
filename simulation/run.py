# -*- coding: utf-8 -*-

import itertools

import simulation.strategies as strategies
from simulation.game import Game

def run():
    players = (strategy() for strategy in strategies.Strategy.__subclasses__())
    for (p1, p2) in itertools.combinations_with_replacement(players, 2):
        game = Game(p1, p2, 10)
        game.play()

if __name__ == "__main__":
    run()
