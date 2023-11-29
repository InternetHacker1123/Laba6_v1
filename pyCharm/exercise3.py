#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Введите предложение: ")
    sp = list(sentence)
    for i, symb in enumerate(sp):
        if i % 2 != 0 and symb == "о":
           del sp[i]
    sentence = ''.join(sp)
    print(sentence)