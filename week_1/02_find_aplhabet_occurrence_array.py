input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string :
        if not alphabet.isalpha():
            continue
        alphabet_occurrence_array[ord(alphabet)-ord("a")] += 1


    return alphabet_occurrence_array


result = find_max_occurred_alphabet(input)
print(result)