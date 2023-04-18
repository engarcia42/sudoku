def numCheck(key, num):
    if (num == key):
        print("It is", key)
    else:
        print("It is wrong.")
def main():
    correctNum = 6
    userNum = int(input("Enter a number to test: "))
    numCheck(correctNum, userNum)
    correctNum2 = 1
    userNum = int(input("Entering the 2nd number to compare to a different number: "))
    numCheck(correctNum, userNum)
main()
#if this works...