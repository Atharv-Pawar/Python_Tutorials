def determine_color(s):
    if (ord(s[0])+int(s[1]))%2 == 0:
        return 'Black'
    elif (ord(s[0])+int(s[1]))%2 != 0:
        return 'White'
    else:
        return 'Invalid Input'

def main():
    import sys
    # input = sys.stdin.read -- if you include it in the code then after input->Ctrl+Z->Enter(key)
    # meanging of "sys.stdin.read" Only read the input till the End of File(EOF) --“Read EVERYTHING from standard input until EOF (End Of File)”
    s = input().strip()  # Read the input string
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()