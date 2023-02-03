import flet as ft


class Entrada(ft.UserControl):
    def __init__(self, anchura: int, hint: str):
        super().__init__()
        self.anchura: int = anchura
        self.hint: str = hint

    def build(self):
        return ft.Container(
            width=self.anchura,
            height=40,
            bgcolor=ft.colors.BLUE_GREY_200,
            border_radius=8,
            padding=8,
            content=ft.Row(
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.TextField(
                        border_color=ft.colors.TRANSPARENT,
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_width=1,
                        hint_text=self.hint,
                        expand=True,
                        capitalization=ft.TextCapitalization.SENTENCES
                    )
                ]
            )
        )
