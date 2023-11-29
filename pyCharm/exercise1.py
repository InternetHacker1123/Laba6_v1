#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    symbol = input("Введите символ: ")
    sentense = input("Введите предложение: ")

    for i, symb in enumerate(sentense):
        if symb == symbol:
            print(symb)