from __future__ import division
import math

class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        numer = numer // gcd
        denom = denom // gcd
        if (denom < 0):
            numer *= -1
            denom *= -1
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer *
                        self.denom,  self.denom * other.denom)


    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer *
                        self.denom,  self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** abs(power), self.denom ** abs(power))

    def __rpow__(self, base):
        return (base ** self.numer) ** (1/self.denom)