def double_string(string):
    doubled = ''
    for letter in string:
        if letter == ' ' or letter is None:
            doubled += ' '
            continue
        doubled = doubled + (2 * letter)
    return doubled


print(double_string("Hello there"))
print(double_string("General Kenobi"))
print(double_string("I've been trained in your Jedi arts"))
