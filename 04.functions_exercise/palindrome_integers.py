def palindrome(integers):
    for x in integers:
        if x == x[::-1]:
            print("True")
        else:
            print("False")


list_of_positive_integers = input().split(", ")
palindrome(list_of_positive_integers)
