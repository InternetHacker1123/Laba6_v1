#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    first_word = input("Введите первое слово: ").lower()
    second_word = input("Введите второе слово: ").lower()
    value = first_word + second_word
    result = ''
    for i, symb in enumerate(value):
        if value.count(symb) == 1:
            result += f"{symb} "
    print(result)
    
    
