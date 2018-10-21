"""
Author: Julie Perilla Garcia

This script implements the Viterbi algorithm for a hidden markov model.

Input:
    q = States
    s (sigma) = Possible activities
    a = transition matrix
    pi = State start probabilities
    e = Emission matrix
    y = sequence of observed activities
Output:
    v = Likely series of states that occurred to produce the observed activities.
"""
import numpy as np


def viterbi(q, s, a, pi, e, y):
    k = len(q)
    n = len(s)
    v = np.zeros((k, n,))
    return v


Q = ['Rainy', 'Sunny']  # States
S = ['WALK', 'SHOP', 'CLEAN']  # Possible events
A = np.array([[.7, .3], [.4, .6]])  # Transition Matrix
PI = [0.6, 0.4] # Start probabilities
E = np.array([[.1, .4, .5], [.6, .3, .1]])  # Emission Matrix
Y = ['WALK', 'SHOP', 'CLEAN']  # Actual events

V = viterbi(Q, S, A, PI, E, Y)
print(V)
