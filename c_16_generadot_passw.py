"""generador de contraseñas"""
import random as rd
import string as st
import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Generador Contraseñas"
    page.window.center()

    # funciones
    def generate_password(length, use_uppercase, use_numbers, use_symbols):
        """generador de contraseña"""
        # juntar todos los caracteres del codigo ascii letras minusculas
        characters = st.ascii_lowercase
        # agregar a characters los tipos de caracter si son true
        if use_uppercase:
            characters += st.ascii_uppercase
        if use_numbers:
            characters += st.digits
        if use_symbols:
            characters += st.punctuation
        # retornar un aleatorio de (length) caracteres
        return "".join(rd.choice(characters) for _ in range(length))

    def update_password(e):
        """actializar el pasw"""
        password_field.value = generate_password(
            length=int(length_slider.value),
            use_uppercase=uppercase_switch.value,
            use_numbers=numbers_switch.value,
            use_symbols=symbols_switch.value
        )
        page.update()

    def copy_to_clipboard(e):
        """copiar al portapapeles"""
        page.set_clipboard(password_field.value)
        # mostrar mensaje te texto copiado
        snack_bar = ft.SnackBar(
            content=ft.Text("Contraseña copiada al portapapeles")
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    # elementos
    titulo = ft.Text(
        value="Generador de Contraseñas",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    password_field = ft.TextField(
        read_only=True,
        width=400,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.BOLD
        )
    )

    length_slider = ft.Slider(
        value=12,
        min=8,
        max=32,
        divisions=24,
        label="{value}",
        on_change=update_password
    )

    generate_button = ft.ElevatedButton(
        text="Generar contraseña",
        on_click=update_password,
        icon=ft.Icons.REFRESH
    )

    uppercase_switch = ft.Switch(
        label="Mayúsculas",
        value=True,
        on_change=update_password
    )

    numbers_switch = ft.Switch(
        label="Números",
        value=False,
        on_change=update_password
    )
    symbols_switch = ft.Switch(
        label="Símbolos",
        value=False,
        on_change=update_password
    )

    copy_button = ft.ElevatedButton(
        text="Copiar al portapapeles",
        on_click=copy_to_clipboard,
        icon=ft.Icons.COPY
    )

    # page
    page.add(
        titulo,
        ft.Column(
            controls=[
                ft.Text("Longitud de la contraseña:"),
                length_slider,
                uppercase_switch,
                numbers_switch,
                symbols_switch,
                password_field
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        ft.Row(
            controls=[
                generate_button,
                copy_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )


ft.app(main)
