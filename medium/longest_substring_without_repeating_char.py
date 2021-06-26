
def lengthOfLongestSubstring(s):
    # create dictionary such that you can check if letter has been  there
    already_here = {}
    # create an initial starting point and length to get largest length
    start = maxLength = 0

    for i, c in enumerate(s):
        # if you find that the letter is already there and the starting point is before the letter position then you move the starting point to the left
        if c in already_here and start <= already_here[c]:
            start = already_here[c] + 1
        # if the character is new then you haven't moved the cursor and you store the max different between the position you  are in - the start of where you are
        else:
            maxLength = max(maxLength, i - start + 1)

        already_here[c] = i
    print(already_here)
    return maxLength
print(lengthOfLongestSubstring('abcabccabcdef'))