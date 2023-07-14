#!/usr/bin/env python3
# -*-  coding: utf-8 -*-
import random

# QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
# 請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

# 輸入：n值(0-100)
# 輸出：第幾順位

# execute command: python3 test3.py


def find_the_last_one(n):
    if type(n) == int:
        if n != 0:
            member_list = list(range(1, n + 1))

            index = 0
            while len(member_list) > 1:
                index = (index + 2) % len(member_list)
                member_list.pop(index)
                # print(member_list)
            return member_list[0]
        else:
            return 0
    else:
        return "Error!! Input should be int."


if __name__ == "__main__":
    n = random.randint(0, 100)
    # n = 27
    result = find_the_last_one(n)

    if result != 0:
        print(f"共有{n}個同事，最後留下的是第 {result} 順位")
    else:
        print("QA部門沒有人!")
