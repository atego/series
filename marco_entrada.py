import flet as ft
from entrada import Entrada
from seleccion import Seleccion


class MarcoEntrada(ft.UserControl):
    def build(self):
        self.titulo = Entrada(anchura=200, hint='Título')
        self.plataforma = Seleccion(anchura=140, opciones=['Netflix', 'HBO', 'Amazon'], hint='Plataforma')
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.titulo,
                    self.plataforma
                ]
            )
        )
