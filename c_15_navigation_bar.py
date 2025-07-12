"""Navigation Bar"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "NavigationBar Example"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.window.center()
    page.window.width = 400

    # funciones

    def on_navigation_change(e):
        """cambio en la navegación"""
        selected_index = e.control.selected_index
        if selected_index == 0:
            show_home()
        elif selected_index == 1:
            show_search()
        elif selected_index == 2:
            show_settings()
        page.update()

    def show_home():
        """mostrar page home"""
        page.controls.clear()
        counter.value = f"Contador = {counter_value}"
        page.add(
            navigation_bar,
            counter,
            btn_increment,
            btn_decrement
        )

    def increment_counter(e):
        """aumentar contador"""
        nonlocal counter_value
        counter_value += 1
        counter.value = f"Contador = {counter_value}"
        page.update()

    def decrement_counter(e):
        """aumentar contador"""
        nonlocal counter_value
        counter_value -= 1
        counter.value = f"Contador = {counter_value}"
        page.update()

    def search_text(e):
        """mostrar valor del input"""
        search_output.value = f"Texto ingresado: {search_input.value}"
        page.update()

    def show_search():
        """mostrar page search"""
        page.controls.clear()
        search_input.value = ""
        search_output.value = ""
        page.add(
            navigation_bar,
            search_input,
            btn_search,
            search_output
        )

    def reset_brillo(e):
        """resetear el slider"""
        brillo_bar.value = 50
        page.update()

    def show_settings():
        """mostrar page settings"""
        page.controls.clear()
        brillo_bar.value = 50
        page.add(
            navigation_bar,
            brillo_bar,
            btn_reset_brillo
        )

        # elementos
    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_navigation_change,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Home"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SEARCH,
                label="Search"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS,
                label="Settings"
            ),
        ],
        bgcolor=ft.Colors.BLUE_GREY_900,
        indicator_color=ft.Colors.AMBER
    )

    # elementos de la vista home
    counter = ft.Text(
        value="Contador = 0",
        size=30,
        color=ft.Colors.WHITE
    )

    counter_value = 0

    btn_increment = ft.ElevatedButton(
        text="Increment",
        on_click=increment_counter
    )

    btn_decrement = ft.ElevatedButton(
        text="Decrement",
        on_click=decrement_counter
    )

    # elementos de la vista search
    search_input = ft.TextField(
        label="Introduce el texto"
    )

    search_output = ft.Text(
        value="",
        size=20,
        color=ft.Colors.WHITE
    )

    btn_search = ft.ElevatedButton(
        text="Search",
        on_click=search_text
    )

    # elementos de la vista settings
    brillo_bar = ft.Slider(
        min=0,
        max=100,
        value=50,
        label="Brillo"
    )

    btn_reset_brillo = ft.ElevatedButton(
        text="Reset",
        on_click=reset_brillo
    )

    # page
    page.add(
        navigation_bar
    )
    show_home()


ft.app(main)
