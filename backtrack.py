def numCheck(key, num):
    if (num == key):
        print("It is", key)
    else:
        print("It is wrong.")
def main():
    correctNum = 6
    userNum = int(input("Enter a number to test: "))
    numCheck(correctNum, userNum)
main()