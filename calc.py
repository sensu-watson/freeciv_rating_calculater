#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import math

class Player:
    def __init__(self, name, oldrate, score):
        self.name = name
        self.oldrate = oldrate
        self.score = score

    def calcrate(self, baserate, averagepoint, devpoint):
        if 0 < baserate - self.oldrate:
            newrate = self.oldrate + (baserate - self.oldrate) / math.sqrt(baserate - self.oldrate) + 30 * (self.score - averagepoint) / devpoint
        else :
            newrate = self.oldrate + (baserate - self.oldrate) / math.sqrt(self.oldrate - baserate) + 30 * (self.score - averagepoint) / devpoint
        return newrate

    def retoldrate(self):
        return self.oldrate

    def retscore(self):
        return self.score

    def retname(self):
        return self.name

            
if __name__ == '__main__':
    playerlist = []
    playerlist.append(Player('orz', 2029, 362))
    playerlist.append(Player('suomi', 1889, 228))
    playerlist.append(Player('gakuto', 1417, 184))
    playerlist.append(Player('moheji', 1622, 179))
    playerlist.append(Player('tanun3sei', 1300, 170))
    playerlist.append(Player('korins', 1300, 115))

    baserate = 0
    averagepoint = 0
    dobleavepoint = 0
    i=0
    for pl in playerlist:
        baserate += pl.retoldrate()
        averagepoint += pl.retscore()
        dobleavepoint += pl.retscore() * pl.retscore()
        i+=1
    baserate = baserate / i
    averagepoint = averagepoint / i
    dobleavepoint = dobleavepoint / i
    devpoint = dobleavepoint - averagepoint * averagepoint
    devpoint = math.sqrt(devpoint)

    for pl in playerlist:
        score = pl.calcrate(baserate, averagepoint, devpoint)
        name = pl.retname()
        print(name + ' : ' + str(score))
