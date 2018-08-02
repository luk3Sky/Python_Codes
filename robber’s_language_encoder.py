input_word = str(input("Input: "))
vowels = ['a','A','e','E','i','I','o','O','u','U']
final_str = ''
for letter in input_word:
    # print(letter)
    if letter.isalpha() is True:
        if letter in vowels:
            final_str += (letter)
        else:
            final_str += (letter+"o"+letter.lower())

    else :
        final_str += (letter)
if input_word[-1] is "!":
    pass
else:
    final_str += '!'

print("Output(Encoded): ",str(final_str))