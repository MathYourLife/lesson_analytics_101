#!/usr/bin/env python
#
# Copyright 2014 Daniel Couture (GNU GPLv3)
#
"""
Implement a time series control chart.

Usage:

    cat data | python{3} control_chart.py

Errors to stdout:

    [x] is < 3 sigma
    [x] is > 3 sigma
    [x] is 2/3 points > 2 sigma
    [x] is 2/3 points < 2 sigma
    [x] is 4/5 points > 1 sigma
    [x] is 4/5 points < 1 sigma
    [x] is 8/8 points > centerline
    [x] is 8/8 points < centerline
    [x] is 10/11 points > centerline
    [x] is 10/11 points < centerline
    [x] is 12/14 points > centerline
    [x] is 12/14 points < centerline
    [x] is 14/17 points > centerline
    [x] is 14/17 points < centerline
    [x] is 16/20 points > centerline
    [x] is 16/20 points < centerline

Test Source:
    Implementing Six Sigma
    Smarter Solutions Using Statistical Methods
    Forrest W. Breyfogle III
    Second Edition, pp. 221

Out of control tests:
    1 data point is > 3 sigma (or < -3 sigma)
    2 of 3 points are > 2 sigma (or < -2 sigma)
    4 of 5 points are > 1 sigma (or < -1 sigma)
    8 points are on one side of the mean

Shift in centerline tests:
    >= 10 out of 11 points are on one side of the mean
    >= 12 out of 14 points are on one side of the mean
    >= 14 out of 17 points are on one side of the mean
    >= 16 out of 20 points are on one side of the mean
"""

import os
import sys
import numpy as np
from argparse import ArgumentParser


class Window(object):

    def __init__(self, n, init=None):
        self.idx = 0
        self.n = n
        self.data = np.empty(n)
        if init is None:
            self.data.fill(np.nan)
        else:
            self.data.fill(init)

    def append(self, value):
        try:
            self.data[self.idx] = value
        except IndexError:
            self.idx = 0
            self.data[self.idx] = value
        self.idx += 1

    def __str__(self):
        return str(self.data)


def err_out(msg):
    sys.stderr.write("%s\n" % msg)
    sys.stderr.flush()


def test_3_sigma(options):
    lcl = options.m - 3 * options.s
    ucl = options.m + 3 * options.s
    def test(x):
        if x < lcl:
            err_out("%g is < 3 sigma" % x)
        elif x > ucl:
            err_out("%g is > 3 sigma" % x)
    return test

def test_2_sigma(options):
    w = Window(3, init=options.m)
    lcl = options.m - 2 * options.s
    ucl = options.m + 2 * options.s
    def test(x):
        w.append(x)
        if np.sum(w.data > ucl) >= 2:
            err_out("%s is 2/3 points > 2 sigma" % w.data)
        elif np.sum(w.data < lcl) >= 2:
            err_out("%s is 2/3 points < 2 sigma" % w.data)
    return test


def test_1_sigma(options):
    w = Window(5, init=options.m)
    lcl = options.m - 1 * options.s
    ucl = options.m + 1 * options.s
    def test(x):
        w.append(x)
        if np.sum(w.data > ucl) >= 4:
            err_out("%s is 4/5 points > 1 sigma" % w.data)
        elif np.sum(w.data < lcl) >= 4:
            err_out("%s is 4/5 points < 1 sigma" % w.data)
    return test


def test_cl_shift(options):
    """
    8 out of 8 points are on one side of the mean
    >= 10 out of 11 points are on one side of the mean
    >= 12 out of 14 points are on one side of the mean
    >= 14 out of 17 points are on one side of the mean
    >= 16 out of 20 points are on one side of the mean
    """
    windows = [
        (8, Window(8, init=options.m)),
        (10, Window(11, init=options.m)),
        (12, Window(14, init=options.m)),
        (14, Window(17, init=options.m)),
        (16, Window(20, init=options.m)),
    ]
    cl = options.m
    def test(x):
        for n, w in windows:
            w.append(x)
            if np.sum(w.data > cl) >= n:
                err_out("%s is %g/%g points > centerline" %
                    (w.data, n, w.n))
            elif np.sum(w.data < cl) >= n:
                err_out("%s is %g/%g points < centerline" %
                    (w.data, n, w.n))
    return test


def control_chart(stream, options):
    tests = []
    tests.append(test_3_sigma(options))
    tests.append(test_2_sigma(options))
    tests.append(test_1_sigma(options))
    tests.append(test_cl_shift(options))

    for x in stream:
        for test in tests:
            test(x)


def load_stream(input_stream):
    for line in input_stream:
        clean_line = line.strip()
        if not clean_line:
            # skip empty lines (ie: newlines)
            continue
        if clean_line[0] in ['"', "'"]:
            clean_line = clean_line.strip('"').strip("'")
        try:
            yield float(clean_line)
        except:
            err_out("invalid line %r" % line)


def parse_args():
    _, fname = os.path.split(__file__)
    usage = "cat data | python %s" % fname

    parser = ArgumentParser(usage=usage)
    parser.add_argument("-m", "--center", dest="m", required=True,
                        type=float, help="control chart centerline")
    parser.add_argument("-s", "--stdev", dest="s", required=True,
                        type=float, help="standard deviation")

    if sys.stdin.isatty():
        # if isatty() that means it's run without anything piped into it
        parser.print_usage()
        print("for more help use --help")
        sys.exit(1)
    return parser.parse_args()


def main():
    options = parse_args()
    control_chart(load_stream(sys.stdin), options)


if __name__ == "__main__":
    main()