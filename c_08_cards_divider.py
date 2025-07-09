"""Uso de Cards - Divider - VerticalDivider"""

import random as rd
import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Juego de adivinanzas"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # funciones card 1
    def verificar_intentos(e):
        """verificar intentos"""
        nonlocal intentos
        intento = int(input_numero.value)
        intentos += 1

        if intento == numero_secreto:
            resultado.value = f"Correcto! lo adivinaste en {intentos} intentos"
            resultado.color = ft.Colors.GREEN
            btn_verificar.disabled = True
        elif intento < numero_secreto:
            resultado.value = "Demasiado bajo, intenta de nuevo"
            resultado.color = ft.Colors.ORANGE
        else:
            resultado.value = "Demasiado alto, intenta de nuevo"
            resultado.color = ft.Colors.ORANGE

        txt_intentos.value = f"Intentos: {intentos}"
        page.update()

    def reiniciar_juego(e):
        """reinicia el juego"""
        nonlocal intentos, numero_secreto
        numero_secreto = rd.randint(1, 10)
        intentos = 0
        resultado.value = "Adivina el número entre 1 y 10"
        resultado.color = ft.Colors.WHITE
        txt_intentos.value = "intentos: 0"
        btn_verificar.disabled = False
        input_numero.value = ""
        page.update()

    # funciones card2
    def cambiar_tema(e):
        """cambia el tema"""
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.Colors.BLUE_GREY_100
            btn_tema.text = "Modo Oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.Colors.BLUE_GREY_800
            btn_tema.text = "Modo Claro"

        page.update()

    # elementos card1
    titulo = ft.Text(
        value="Cards, Divider y VerticalDivider en Flet",
        size=30,
        weight=ft.FontWeight.BOLD,
    )

    titulo_final = ft.Text(
        value="Área final de la App",
        size=20,
        weight=ft.FontWeight.BOLD
    )

    titulo_juego = ft.Text(
        value="Juego de adivinanza",
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    numero_secreto = rd.randint(1, 10)
    intentos = 0

    input_numero = ft.TextField(
        label="Tu intento",
        width=100
    )

    resultado = ft.Text(
        value="Adivina el número entre 1 y 10"
    )

    btn_verificar = ft.ElevatedButton(
        text="Verificar",
        on_click=verificar_intentos
    )

    txt_intentos = ft.Text(
        value="Intentos: 0"
    )

    btn_reiniciar = ft.ElevatedButton(
        text="Reiniciar",
        on_click=reiniciar_juego
    )

    # elementos card2
    titulo_tema = ft.Text(
        value="Cambiar Tema",
        size=20,
        weight=ft.FontWeight.BOLD
    )

    btn_tema = ft.ElevatedButton(
        text="Modo Claro",
        on_click=cambiar_tema
    )

    # dividers
    divider_simple = ft.Divider(height=1, color=ft.Colors.BLUE_200)
    divider_vertical = ft.VerticalDivider(width=100, color=ft.Colors.BLUE_200)

    # cards
    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    titulo_juego,
                    input_numero,
                    btn_verificar,
                    resultado,
                    txt_intentos,
                    btn_reiniciar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            padding=20
        ),
        width=300,
        height=400
    )

    card2 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    titulo_tema,
                    btn_tema
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            padding=20
        )
    )

    layout = ft.Row(
        controls=[
            card1,
            divider_vertical,
            card2
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # page
    page.add(
        titulo,
        divider_simple,
        layout,
        divider_simple,
        titulo_final
    )


ft.app(main)
