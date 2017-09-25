#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rules:

    DEFECT = 1
    COOPERATE = 0
    EVALUATING_TABLE = (((2, 2), (-2, 4)),
                        ((4, -2), (0, 0)))

    @classmethod
    def evaluate(cls, decision1, decision2):
        return cls.EVALUATING_TABLE[decision1][decision2]
