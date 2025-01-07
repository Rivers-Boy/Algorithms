"""
https://codeforces.com/problemset/problem/2039/B
对于一个字符串 p，定义 f(p) 为 p 的不同非空子字符串的数量。
Shohag 有一个字符串 s。请帮助他找到一个非空字符串 p，使得 p 是 s 的子字符串，且 f(p) 是一个偶数；或者说明这样的字符串不存在。

输入：第一行给出 case 的数量(10**4)，后续每个给出一个只包含小写字母字符串(10**5)
输出：如果存在 p则输出 p，不存在则返回-1

观察发现：
    如果 p = 1, 显然不符合要求
    如果 p = 2，同时两个字符相等，此时 f(p)为偶数
    如果 p = 3, 如果存在两个连续字符相等，则变为 2 的情况直接返回连续字符，
               如果不存在连续字符相等则只剩下 abc, aba两种情况，其中 abc 符合条件
    由此反推断出什么字符串不符合条件呢？形如 ababababab...这样的

"""


def solution(s):
    n = len(s)
    if n == 1:
        return -1
    if n == 2:
        return s if s[0] == s[1] else -1
    for i in range(1, n - 1):
        if s[i] == s[i - 1]:
            return s[i - 1:i + 1]
        if s[i] != s[i + 1] and s[i - 1] != s[i] and s[i - 1] != s[i + 1]:
            return s[i - 1:i + 2]
    return s[n - 2:] if s[-1] == s[-2] else -1


def solve():
    n = int(input())
    for _ in range(n):
        print(solution(input()))


if __name__ == "__main__":
    solve()