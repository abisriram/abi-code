def longest_common_middle_substring(S1, S2):
    n1, n2 = len(S1), len(S2)
    mid1, mid2 = n1 // 2, n2 // 2  # Middle indexes (since lengths are odd)

    # Finding all substrings centered at mid1 in S1
    substrings = set()
    for length in range(1, min(mid1, mid2) + 2):# +2 to include full middle range
        print("length", length)
        for i in range(mid1 - length + 1, mid1 + length):
            print("i",i)
            print("added substring", S1[i: i+length])
            substrings.add(S1[i: i + length])
            print("subsctring", substrings)

    # Finding the longest substring in S2 that matches
    longest = ""
    for sub in substrings:
        if sub in S2 and len(sub) > len(longest):
            print("sub in s2",sub)
            print("Before lon",longest)
            longest = sub
            print("After lon",longest)
            print("sub",sub)
            


    print(longest if longest else -1)


# Taking input
S1 = input().strip()
S2 = input().strip()

# Calling the function
longest_common_middle_substring(S1, S2)
