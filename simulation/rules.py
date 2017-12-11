# -*- coding: utf-8 -*-

class Rules:

    COOPERATE = 0
    DEFECT = 1

    CHOICES_STR = ['C', 'D']

    #((A A) (C B))
    #((B C) (D D))

    PRISONERS_DILEMA = "Prisoners dilemma"
    GAME_OF_CHICKEN = "Game of chicken"
    STAG_HUNT = "Stag hunt"
    RULES = {
        PRISONERS_DILEMA: (((2, 2), (-4, 4)), # B > A > D > C
                           ((4, -4), (0, 0))),
        GAME_OF_CHICKEN: (((2, 2), (0, 4)), # B > A > C > D
                          ((4, 0), (-4, -4))),
        STAG_HUNT: (((4, 4), (-4, 2)), # A > B >= D > C
                    ((2, -4), (0, 0)))
    }

    @staticmethod
    def evaluate(game_name, decision1, decision2):
        return Rules.RULES[game_name][decision1][decision2]
