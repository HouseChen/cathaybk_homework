#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

# 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

# 輸出：
# 0 1
# 6 1
# A 4
# C 2
# E 5
# H 3
# ....(繼續印下去)

# execute command: python3 test2.py

def count_and_print_alphabet(text_string):
    letter_counts = {}
    tmp_text_string = text_string.replace(' ','').upper()

    for char in tmp_text_string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[0])

    return sorted_letter_counts

if __name__ == "__main__":
    test_text = "Hello welcome to Cathay 60th year anniversary"
    
    result = count_and_print_alphabet(test_text)
    # print(result)
    for letter, result_count in result:
        # print(f"{letter} {result_count}")     python3 
        print("%s %s" % (letter, result_count)) 
    print("題目範例的輸出有錯！ a是5個不是4個")
