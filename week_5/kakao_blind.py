def string_compression(string):
    min_len = len(string)
    compressed_length_array = []

    for split_size in range(1, min_len//2 + 1):
        compressed = ""
        splited = [
            string[i:i+split_size] for i in range(0, min_len, split_size)
        ]
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                count += 1
            else :
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1

        if count >1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]

        compressed_length_array.append(len(compressed))
        print(compressed)
    return min(compressed_length_array)

print("정답 : 11, 출력결과는 : ",string_compression("abcdabcdededab"))