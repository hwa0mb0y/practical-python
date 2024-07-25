# bounce.py

init_height = 100
next_height = init_height * (3/5)

for _ in range(10):
    next_height = init_height * (3/5)
    init_height = next_height
    print(round(next_height, 4))
