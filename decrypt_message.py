from encyrpt_message import alphabet_lower_case, alphabet_upper_case

def decrypt(text):
    list = []

    def shift_finder(text):    # finding shift no. in the encrypted form
        list.append(text[1])
        list.append(text[-2])
        return list
    shift_finder(text)


    def shift_choice_decryption(list):  # decoding shift no. in its real form which is integer
        for i in range(len(list)):
            if list[i] == 'q':
                list[i] = 1
            if list[i] == 't':
                list[i] = 2
            if list[i] == 'a':
                list[i] = 3
            if list[i] == 'e':
                list[i] = 4
            if list[i] == 'm':
                list[i] = 5
            if list[i] == 'z':
                list[i] = 6
            if list[i] == 'd':
                list[i] = 7
            if list[i] == 'h':
                list[i] = 8
            if list[i] == 'j':
                list[i] = 9
    shift_choice_decryption(list)
    shift = str(list[0]) + str(list[1])
    shift = int(shift)
    new_text = []
    for i in range(len(text)):
        new_text.append(text[i])

    new_text.pop(1)                         # popping out shift no. from original encrypted text
    new_text.pop(-2)                        # popping out shift no. from original encrypted text
    text = "".join(new_text)

    list_alpha = []

    fullstop = ["+", "#", "|"]       # list of all options available to encrypt a fullstop '.'
    at_the_rate = ["<", ">", "~"]             # list of all options available to encrypt a @ '.'
    question_mark = ["1", "5", "7"]
    star_mark = ["2", "3", "0"]
    hash_mark = ["4", "6", "8"]
    and_mark = ["9", "/"]

    for letter in text:
        if letter.islower():                   # decrypting all alphabets
            pos = alphabet_lower_case.index(letter)
            pos = pos - shift
            list_alpha.append(alphabet_lower_case[pos])

        if letter.isupper():                   # decrypting all alphabets
            pos = alphabet_upper_case.index(letter)
            pos = pos - shift
            list_alpha.append(alphabet_upper_case[pos])

        elif letter == " ":
            list_alpha.append(" ")

        elif letter in fullstop:          # decrypting '.' , fullstop = ["+", ":", "#", "|", "/"]
            list_alpha.append(".")

        elif letter in at_the_rate:       # decrypting @ ,   at_the_rate = ["<", ">", "~"]
            list_alpha.append("@")

        elif letter in question_mark:    # decrypting ? ,    question_mark = ['1', '5', '7']
            list_alpha.append("?")

        elif letter in star_mark:    # decrypting * ,    star_mark = ["2", "3", "0"]
            list_alpha.append("*")

        elif letter in hash_mark:    # decrypting # ,    hash_mark = ["4", "6", "8"]
            list_alpha.append("#")

        elif letter in and_mark:    # decrypting & ,    and_mark = ["9", "/"]
            list_alpha.append("&")

        elif letter == ":":
            list_alpha.append("$")

        elif letter == "$":
            list_alpha.append(":")

        else:                           # decrypting numbers
            if letter == '!':
                list_alpha.append('0')
            if letter == '%':
                list_alpha.append('1')
            if letter == '^':
                list_alpha.append('2')
            if letter == '&':
                list_alpha.append('3')
            if letter == ')':
                list_alpha.append('4')
            if letter == '(':
                list_alpha.append('5')
            if letter == '_':
                list_alpha.append('6')
            if letter == '{':
                list_alpha.append('7')
            if letter == '[':
                list_alpha.append('8')
            if letter == "]":
                list_alpha.append('9')
    simple_text = "".join(list_alpha)
    return simple_text
    # print(simple_text)


