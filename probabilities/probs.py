from collections import Counter as Counter
import math

AVG_SCORE = 3.5
SCORE_KNIFFEL = 50
SCORE_GR_STRASSE = 40
SCORE_KL_STRASSE = 30
SCORE_FULL_HOUSE = 25

NUMBER_OF_DICES = 5

def kniffel(first_roll):
    probs, _ = pasch(first_roll, 5)
    return probs, SCORE_KNIFFEL

def pasch(first_roll, kind_of):
    '''Errechnet die Pasch Wahrscheinlichkeiten mit der Gewinnsumme'''

    c = Counter((int(x) for x in first_roll))
    if kind_of not in set(range(1,7)):
        raise ValueError("Nur Zahlen von 1-6 als Argument erlaubt")
    number, amount = c.most_common(1)[0]
    needed = kind_of - amount
    gains = number * kind_of + (NUMBER_OF_DICES - kind_of) * AVG_SCORE
    probability = 1 if needed <= 0 else pow(1/6, needed) * 2
    return probability, gains

def gleiche(first_roll, kind_of):
    '''Errechnet die Wahrscheinlichkeiten für mind. 3 Gleiche'''
    c = Counter((int(x) for x in first_roll))
    if kind_of not in set(range(1, 7)):
        raise ValueError("Nur Zahlen von 1-6 als Argument erlaubt")
    number = kind_of
    amount = c[kind_of]
    needed = kind_of - amount
    gains = number * kind_of + (NUMBER_OF_DICES - kind_of) * AVG_SCORE
    probability = 1 if needed <= 0 else pow(1 / 6, needed) * 2
    return probability, gains

def kl_strasse(first_roll):
    '''Errechnet die Wahrscheinlichkeiten für eine kleine Straße'''
    c = Counter((int(x) for x in first_roll))
    num_unique = len(c.most_common())
    needed = 5 - num_unique
    probability = 1 if needed <= 0 else pow(1 / 6, needed) * 2 * (NUMBER_OF_DICES - num_unique)
    return probability, SCORE_KL_STRASSE

def gr_strasse(first_roll):
    '''Errechnet die Wahrscheinlichkeiten für eine kleine Straße'''
    c = Counter((int(x) for x in first_roll))
    num_unique = len(c.most_common())
    needed = NUMBER_OF_DICES - num_unique
    # das hier gilt nur bei einem wurf, wir haben aber noch 2
    probability = 1 if needed <= 0 else math.factorial(needed)/6**needed
    return probability, SCORE_GR_STRASSE

# fix this
def full_house(first_roll):
    c = Counter((int(x) for x in first_roll))
    num_unique = len(c.most_common())
    if num_unique == 1: # we have a kniffel
        pass  
    if num_unique >= 3:
        num_unique 
    needed = 6 - num_unique
    probability = 1 if needed <= 0 else pow(1 / 6, needed) * 2 * (NUMBER_OF_DICES - num_unique)
    return probability, SCORE_GR_STRASSE
