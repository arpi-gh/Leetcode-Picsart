def isIsomorphic(s: str, t: str) -> bool:
    smap = {}
    tmap = {}
    for l in range(len(s)):
        if s[l] not in smap:
            smap[s[l]] = t[l]
        if t[l] not in tmap:
            tmap[t[l]] = s[l]
        if smap[s[l]] != t[l] or tmap[t[l]] != s[l]:
            return False
    return True


s1 = 'foo'
s2 = 'bar'
print(isIsomorphic(s1, s2))
