#!/usr/bin/python3
# -*- coding:utf-8 -*-

#from urllib import response
#import requests
import csv


# 练习一：现有字典 d = {'a':24,'g':52,'l':12,'k':33},请按字典中的value值进行排序.
def sort_dict(d):
    # 返回[('l', 12), ('a', 24), ('k', 33), ('g', 52)]
    sorted(d.items(), key=lambda x: x[1])


# 练习二: age_list=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]，按age由大到小排序:
def sort_age(age_list):
    sorted(age_list, key=lambda x: x['age'], reverse=True)


# 练习三：重新排序数组中的正值和负值，如:给定 [-1,2,-2,3,5,-4], 重新排列后变成 [-1,-2,-4,2,3,5]
def sort_num(all_list):
    print(sorted(all_list, key=lambda x: (x > 0, abs(x))))


# 练习四：通过dicts的value取key：
def getDictKey(myDict, value):
    keyList = []
    for k, v in myDict.items():
        if v == value:
            keyList.append(k)
    return keyList


# 练习五：最长回文字符串。
def longestPalindrome(s):
    if len(s) <= 1:
        return s
    for j in range(len(s), 0, -1):
        for i in range(0, len(s) - j + 1):
            now_s = s[i:i + j]
            if now_s == now_s[::-1]:
                return now_s


#练习六： 查找单链接倒数第k个数
def FindKthToTail(head, k):
    L = []
    while head:
        L.append(head)
        head = head.next
    if k > len(L) or k < 1:
        return None
    return L[-k]


# 练习七： 查找单链接倒数第k个数
def FindKthToTail(head, k):
    L = []
    while head:
        L.append(head)
        head = head.next
    if k > len(L) or k < 1:
        return None
    return L[-k]

# 练习八：房源转go


def myUser():
    # user = [47647026053121, 67790120681473, 70000000010001, 70000119838701, 70000119886001,
    #         70000135884401, 70000137627701, 70000146466001, 70000952072706, 70000987214628]
    url_1 = 'https://test-securewireless-uic.xiaozhu.com/app/xzfk/ios/6.38.00/favorite/favoriteList?sessId=WyIwMTAyMDMyNDIyb0tPayIseyJzc0lkIjoxNTYzNDAxNjk0NzQwNDksInNzVHlwZSI6Im1vYmlsZV9jb2RlIiwiZGF0YSI6IjFhYjVmMDdlNTE5ZDk0ZTY5NTYyZTJhYzBjNmMyZDJkIiwiZXhwaXJlIjoxNjYzNDgyMjQxfSwiNDFlNzUzYWYwMDFiZmIzMDE2MzlmY2VlYWY1YmJkMzMiXQ%3D%3D&userId='
    url_2 = '&anonymous_id=082C5331-F8FF-49DE-9609-A18166FCFB54&bundleType=xztest&gatets=1647941305&gatesign=96ad32a1e5ea0aa6bc7275c8aa3f54a531205232&uniqueId=0E3EBAEF-A88A-4CD6-AD53-40B9E831FFC6&checkInDay=2022-03-22&checkOutDay=2022-03-23&cityId=0&length=30&offset=0&gatetoken=3fb2n4nanqyh2vtzxp375puuuxkfead7'
    header = {"X-Virtual-Env": "feature-backend-210"}
    with open("query_result.csv", "r", encoding="utf-8") as csvfile:
        read = csv.reader(csvfile)
        for cline in read:
            url_3 = url_1 + str(cline[0]) + url_2
            try:
                response = requests.get(url=url_3, headers=header).json()
                print(cline[0], response['content']['collectionNum'])
            except:
                pass


# 练习九: 字符串的所有组合问题，输入三个字符a,b,c，则它们的组合有['a', 'b', 'c', 'ab', 'bc', 'abc']。
def sortABC(s):
    if len(s) <= 1:
        return [s]
    total = []
    lens = len(s)
    for i in range(lens):
        total.append(s[i])
        for j in range(i + 1, lens):
            total.append(s[i:j+1])    ##因为j只能到lens -1，所以需要j+1来取到最后一个数
    return sorted(total, key=lambda i: len(i), reverse=False)

# 练习十: 字符串的所有组合问题，输入三个字符a,b,c，则它们的组合有['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
def strSort(s):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in strSort(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list

print(sortABC('abc'))
