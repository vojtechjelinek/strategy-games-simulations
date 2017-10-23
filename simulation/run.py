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

def show_graphs(*players_from_games):
    n_players = len(players_from_games[0])
    colors = ['r', 'g', 'b']
    index = np.arange(n_players)
    width = 0.25
    game_names = ("Prisoner Dilema", "Game of Chicken", "Stag Hunt")

    ax = plt.subplot()
    plots = []
    for (i, game_players) in enumerate(players_from_games):
        data = [p.total_points for p in game_players]
        plot = plt.bar(index + width*i, data, align='center', width=width,
                       color=colors[i])
        plots.append(plot)
    plt.xticks(index + width, [p.name for p in players_from_games[0]])
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=30, horizontalalignment='right')
    plt.ylabel("N of points")
    plt.title("Total poins gain")
    plt.xlim([-0.5, n_players])
    plt.legend(plots, game_names)
    plt.show()

    ax = plt.subplot()
    plots = []
    for (i, game_players) in enumerate(players_from_games):
        data = [p.games_won for p in game_players]
        plot = plt.bar(index + width * i, data, align='center', width=width,
                       color=colors[i])
        plots.append(plot)
    plt.xticks(index + width, [p.name for p in players_from_games[0]])
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=30, horizontalalignment='right')
    plt.ylabel("N of games")
    plt.title("Total Games Won")
    plt.xlim([-0.5, n_players])
    plt.legend(plots, game_names)
    plt.show()


def run(verbose=False):
    players_prisoner_dilema = run_game(
        Rules.PRISONERS_DILEMA, verbose=verbose)
    players_game_of_chicken = run_game(
        Rules.GAME_OF_CHICKEN, verbose=verbose)
    players_stag_hunt = run_game(
        Rules.STAG_HUNT, verbose=verbose)

    show_graphs(
        players_prisoner_dilema, players_game_of_chicken, players_stag_hunt)

if __name__ == "__main__":
    run(True)
