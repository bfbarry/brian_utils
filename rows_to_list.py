l = []
while True:
    curr = input()
    if curr == '':
        break
    l.append(curr)

print('[')
for i in l:
    print(f"'{i}',")
print(']')
