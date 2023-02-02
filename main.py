import flet as ft


def main(page: ft.Page):
    page.title = ''
    page.window_width = 600
    page.window_height = 400

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
