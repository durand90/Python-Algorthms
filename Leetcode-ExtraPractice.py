

# my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

# print(len(my_dict))





def practice(s):

    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    


#####
    # for i in s:
        # print(i)
        # print(s)

        # if i in my_dict:
        #     print(my_dict[s])

        # print(my_dict[s[i]])
    


########

    result = 0

    for i in range(len(s)):
        if i + 1 < len(s) and my_dict[s[i]] < my_dict[s[i + 1]]:
            print(i)
            # print(my_dict[s[i + 1]])
            result -= my_dict[s[i]]
            print(my_dict[s[i]])
            # print(result)

        else:
            result += my_dict[s[i]]
            print("else:", my_dict[s[i]])
            # print(result)

    print(result)
    return result

practice("XCII")