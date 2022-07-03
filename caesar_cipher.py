alphanumerics = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def shift(word, num):
    word_arr = []
    new_word = ""
    for i in word:
        word_arr.append(i)
    for j in range(0, len(word_arr)):
        if word_arr[j] in alphanumerics:
            ind = alphanumerics.index(word_arr[j]) + num
            if ind > (len(alphanumerics) - 1):
                ind = ind % len(alphanumerics)
            elif ind < 0:
                ind = len(alphanumerics) + ind
            word_arr[j] = alphanumerics[ind]
            new_word += alphanumerics[ind]
        else:
            new_word += word_arr[j]
    return new_word


def code(word, num):
    return shift(word, num)


def decode(word, num):
    return shift(word, -num)


def start():
    action = ""
    while action != "code" and action != "decode":
        action = input("Do you want to code, or decode?\n")
    shift_num = ""
    while shift_num.isnumeric() == False:
        shift_num = (input("Enter shift number\n"))
    shift_num = int(shift_num)
    msg = input("Enter your message.\n")
    if action == "code":
        out = code(msg, shift_num)
        print(f"Encoded message: {out}")
    elif action == "decode":
        out = decode(msg, shift_num)
        print(f"Decoded message: {out}")

restart=True

while restart:
    start()
    if_restart=input("Do you want to continue?")
    restart_check=""
    while restart_check=="":
        if if_restart.lower()=="y" or if_restart.lower()=="yes":
            restart = True
            restart_check = 1
        elif if_restart.lower()=="n" or if_restart.lower()=="no":
            restart = False
            restart_check = 1
    if restart == True:
        start()

