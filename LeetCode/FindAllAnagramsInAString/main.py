# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s, p):
        solution = []

        if len(p) > len(s):
            return solution

        letter_occur_p = {}
        s_sum_of_letters = 0

        for letter in p:
            if letter not in letter_occur_p:
                letter_occur_p[letter] = 0
            letter_occur_p[letter] += 1

        for i in range(len(s)):
            if s[i] in letter_occur_p:
                if letter_occur_p[s[i]] > 0:
                    s_sum_of_letters += 1
                letter_occur_p[s[i]] -= 1
            if i >= len(p):
                if s[i - len(p)] in letter_occur_p:
                    letter_occur_p[s[i - len(p)]] += 1
                    if letter_occur_p[s[i - len(p)]] > 0:
                        s_sum_of_letters -= 1

            if len(p) == s_sum_of_letters:
                solution.append(i - len(p) + 1)
        return solution
