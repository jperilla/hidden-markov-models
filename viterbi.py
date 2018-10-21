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
import numpy


def viterbi(q, s, a, pi, e, y):
    v = numpy.empty((3, 3,))
    return v


