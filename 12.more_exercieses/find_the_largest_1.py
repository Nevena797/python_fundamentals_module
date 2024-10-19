origin_number_like_txt = input()
while True:
    first_digit_s = ''
    for element in range(len(origin_number_like_txt) - 1):
        if int(origin_number_like_txt[element]) < int(origin_number_like_txt[element + 1]):
            origin_number_like_txt = first_digit_s + origin_number_like_txt[element + 1] + \
                                     origin_number_like_txt[element] + origin_number_like_txt[element + 2:]
            break
        else:
            first_digit_s += origin_number_like_txt[element]
    else:
        break
print(origin_number_like_txt)
