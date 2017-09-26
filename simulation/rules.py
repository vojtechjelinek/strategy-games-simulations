# -*- coding: utf-8 -*-

class Rules:

    DEFECT = 1
    COOPERATE = 0
    EVALUATING_TABLE = (((2, 2), (-4, 4)),
                        ((4, -4), (0, 0)))

    EVALUATING_TABLE2 = (((2, 2), (-4, 4)),
                         ((4, -4), (-8, -8)))

    @classmethod
    def evaluate(cls, decision1, decision2):
        return cls.EVALUATING_TABLE2[decision1][decision2]
