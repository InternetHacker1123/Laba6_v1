#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    firstWord = input("Введите первое слово: ").lower()
    secondWord = input("Введите второе слово: ").lower()
    value = firstWord + secondWord
    result = ''
    for i, symb in enumerate(value):
        if value.count(symb) == 1:
            result += f"{symb} "
    print(result)
    
    
