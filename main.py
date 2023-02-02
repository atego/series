import flet as ft
from entrada import Entrada


def main(page: ft.Page):
    page.title = ''
    page.window_width = 600
    page.window_height = 400

    entrada = Entrada()

    page.add(entrada)

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
