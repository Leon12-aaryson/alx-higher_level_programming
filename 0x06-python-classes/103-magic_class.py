#!/usr/bin/python3

class MagicClass:
    def __init__(self, radius = 0):
        self.radius = radius

import dis
dis.dis(MagicClass)
