##1302번: 베스트셀러
## https://www.acmicpc.net/problem/1302
d= dict()
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book]+=1
    else:
        d[book] = 1


max = max(d.values())
condi = []
for k,v in d.items():
    if v == max:
        condi.append(k)

print(sorted(condi)[0])