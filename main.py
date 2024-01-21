# словарь с азбукой морзе
# dictionary with morse code
MorseCode = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
             'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
             'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
             'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' ', '.': '......',
             ',': '.-.-.-', ';': '-.-.-.', ':': '---...', '?': '..--..', '!': '--..--', '-': '-....-', '(': '-.--.',
             ')': '-.--.-', 'а': ".-", 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-',
             'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
             'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
             'ч': '---.', 'ш': '----', 'щ': '--.-', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-'
             }


# функция дешифрации
# a decryption function
def decode_from_morse(code):
    morse_code_reverse = {v: k for k, v in MorseCode.items()}
    decoded_text = ''
    x61 = code.split('   ')
    x16 = ' # '.join(x61)
    for morse_char in x16.split():
        if morse_char == '#':
            decoded_text += ' '
        elif morse_char in morse_code_reverse:
            decoded_text += morse_code_reverse[morse_char]
    return decoded_text


# функция шифрации
# an encryption function
def encode_to_morse(text):
    encoded_message = []
    for char in text.lower():
        if char in MorseCode:
            encoded_message.append(MorseCode[char])
        elif char == ' ':
            encoded_message.append(' ')
    return ' '.join(encoded_message)


# основная функция программы
# the main function of the program
def main():
    while True:
        print('''Приветствую. Я могу помоч вам закодировать или декодировать азбуку морзе. Введите слово "кодировать"
        или "декодировать". Что бы закончить работу введите "стоп" слова должны разделятся тремя пробелами''')
        a = input()
        if a == 'кодировать':
            print('Введите текст')
            b = input()
            print(encode_to_morse(b))
        elif a == 'декодировать':
            print('Введите код')
            b = input()
            print(decode_from_morse(b))
        elif a == 'стоп':
            print('Завершение работы')
            break
        else:
            print('Программа не может распознать ваш ответ попробуйте снова')
