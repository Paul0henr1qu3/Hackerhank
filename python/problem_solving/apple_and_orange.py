# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for apple in range(0, len(apples)):
        apples[apple] += a

    for orange in range(0, len(oranges)):
        oranges[orange] += b

    apple_near_to_house = 0
    for apple in apples:
        if apple >= s and apple <= t:
            apple_near_to_house += 1

    print(apple_near_to_house)

    orange_near_to_house = 0
    for orange in oranges:
        if orange >= s and orange <= t:
            orange_near_to_house += 1

    print(orange_near_to_house)