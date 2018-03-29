#!/usr/bin/python

letter = ""
message = ""


print "Enter message.\n- Press 2-9 for letters.\n- Enter 0 for spaces and punctuation.\n- Press enter after each character.\n- Enter 1 as the last character to send."
while True:
    letter = raw_input("Message = " + message + "\n")

    if letter == "2":
        message = message + "a"
    elif letter == "22":
        message = message + "b"
    elif letter == "222":
        message = message + "c"
    elif letter == "2222":
        message = message + "2"

    elif letter == "3":
        message = message + "d"
    elif letter == "33":
        message = message + "e"
    elif letter == "333":
        message = message + "f"
    elif letter == "3333":
        message = message + "3"

    elif letter == "4":
        message = message + "g"
    elif letter == "44":
        message = message + "h"
    elif letter == "444":
        message = message + "i"
    elif letter == "4444":
        message = message + "4"

    elif letter == "5":
        message = message + "j"
    elif letter == "55":
        message = message + "k"
    elif letter == "555":
        message = message + "l"
    elif letter == "5555":
        message = message + "5"

    elif letter == "6":
        message = message + "m"
    elif letter == "66":
        message = message + "n"
    elif letter == "666":
        message = message + "o"
    elif letter == "6666":
        message = message + "6"

    elif letter == "7":
        message = message + "p"
    elif letter == "77":
        message = message + "q"
    elif letter == "777":
        message = message + "r"
    elif letter == "7777":
        message = message + "s"
    elif letter == "77777":
        message = message + "7"

    elif letter == "8":
        message = message + "t"
    elif letter == "88":
        message = message + "u"
    elif letter == "888":
        message = message + "v"
    elif letter == "8888":
        message = message + "8"

    elif letter == "9":
        message = message + "w"
    elif letter == "99":
        message = message + "x"
    elif letter == "999":
        message = message + "y"
    elif letter == "9999":
        message = message + "z"
    elif letter == "99999":
        message = message + "9"

    elif letter == "0":
        message = message + " "
    elif letter == "00":
        message = message + "."
    elif letter == "000":
        message = message + "?"
    elif letter == "0000":
        message = message + "!"
    elif letter == "00000":
        message = message + "0"

    elif letter == "1":
        break

    else:
        print "\"" + letter + "\" is not recognized. Try again."

    if message.endswith('1'):
        break
    else:
        continue
