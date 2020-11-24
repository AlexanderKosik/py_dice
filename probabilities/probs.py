from collections import Counter as Counter

AVG_SCORE = 3.5
SCORE_KNIFFEL = 50
SCORE_GR_STRASSE = 40
SCORE_KL_STRASSE = 30
SCORE_FULL_HOUSE = 25

def kniffel(first):
    probs, _ = pasch(first, 6)
    return probs, SCORE_KNIFFEL

def pasch(first, kind_of):
    '''Errechnet die Pasch Wahrscheinlichkeiten mit der Gewinnsumme'''

    c = Counter((int(x) for x in first))
    if kind_of not in set(range(1,7)):
        raise ValueError("Nur Zahlen von 1-6 als Argument erlaubt")
    number, amount = c.most_common(1)[0]
    needed = kind_of - amount
    gains = number * kind_of + (6-kind_of) * AVG_SCORE
    probability = 100 if needed <= 0 else pow(1/6, needed) * 2
    return round(probability, 3), gains

def gleiche(first, kind_of):
    '''Errechnet die Wahrscheinlichkeiten für mind. 3 Gleiche'''
    c = Counter((int(x) for x in first))
    if kind_of not in set(range(1, 7)):
        raise ValueError("Nur Zahlen von 1-6 als Argument erlaubt")
    number = kind_of
    amount = c[kind_of]
    needed = kind_of - amount
    gains = number * kind_of + (6 - kind_of) * AVG_SCORE
    probability = 100 if needed <= 0 else pow(1 / 6, needed) * 2
    return round(probability, 3), gains

gleiche("666655", 6)

