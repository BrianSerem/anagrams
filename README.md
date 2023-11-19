# anagrams

A string can be formed using another string s by repeatedly concatenating the anagram of s any number of times. Given a string input_str of length n, find out the length of the smallest string s that can be used to create input_str.

Note that the string input_str only consists of lowercase English letters.

Example

input_str = "ababbbaab"

In the above example, the length of the string = 8 n=8.

One of the possible strings s can be "aabb", First append "abab" and then append "baab".
Another possible string s can be "ab", append the anagrams of s in the order: "ab", "ab", "ba" and "ab".
It can be proved that the length of s cannot be reduced further than 2. Hence, we return 2 as the answer.

Function Description

Complete the function getAnagramPeriod in the editor below.

getAnagramPeriod has the following parameter(s):

string input_str: a string of length n
Returns int: the length of the smallest possible string 
