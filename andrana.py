list = [2, 3, 1, 5, 6]

slist = sorted(list)
print(f"slist = {slist}")

for i in range(len(list)):
    list[i] = i+1
    print(list)