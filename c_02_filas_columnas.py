"""filas y columnas"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    page.title = "Mi app mejorada con filas y columnas"
    page.bgcolor = ft.Colors.BLUE_GREY_800

    # elementos
    texto1 = ft.Text(
        value="Texto 1",
        size=24,
        color=ft.Colors.WHITE
    )

    texto2 = ft.Text(
        value="Texto 2",
        size=24,
        color=ft.Colors.WHITE
    )

    texto3 = ft.Text(
        value="Texto 3",
        size=24,
        color=ft.Colors.WHITE
    )

    btn_1 = ft.FilledButton(
        text="Botón 1"
    )

    btn_2 = ft.FilledButton(
        text="Botón 2"
    )

    btn_3 = ft.FilledButton(
        text="Botón 3"
    )

    # organizar elementos en fila
    fila_textos = ft.Row(
        controls=[
            texto1,
            texto2,
            texto3
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    fila_botones = ft.Row(
        controls=[
            btn_1,
            btn_2,
            btn_3
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    # filas y columnas
    # se crean las listas de los textos
    txt_col_1 = [
        ft.Text(value="Columna 1 - Fila 1", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 1 - Fila 2", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 1 - Fila 3", size=18, color=ft.Colors.WHITE),
    ]

    txt_col_2 = [
        ft.Text(value="Columna 2 - Fila 1", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 2 - Fila 2", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 2 - Fila 3", size=18, color=ft.Colors.WHITE),
    ]

    # se coloca cada lista de textos en una columna independiente
    col_txt_1 = ft.Column(controls=txt_col_1)
    col_txt_2 = ft.Column(controls=txt_col_2)

    # se crea una fila de las 2 columnas creadas
    fila_col = ft.Row(
        controls=[col_txt_1, col_txt_2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    # page
    page.add(
        fila_textos,
        fila_botones,
        fila_col
    )


ft.app(main)
