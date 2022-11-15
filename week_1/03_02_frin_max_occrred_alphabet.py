input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string :
        if not alphabet.isalpha():
            continue
        alphabet_occurrence_array[ord(alphabet)-ord("a")] += 1

    max_occurrence =0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    return chr(max_alphabet_index +ord("a"))

result = find_max_occurred_alphabet(input)
print(result)