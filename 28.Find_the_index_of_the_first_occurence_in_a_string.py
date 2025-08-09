haystack = "leetcode"
needle = "leeto"

i = 0
first_occurrence = None
for j in range(len(haystack)):
    if haystack[j] == needle[i] and i < len(needle):
        if first_occurrence is None:
            first_occurrence = i
        else:
            i += 1
    else:
        return -1
return first_occurrence