# -*- coding: utf-8 -*-

import itertools
import matplotlib.pyplot as plt
import numpy as np

from simulation.game import Game
import simulation.strategies as strategies
from simulation.rules import Rules

def run_game(rules, n_of_rounds=11, verbose=False):
    players = [strategy() for strategy in strategies.Strategy.__subclasses__()]
    games = []
    for (p1, p2) in itertools.combinations(players, 2):
        game = Game(p1, p2, n_of_rounds, rules)
        game.play(verbose)
        games.append(game)

    print("Final score:")
    for p in players:
        print("{} got {} points".format(p.name, p.total_points))

    players.sort(key=lambda p: p.name)
    return players

def show_graph(names, values,  title):
    n_players = len(names)
    index = np.arange(n_players)
    width = 0.25

    ax = plt.subplot()
    plt.bar(index + width, values,
            align='center', width=width)

    plt.title(title)

    plt.xticks(index + width, names)
    plt.xlim([-0.5, n_players])
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=30, horizontalalignment='right')

    plt.ylabel("N of points")
    min_ = int(min(values))
    max_ = int(max(values))
    step = int((max_ - min_) / 10)
    step = 1 if step == 0 else step
    plt.yticks(range(min_, max_ + step, step))

    ax.grid(True)
    plt.tight_layout()
    plt.show()


def show_graphs(players_from_game, add_to_title=""):
    names = [p.name for p in players_from_game]
    values = [p.total_points for p in players_from_game]
    show_graph(names, values, "Total poins gain" + " — " + add_to_title)

    values = [p.games_won for p in players_from_game]
    show_graph(names, values, "Total games won" + " — " + add_to_title)


def run(verbose=False):
    players_prisoner_dilema = run_game(
        Rules.PRISONERS_DILEMA, verbose=verbose)
    show_graphs(players_prisoner_dilema, Rules.PRISONERS_DILEMA)

    players_game_of_chicken = run_game(
        Rules.GAME_OF_CHICKEN, verbose=verbose)
    show_graphs(players_game_of_chicken, Rules.GAME_OF_CHICKEN)

    players_stag_hunt = run_game(
        Rules.STAG_HUNT, verbose=verbose)
    show_graphs(players_stag_hunt, Rules.STAG_HUNT)

if __name__ == "__main__":
    run()
