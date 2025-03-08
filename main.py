import sys
from nok_game import play_nok_game
from geometric_progression import play_progression_game

def main():
    # Проверяем, был ли передан аргумент командной строки
    if len(sys.argv) > 1:
        if sys.argv[1] == "nok":
            play_nok_game()
            return
        elif sys.argv[1] == "progression":
            play_progression_game()
            return
        else:
            print("Ошибка: неизвестная игра. Используйте 'nok' или 'progression'.")
            return

    # Если аргумента нет, показываем меню
    print("Выберите игру:")
    print("1 – Игра 'НОК' (наименьшее общее кратное)")
    print("2 – Игра 'Геометрическая прогрессия'")
    print("0 – Выйти")

    choice = input("Введите номер игры: ")

    if choice == "1":
        play_nok_game()
    elif choice == "2":
        play_progression_game()
    elif choice == "0":
        print("Выход из программы.")
    else:
        print("Неверный ввод, попробуйте снова.")
        main()


if __name__ == "__main__":
    main()