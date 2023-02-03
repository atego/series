import flet as ft
from marco_entrada import MarcoEntrada


def main(page: ft.Page):
    page.title = ''
    page.window_width = 600
    page.window_height = 400
    page.bgcolor = ft.colors.INDIGO

    entrada = MarcoEntrada()

    page.add(entrada)

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
