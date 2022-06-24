import random

alphabet_lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(text):
    shift = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25]
    random.shuffle(shift)
    shift_choice = random.choice(shift)
    list_alpha = []
    numbers = []
    number_pos = []

    i = 0
    for letter in text:
        if letter.islower():
            pos = alphabet_lower_case.index(letter)
            pos = pos + shift_choice
            list_alpha.append(alphabet_lower_case[pos])
            i += 1
        elif letter.isupper():
            pos = alphabet_upper_case.index(letter)
            pos = pos + shift_choice
            list_alpha.append(alphabet_upper_case[pos])
            i += 1
        elif letter == " ":
            list_alpha.append(" ")
            i += 1
        elif letter == ".":
            fullstop = ["+", "#", "|"]
            random.shuffle(fullstop)
            list_alpha.append(random.choice(fullstop))
            i += 1
        elif letter == "@":
            at_the_rate = ["<", ">", "~"]
            random.shuffle(at_the_rate)
            list_alpha.append(random.choice(at_the_rate))
            i += 1
        elif letter == "?":
            question_mark = ["1", "5", "7"]
            random.shuffle(question_mark)
            list_alpha.append(random.choice(question_mark))
            i += 1
        elif letter == "*":
            star_mark = ["2", "3", "0"]
            random.shuffle(star_mark)
            list_alpha.append(random.choice(star_mark))
            i += 1

        elif letter == "#":
            hash_mark = ["4", "6", "8"]
            random.shuffle(hash_mark)
            list_alpha.append(random.choice(hash_mark))
            i += 1

        elif letter == "&":
            and_mark = ["9", "/"]
            random.shuffle(and_mark)
            list_alpha.append(random.choice(and_mark))
            i += 1

        elif letter == "$":
            list_alpha.append(":")
            i += 1

        elif letter == ":":
            list_alpha.append("$")
            i += 1

        elif letter.isdigit():
            numbers.append(letter)
            number_pos.append(i)
            i += 1




    # inserting " numbers "


    def number_encryption(numbers):
        for i in range(len(numbers)):
            if numbers[i] == '0':
                numbers[i] = '!'
            if numbers[i] == '1':
                numbers[i] = '%'
            if numbers[i] == '2':
                numbers[i] = '^'
            if numbers[i] == '3':
                numbers[i] = '&'
            if numbers[i] == '4':
                numbers[i] = ')'
            if numbers[i] == '5':
                numbers[i] = '('
            if numbers[i] == '6':
                numbers[i] = '_'
            if numbers[i] == '7':
                numbers[i] = '{'
            if numbers[i] == '8':
                numbers[i] = '['
            if numbers[i] == '9':
                numbers[i] = ']'
    number_encryption(numbers)         # variables of these functions are declared at top

    xy = 0
    for nos in number_pos:
        list_alpha.insert(nos, numbers[xy])
        xy += 1

    # shift conversion from str to list and encrypting into alphabets
    shift_choice = str(shift_choice)
    new_shift_choice = []
    for i in range(len(shift_choice)):
        new_shift_choice.append(shift_choice[i])

    def shift_choice_encryption(new_shift_choice):
        for i in range(len(new_shift_choice)):
            if new_shift_choice[i] == '1':
                new_shift_choice[i] = 'q'
            if new_shift_choice[i] == '2':
                new_shift_choice[i] = 't'
            if new_shift_choice[i] == '3':
                new_shift_choice[i] = 'a'
            if new_shift_choice[i] == '4':
                new_shift_choice[i] = 'e'
            if new_shift_choice[i] == '5':
                new_shift_choice[i] = 'm'
            if new_shift_choice[i] == '6':
                new_shift_choice[i] = 'z'
            if new_shift_choice[i] == '7':
                new_shift_choice[i] = 'd'
            if new_shift_choice[i] == '8':
                new_shift_choice[i] = 'h'
            if new_shift_choice[i] == '9':
                new_shift_choice[i] = 'j'

    shift_choice_encryption(new_shift_choice)

    j = 0
    option = [1, -1]
    for i in option:
        way = i
        list_alpha.insert(way, new_shift_choice[j])  # initial value of j=0
        j += 1

    # final printing of encrypted text
    ciper_text = "".join(list_alpha)
    return ciper_text
    # print(f"\n Your encrypted message : {ciper_text}")




