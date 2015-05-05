n = 0
for i in range(18644,33087+1):
    l = str(i)
    if "2" in l and not "7" in l:
        n += 1
print(n)
