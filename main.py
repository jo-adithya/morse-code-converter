MORSE_CODE = {
    'a': ' •- ',
    'b': ' -••• ',
    'c': ' -•-• ',
    'd': ' -•• ',
    'e': ' • ',
    'f': ' ••-• ',
    'g': ' --• ',
    'h': ' •••• ',
    'i': ' •• ',
    'j': ' •--- ',
    'k': ' -•- ',
    'l': ' •-•• ',
    'm': ' -- ',
    'n': ' -• ',
    'o': ' --- ',
    'p': ' •--• ',
    'q': ' --•- ',
    'r': ' •-• ',
    's': ' ••• ',
    't': ' - ',
    'u': ' ••- ',
    'v': ' •••- ',
    'w': ' •-- ',
    'x': ' -••- ',
    'y': ' -•-- ',
    'z': ' --•• ',
    '0': ' ----- ',
    '1': ' •---- ',
    '2': ' ••--- ',
    '3': ' •••-- ',
    '4': ' ••••- ',
    '5': ' ••••• ',
    '6': ' -•••• ',
    '7': ' --••• ',
    '8': ' ---•• ',
    '9': ' ----• ',
    '.': ' •-•-•- ',
    ',': ' --••-- ',
    '?': ' ••--•• ',
    "'": ' •----• ',
    '/': ' -••-• ',
    ':': ' ---••• ',
    ';': ' -•-•-• ',
    '+': ' •-•-• ',
    '-': ' -••••- ',
    '=': ' -•••- ',
}

if __name__ == "__main__":
    print('—————————————————————————————————————————————————————————————')
    print('Welcome to String to Morse Code Converter\n')
    while True:
        attempt = input('Do you want to convert string into morse code? ').lower()
        if attempt != 'y' and attempt != 'yes':
            break
        s = input('Enter the text: ').lower()
        morse = [MORSE_CODE[letter] for letter in s if letter in MORSE_CODE]
        print(''.join(morse))
        print()