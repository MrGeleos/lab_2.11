#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def mul(a):
    def helper(b):
        return a * b
    return helper


if __name__ == '__main__':
    print(mul(5)(2))
    