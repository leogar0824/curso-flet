"""Uso del grid"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Tablero de Notas Adhesivas"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.theme_mode = "light"
    page.padding = 20

    # funciones
    # crear nota nueva
    def add_note(e):
        """agregar nota"""
        new_note = create_note("Nueva nota...")
        grid.controls.append(new_note)
        page.update()

    # borrar nota
    def delete_note(note):
        """borrar nota"""
        grid.controls.remove(note)
        page.update()

    # crear el contenedor de la nota
    def create_note(text):
        """crear nota"""
        note_content = ft.TextField(
            value=text,
            multiline=True,
            bgcolor=ft.Colors.BLUE_GREY_50,
            border_radius=10
        )

        note = ft.Container(
            content=ft.Column(
                controls=[
                    note_content,
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=lambda _: delete_note(note)
                    )
                ]
            ),
            width=200,
            height=200,
            bgcolor=ft.Colors.BLUE_GREY_100,
            border_radius=20,
            padding=10
        )

        return note

    # crear grid
    grid = ft.GridView(
        expand=True,
        max_extent=220,  # ancho máximo del elemento
        child_aspect_ratio=1,   # relación de aspecto 1:1
        spacing=10,  # espaciado entre las filas del grid
        run_spacing=10,  # espaciado entre columnas
    )

    # variables
    notes = [
        "Comprar leche",
        "Llamar al médico",
        "Reunión a las 3pm"
    ]

    # elementos
    # recorre la lista de notes y cada elmento crea una nota
    for note in notes:
        grid.controls.append(create_note(note))

    # page
    page.add(
        ft.Row(
            controls=[
                ft.Text(
                    value="Mis notas adhesivas",
                    size=24,
                    weight="bold",
                    color=ft.Colors.WHITE
                ),
                ft.IconButton(
                    icon=ft.Icons.ADD,
                    icon_color=ft.Colors.WHITE,
                    on_click=add_note
                )
            ],
            # separar los elementos del Row lo máx
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        grid
    )


ft.app(main)
