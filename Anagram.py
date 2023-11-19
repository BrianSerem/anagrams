def getAnagramPeriod(input_str):
    # Function to check if a substring can form anagrams
    def can_form_with_anagrams(s, sub):
        if len(s) % len(sub) != 0:
            return False
        for i in range(0, len(s), len(sub)):
            if sorted(s[i:i + len(sub)]) != sorted(sub):
                return False
        return True

    # Main loop to find the smallest substring
    for i in range(1, len(input_str) + 1):
        substring = input_str[:i]
        if can_form_with_anagrams(input_str, substring):
            return len(substring)

    return len(input_str)

test_str = "abcabcd"
print(getAnagramPeriod(test_str))
