def count_letters(input_str):
    output = {}
    for i in input_str:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output
