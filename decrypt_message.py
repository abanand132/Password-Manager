from encyrpt_message import alphabet_lower_case, alphabet_upper_case

def decrypt(text):
    list = []

    def shift_finder(text):
        list.append(text[1])
        list.append(text[-2])
        return list
    shift_finder(text)


    def shift_choice_decryption(list):
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

    new_text.pop(1)
    new_text.pop(-2)
    text = "".join(new_text)

    list_alpha = []
    x = []
    fullstop = ["+", ":", "#", "|", "/"]
    at_the_rate = ["<", ">", "~"]
    question_mark = ['1', '5', '7']
    for letter in text:
        if letter.islower():
            pos = alphabet_lower_case.index(letter)
            pos = pos - shift
            list_alpha.append(alphabet_lower_case[pos])

        if letter.isupper():
            pos = alphabet_upper_case.index(letter)
            pos = pos - shift
            list_alpha.append(alphabet_upper_case[pos])

        elif letter == " ":
            list_alpha.append(" ")

        elif letter in fullstop:
            list_alpha.append(".")

        elif letter in at_the_rate:
            list_alpha.append("@")

        elif letter in question_mark:
            list_alpha.append("?")
        else:
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
            if letter == '$':
                list_alpha.append('6')
            if letter == '{':
                list_alpha.append('7')
            if letter == '[':
                list_alpha.append('8')
            if letter == "]":
                list_alpha.append('9')
    simple_text = "".join(list_alpha)
    return simple_text



