s = 'aabcadefss'
nduplicate = []
for i in range(len(s)):
    # print(s[i])
    for j in range(i + 1, len(s)):
        # print(s[j],end='')
        if s[i] != s[j]:
            continue
            # break
        elif s[i] == s[j]:
            nduplicate.append(j - i)
            break
        else:
            nduplicate.append(j-i)

print(nduplicate)
