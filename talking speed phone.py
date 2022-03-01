import random
import winsound
import os
fileat = os.path.dirname(os.path.abspath(__file__)) + str("\s")
def speedanswer():
    randomvar = random.randint(1, 5)
    if randomvar == 1:
        print("Speed - ho ho ho")
        winsound.PlaySound(fileat + "peedhohoho", winsound.SND_FILENAME)
        benstart()
    if randomvar == 2:
        print("Speed - yes")
        winsound.PlaySound(fileat + "peedyes", winsound.SND_FILENAME)
        benstart()
    if randomvar == 3:
        print("Speed - no")
        winsound.PlaySound(fileat + "peedno", winsound.SND_FILENAME)
        benstart()
    if randomvar == 4:
        print("Speed - angry eugh")
        winsound.PlaySound(fileat + "peedaugg", winsound.SND_FILENAME)
        benstart()
    if randomvar == 5:
        print("Speed cut the line!")
        winsound.PlaySound(fileat + "peedcutline", winsound.SND_FILENAME)
        askstart()
def benstart():
    input("Ask speed the wise a question: ")
    speedanswer()
def askstart():
    if input("What do you want to do (phone or close) ") == "phone":
        winsound.PlaySound(fileat + "peedstart", winsound.SND_FILENAME)
        print("Speed - Bæn")
        benstart()
    else:
        quit()
askstart()