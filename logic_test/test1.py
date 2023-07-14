#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

# 國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，請用一個函數來將學生的成績修正。

# 輸入: [35, 46, 57, 91, 29]
# 輸出: [53, 64, 75, 19, 92]

# execute command: python3 test1.py

def fix_incorrect_score(score_list):
    result = []
    for score in score_list:
        if type(score) == int:
            score_str = str(score)
            if "0" not in score_str:
                fixed_num = int(score_str[::-1])
                # fixed_num=''.join(reversed(score_str))
            else:
                fixed_num = score
            result.append(fixed_num)
        else:
            return "Error!! Input list should be int."
    return result


if __name__ == "__main__":
    A = [35, 46, 57, 91, 29]
    expect_result = [53, 64, 75, 19, 92]

    # 假設 0, 100, 80 有0的與個位數的成績不會key錯
    # A = [35, 46, 57, 91, 29, 77, 0, 100, 80, 6]
    # expect_result = [53, 64, 75, 19, 92, 77, 0, 100, 80, 6]

    # 假設 key的不是數字
    # A = [90, "A"]

    test_result = fix_incorrect_score(A)
    print(test_result)
    if test_result == expect_result:
        print("This function is correct.")
    else:
        print("Something wrong in this function.")
