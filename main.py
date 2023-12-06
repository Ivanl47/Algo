def naive_search(haystack, needle):
    comparisons_count = 0
    found_index = -1

    for i in range(len(haystack) - len(needle) + 1):
        match = True

        for j in range(len(needle)):
            comparisons_count += 1
            if haystack[i + j] != needle[j]:
                match = False
                break

        if match:
            found_index = i

    return found_index, comparisons_count

haystack = "ababcababcabc"
needle = "abc"
result_index, comparisons_count = naive_search(haystack, needle)

print(result_index)
