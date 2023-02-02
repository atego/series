import flet as ft


class Entrada(ft.UserControl):
    def entrada_input(self):
        return ft.TextField(
            expand=1,
            border_color=ft.colors.TRANSPARENT,
            content_padding=ft.padding.only(left=8),
            height=26,
            text_size=14,
            cursor_height=22,
            cursor_color=ft.colors.BLUE_GREY_200,
        )

    def build(self):
        return ft.Container(
            content=self.entrada_input(),
            bgcolor=ft.colors.AMBER_200,
            border_radius=8
        )
