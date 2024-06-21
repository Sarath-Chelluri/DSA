def pick_coins(treasure):
    count = 0
    skip = 0
    for box in range(1, len(treasure)):
        if treasure[box - 1 + skip] > treasure[box + skip]:
            count += treasure[box + skip]
            skip += 1


print(pick_coins([]))
