l = [1, 2, 3, 4]

while l:
    front, *l = l
    print(front, l)
    