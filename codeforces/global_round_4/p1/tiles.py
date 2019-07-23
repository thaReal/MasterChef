#!/usr/bin/python


# Main
d = [int(x) for x in raw_input().split(" ")]
h = d[0]
w = d[1]

magic = 998244353

print pow(2, h+w) % magic
