vol_lvl: int = int(input("please enter the volume level of the speaker: "))
match vol_lvl:
    case 0:
        print("mute")
    case 1:
        print("very quiet")
    case 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9:
        print("extremely loud")
    case 10:
        print("extremely loud")
    case _:
        print("Invalid volume level")

#לא מצליח להריץ "match" כנראה בגלל הגרסא של הפייתון וזה לא נותן לי כרגע לשנות את הגרסא משום מה, מאמין אבל שהקוד יעבוד