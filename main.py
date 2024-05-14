import random
from faker import Faker

fake = Faker()

def choose_word():
    return fake.word()

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def play():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Давайте играть в виселицу!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Введите букву: ").lower()

        if guess in guessed_letters:
            print("Вы уже предполагали эту букву.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            displayed = display_word(word_to_guess, guessed_letters)
            print(displayed)
            if '_' not in displayed:
                print("Поздравляем, вы угадали слово!")
                break
        else:
            attempts -= 1
            print("Неправильно! У вас осталось попыток:", attempts)
            if attempts == 0:
                print("У вас не осталось попыток. Вы проиграли.")
                print("Загаданное слово было:", word_to_guess)
                break

    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again == 'да':
        play()

play()
