from entities.bat import Bat
from controls.menu import show_menu
from textwrap import dedent

if __name__ == '__main__':
    bat = Bat()

    event = f"""
    apareció un {bat} salvaje!
    {bat.draw()}
    Que deseas hacer?
    """

    event = dedent(event)

    options = ["Mirarlo fijamente", "Correr", "Atacar", "Llorar"]
    show_menu(event, options)
