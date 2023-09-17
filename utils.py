import secrets
import random
import math


def generate_unique_id():
    return secrets.token_hex(10)


def plural(x):
    return 's' if x != 1 else ''


def element_to_color(element):
    return {
        'Earth': 'green',
        'Fire': 'red',
        'Water': 'blue',
        'Air': 'yellow',
    }[element]

def shuffled(l):
    l = l[:]
    random.shuffle(l)
    return l

def sigmoid(x):
    return 1 / (1 + math.exp(-x))