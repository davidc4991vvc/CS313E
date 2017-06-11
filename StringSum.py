def sum(myStr):
    if(myStr == ""):
        return 0
    try:
        i = int(myStr[0])
        return i + sum(myStr[1:])
    except ValueError:
        return 0 + sum(myStr[1:])

def main():
    myStr = "00"
    mySum = sum(myStr)
    print(mySum)

main()
