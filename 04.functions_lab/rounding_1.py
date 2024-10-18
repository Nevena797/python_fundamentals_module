def rounding(base_list):
    final_number = [round(float(number)) for number in base_list]
    return final_number


input_list = input().split(" ")  # ['1.0', '2.5', '3.0', '4.5']
print(rounding(input_list))
