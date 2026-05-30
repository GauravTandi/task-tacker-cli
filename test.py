data = ["a", "b", "c", "d"]

for task in data:
    for i in range(1, len(data)+1):
        print(i, data[i-1])
    break
