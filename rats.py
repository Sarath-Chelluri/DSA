def rat_food(rats, unit, food_in_houses, lens):
    if food_in_houses == []:
        return -1
    total_food = 0
    count = 0
    for i in food_in_houses:
        count += 1
        total_food += i
        if total_food >= rats * unit:
            return count
    else:
        return 0


print(rat_food(7, 8, [], 8))
