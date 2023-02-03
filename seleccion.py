import flet as ft


class Seleccion(ft.UserControl):
    def __init__(self, anchura: int, opciones: list[str], hint: str):
        super().__init__()
        self.anchura: int = anchura
        self.opciones: list[str] = opciones
        self.hint: str = hint

    def build(self):
        return ft.Container(
            content=ft.Dropdown(
                options=[ft.dropdown.Option(x) for x in self.opciones],
                hint_text=self.hint,
                border=ft.InputBorder.NONE,
                height=40,
                text_size=14,
                border_radius=8,
                text_style=ft.TextStyle(weight=ft.FontWeight.W_500)
            ),
            bgcolor=ft.colors.BLUE_GREY_200,
            border_radius=8,
            padding=ft.padding.only(left=8),
            width=self.anchura,
            alignment=ft.alignment.center,
        )
