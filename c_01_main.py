"""main py"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # título de la ventana
    page.title = "Mi app "
    # fondo de color de la ventana
    page.bgcolor = ft.Colors.BLUE_GREY_800
    # alineación de los elementos de la ventana
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # label
    texto = ft.Text("Mi primera app con Flet")
    texto2 = ft.Text("Segunda línea de texto")

    # función para cambiar el texto2
    def cambiar_texto(e):
        """cambiar el texto"""
        texto2.value = "Texto actualizado"
        page.update()

    # botón para realizar el cambio
    boton = ft.FilledButton(
        text="Cambiar Texto",
        on_click=cambiar_texto
    )

    # page
    page.add(
        texto,
        texto2,
        boton
    )


ft.app(main)
