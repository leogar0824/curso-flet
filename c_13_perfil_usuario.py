"""Perfil de usuario que se muestra en tiempo real"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventan
    page.title = "Configurador de Perfil de Usuario"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 820
    page.scroll = "auto"

    # funciones
    def toggle_theme(e):
        """cambio de tema"""
        if theme_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            titulo.color = ft.Colors.LIGHT_BLUE_300
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            titulo.color = ft.Colors.PINK_300
        page.update()

    def update_preview(e):
        """modificar los datos en tiempo real"""
        preview.value = f"""
Nombre: {name_input.value}
Edad: {age_dropdown.value}
Genero: {gender_radio.value}
Intereses: {" - ".join([c.label for c in interest_checkbox.controls if c.value])}
Modo Oscuro: {"Activado" if theme_switch.value else "Desactivado"}
"""
        page.update()

    # elementos
    titulo = ft.Text(
        value="Perfil de Usuario",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.PINK_300
    )

    name_input = ft.TextField(
        label="Nombre",
        border_radius=10,
        on_change=update_preview,
    )

    age_dropdown = ft.Dropdown(
        label="Edad",
        # se recorre del 18 al 101 y cada edad se entrega como string a las opciones del drop
        options=[ft.dropdown.Option(str(age)) for age in range(18, 101)],
        border_radius=10,
        on_change=update_preview
    )

    gender_radio = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(
                    value="Masculino",
                    label="Masculino"
                ),
                ft.Radio(
                    value="Femenino",
                    label="Femenino"
                ),
                ft.Radio(
                    value="Otro",
                    label="Otro"
                )
            ]
        ),
        on_change=update_preview
    )

    interests = ["Arte", "Tecnología", "Música",
                 "Deportes", "Viajes", "Ocio"]

    interest_checkbox = ft.Column(
        controls=[ft.Checkbox(label=interest, on_change=update_preview)
                  for interest in interests]
    )

    theme_switch = ft.Switch(
        label="Modo Oscuro",
        # usar lambda para ejecutar 2 funciones en modo de lista
        on_change=lambda e: [
            update_preview(e),
            toggle_theme(e)
        ]
    )

    preview = ft.Text(
        value="Completa el formulario para ver la previsualización",
        size=14
    )

    # page
    page.add(
        titulo,
        name_input,
        age_dropdown,
        ft.Text(
            value="Genero:",
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        gender_radio,
        ft.Text(
            value="Intereses:",
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        interest_checkbox,
        theme_switch,
        ft.Text(
            value="Previsualización del Perfil:",
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        preview
    )


ft.app(target=main)
