words = []
dif = set()
s = " "
maxi = 0
while s != "":
    s = input()
    if s != "":
        elements = list(s.split())
    for x in elements:
        dif.add(x.upper())
        maxi = max(maxi, len(x))
dif = sorted(dif)
dif.sort()
for i in range(1, maxi + 1):
    ans = []
    answer = ""
    for j in dif:
        if len(j) == i:
            ans.append(j)
    if len(ans) != 0:
        for m in ans:
            answer = m + "; " + answer
        print(f"{i}: {answer[:-2]}")