#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    flag = False
    sentence = input("Введите предложение: ")
    sentence = " " + sentence.lower()
    for i, _ in enumerate(sentence):
        if sentence[i - 1] == sentence[i]:
            print(f"Порядковый номер первого символа: {i - 1}\nПорядковый номер второго символа: {i}")
            flag = True
            break
    if flag == False:
        print("Одинаковых соседних символов нет(")
