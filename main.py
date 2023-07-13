from entities.bat import Bat
from controls.menu import show_menu

if __name__ == '__main__':
    bat = Bat()

    event = f"apareció un {bat} salvaje!\n{bat.draw()}\nQue deseas hacer?"

    options = ["Mirarlo fijamente", "Correr", "Atacar", "Llorar"]
    show_menu(event, options)
