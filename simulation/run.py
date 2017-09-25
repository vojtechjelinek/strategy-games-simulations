# -*- coding: utf-8 -*-

import simulation.strategies as strategies
from simulation.game import Game

def run():
    possible_strategies = strategies.Strategy.__subclasses__()
    for strategy1 in possible_strategies:
        for strategy2 in possible_strategies:
            player1 = strategy1()
            player2 = strategy2()
            game = Game(player1, player2, 10)
            game.play()
            print(player1)
            print(player2)
            print(player1.points)
            print(player2.points)

if __name__ == "__main__":
    run()
