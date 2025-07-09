"""lista de compras"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Lista de Compras"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.padding = 20

    # variables de entorno
    categories = ["Sin categoría", "Alimentos",
                  "Limpieza", "Electrónica", "Ropa",]

    # funciones
    def add_item(e):
        """agregar productos a la lista"""
        if item_input.value:
            quantity = quantity_input.value if quantity_input.value else "1"

            # establecer la categoría
            def update_category(e):
                """indicar la categoría"""
                category_text.value = f"Categoría: {e.control.value}"
                page.update()

            # lista desplegable de las categorias
            category_dropdown = ft.Dropdown(
                # agregar cada elemento de la lista categories
                options=[ft.dropdown.Option(category)
                         for category in categories],
                # valor por defecto el índice 0 de la lista categories
                value=categories[0],
                on_change=update_category,
                color=ft.Colors.AMBER,
                width=150
            )

            # etiqueta de categoría
            category_text = ft.Text(
                value=f"Categoría: {categories[0]}",
                color=ft.Colors.AMBER
            )

            # añadir el item a la lista añadiendo cada elemento del listTile
            new_item = ft.ListTile(
                # por cada elemento agregado al listtile
                leading=ft.Checkbox(
                    value=False,
                    fill_color=ft.Colors.AMBER,
                ),
                title=ft.Text(
                    value=f"{item_input.value} (x{quantity})",
                    color=ft.Colors.WHITE
                ),
                subtitle=ft.Row(
                    # fila agregando categoría y el drop
                    controls=[
                        category_text,
                        category_dropdown
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),
                # boton eliminar
                trailing=ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED_400,
                    on_click=lambda _: shopping_list.controls.remove(
                        new_item) or page.update()
                )
            )
            # agregar el nuevo item a la lista de compras
            shopping_list.controls.append(new_item)
            item_input.value = ""
            quantity_input.value = ""
            page.update()

    def clear_list(e):
        """borrar lista"""
        shopping_list.controls.clear()
        page.update()

    def show_stats(e):
        """mostrar estadísticas"""
        total_items = len(shopping_list.controls)
        # contabilizar los seleccionados
        checked_items = sum(
            1 for item in shopping_list.controls if item.leading.value
        )
        category_counts = {}
        for item in shopping_list.controls:
            # extraer la categorya del subtitulo índice 1 (dropdown)
            category = item.subtitle.controls[1].value
            # agregar categorya y conteo al diccionario de category_counts
            category_counts[category] = category_counts.get(category, 0) + 1
            # texto de estadísticas totales
            stats_text = f"Total: {total_items}, Comprados: {checked_items}, Pendientes: {total_items - checked_items}\n"
            # concatenar las estadpisticas por categoría
            stats_text += "Categorias:\n" + "\n".join(
                [f"{cat}: {count}" for cat, count in category_counts.items()]
            )
            # crear la barra snack para mostrar las estadísticas
            snack = ft.SnackBar(
                content=ft.Text(
                    value=stats_text,
                    color=ft.Colors.BLACK
                ),
                bgcolor=ft.Colors.AMBER
            )
            # mostrar snackbar por encima de todo en la page
            page.overlay.append(snack)
            snack.open = True
            page.update()

    # elementos
    titulo = ft.Text(
        value="Lista de Compras con Flet",
        size=30,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # lista de compras como columna
    shopping_list = ft.Column(
        scroll=ft.ScrollMode.AUTO
    )

    # campo del producto
    item_input = ft.TextField(
        hint_text="Añadir artículo...",
        border_color=ft.Colors.AMBER,
        color=ft.Colors.WHITE,
        width=300,
        text_align=ft.TextAlign.CENTER
    )

    # campo de la cantidad
    quantity_input = ft.TextField(
        hint_text="Cantidad",
        border_color=ft.Colors.AMBER,
        color=ft.Colors.WHITE,
        width=100,
        text_align=ft.TextAlign.CENTER
    )

    # botón para agregar el nuevo item
    add_button = ft.OutlinedButton(
        text="Añadir a la Lista",
        on_click=add_item,
        style=ft.ButtonStyle(   # mantiene el color de fondo de la page
            color=ft.Colors.AMBER,
            side=ft.BorderSide(2, ft.Colors.AMBER)
        )
    )

    # ordenar elementos input
    fila_input = ft.Row(
        controls=[
            item_input,
            quantity_input,
            add_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # boton limpiar lista
    clear_button = ft.IconButton(
        icon=ft.Icons.CLEANING_SERVICES,
        icon_color=ft.Colors.AMBER,
        tooltip="Limpiar lista",    # mensaje de ayuda en nube
        on_click=clear_list,
    )

    # botón de las estadísticas
    stats_button = ft.TextButton(
        text="Estadísticas",
        on_click=show_stats,
        style=ft.ButtonStyle(
            color=ft.Colors.AMBER
        )
    )

    # ordenar elementos de botones
    fila_botones = ft.Row(
        controls=[
            clear_button,
            stats_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # page
    page.add(
        titulo,
        fila_input,
        fila_botones,
        ft.Divider(
            height=20,
            thickness=2,
            color=ft.Colors.AMBER
        ),
        shopping_list
    )


ft.app(target=main)
