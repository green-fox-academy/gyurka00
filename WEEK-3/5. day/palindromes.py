def str_reverse(string):
    return string[::-1]

def create_palindrome(string):
    return string + string[::-1]

def search_palindromes(string):
    words = string.split()
    palindromes = []
    for word in words:
        lenght = 3
        if len(word) >= lenght:
            while lenght <= len(word):
                i = lenght - 1
                while i < len(word):
                    start_char=i+1-lenght
                    if word[start_char:i+1] == str_reverse(word[start_char:i+1]) and word[start_char:i+1] != '' and word[start_char:i+1] != word[start_char-1:i]:
                        palindromes.append(word[start_char:i+1])
                    i += 1
                lenght += 1

    return palindromes

def palindromes_input():
    input_string = ''
    while input_string == '' :
        try:
            input_string = input('Write some word in a string: ')
            if not input_string:
                raise ValueError('empty string')
        except ValueError:
            print("Your entered a wrong value")
    return search_palindromes(input_string)

print(palindromes_input())
