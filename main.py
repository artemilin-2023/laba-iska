import string
import random
import keyboard

keyboard.block_key('alt')
keyboard.block_key('ctrl')

MATRIX_LENGTH_DIAPOSONE = range(2, 6)
BREAK_INPUT_SYMBOL = "0"
WORD_LENGTH = 4

def main():

    matrix_lenght = 0
    while True:
        try_input_matrix_lenght = input("Введите размерность матрицы в диапозоне [2, 5]: ")
        if try_input_matrix_lenght.isdigit():
            if int(try_input_matrix_lenght) in MATRIX_LENGTH_DIAPOSONE:
                matrix_lenght = int(try_input_matrix_lenght)
                break
    

    matrix = [[""] * matrix_lenght for _ in range(matrix_lenght)]

    print(f"Вводите слова длинной {WORD_LENGTH} буквы, используя английские символы.\n" +
          f"Если хотите прекаратить ввод слов вручную, введите {BREAK_INPUT_SYMBOL} и оставшиеся ячейки заполнятся автоматически.")
    fill_matrix(matrix)

    print("Исходная матрица:")
    print_matrix(matrix)

    result = []
    for row in matrix:
        for word in row:
            result.append(count_vowel(word))

    result = sorted(result)
    print("Результат: ", result)
    
def fill_matrix(matrix: list) -> None:

    def generate_random_word() -> str:#программ самма выбирает последовательность букв
        word = ""
        alphabet = list(string.ascii_lowercase)
        for _ in range(WORD_LENGTH): 
            word += alphabet[random.randint(0, len(alphabet) - 1)]
    
        return word

    def is_latin_alpha(word: str) -> bool:#проверяем английская ли это буква
        for i in range(len(word)):
            if not ('a' <= word[i] <= 'z' or 'A' <= word[i] <= 'Z'):
                return False
        return True

    user_is_enters = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if user_is_enters:
                user_input = input("Введите слово: ")
                if user_input == BREAK_INPUT_SYMBOL:
                    user_is_enters = False
                    matrix[i][j] = generate_random_word()
                    continue

                if len(user_input) == WORD_LENGTH and is_latin_alpha(user_input):
                    matrix[i][j] = user_input
                else:
                    print("Введенное слово не удовлетовряет критериям, оно автоматически заменилось на случайеное")
                    matrix[i][j] = generate_random_word()
            else:
                matrix[i][j] = generate_random_word()

def print_matrix(matrix: list) -> None:
    for row in matrix:
        print(row) 

def count_vowel(word: str) -> int:
    counter = 0
    vowels = "aeiouy"
    for letter in word:
        if letter.lower() in vowels:
            counter += 1
    return counter

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)

print("Программа завершена")