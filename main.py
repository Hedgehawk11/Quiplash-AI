game = int(input("What Quiplash game are you playing please use only the number \n (XL, included in TJPP2 counts as 1)\n "))

print("quit or exit skips an AI question (you must type it in order to move on to voting/round 2/3)")

print("round 1")
import quiplashAnyW1
import quiplashAnyV1

print("round 2")
import quiplashAnyW1
import quiplashAnyV1

print("round 3")
if (game == 1):
    print("The last lash")
    import quiplashXLW3
    import quiplashXLV3
elif (game == 2):
    round3 = int(input("1 for acro lash, 2 for word lash"))
    if (round3 == 1):
        import quiplashTwoW3ACL
    if (round3 == 2):
        import quiplashTwoW3WL
elif (game == 3):
    print("thriplash")
    import quiplashThreeW3
    import quiplashThreeV3

