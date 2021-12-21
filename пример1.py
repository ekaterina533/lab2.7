#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mul(a):

    def helper(b):
        return a * b
    return helper


new_mul5 = mul(5)

if __name__ == "__main__":
    print(new_mul5(2))
