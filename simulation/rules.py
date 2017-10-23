# -*- coding: utf-8 -*-

class Rules:

    COOPERATE = 0
    DEFECT = 1

    CHOICES_STR = ['C', 'D']

    #((A A) (C B))
    #((B C) (D D))

    PRISONERS_DILEMA = (((2, 2), (-4, 4)), # B > A > D > C
                        ((4, -4), (0, 0)))
    GAME_OF_CHICKEN = (((2, 2), (0, 4)), # B > A > C > D
                       ((4, 0), (-4, -4)))
    STAG_HUNT = (((4, 4), (-4, 2)), # A > B >= D > C
                 ((2, -4), (0, 0)))

    @staticmethod
    def evaluate(table, decision1, decision2):
        return table[decision1][decision2]
