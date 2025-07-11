"""Navigation Rail"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Mi Biblioteca personal"
    page.theme_mode = ft.ThemeMode.DARK

    # funciones
    def change_theme(e):
        """cambiar el tema"""
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        theme_icon_button.icon = ft.Icons.DARK_MODE if theme_icon_button.icon == ft.Icons.LIGHT_MODE else ft.Icons.LIGHT_MODE
        page.update()

    def destination_change(e):
        """cambiar los destinos"""
        # toma el index de la seccion seleccionada
        index = e.control.selected_index
        # borra la seccion actual de la lista de la variable contenidos al final del rail
        content.controls.clear()
        # agrega a la variable de contenidos la sección seleccionada
        if index == 0:
            content.controls.append(books_view)
        elif index == 1:
            content.controls.append(add_book_view)
        elif index == 2:
            content.controls.append(wishlist_view)
        page.update()

    def delete_book(e, book):
        """borrar libro"""
        if book in books_view.controls:
            books_view.controls.remove(book)
        elif book in wishlist_view.controls:
            wishlist_view.controls.remove(book)
        page.update()

    def add_wishlist(e, book):
        """agegar a lista de deseos"""
        wishlist_book = ft.ListTile(
            title=book.title,
            subtitle=book.subtitle,
            trailing=ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        text="Eliminar",
                        on_click=lambda e: delete_book(e, wishlist_book)
                    ),
                    ft.PopupMenuItem(
                        text="Mover a 'Mis Libros'",
                        on_click=lambda e: move_to_book_view(e, wishlist_book)
                    )
                ],
                tooltip="Mostrar menú"
            )
        )
        wishlist_view.controls.append(wishlist_book)
        if book in books_view.controls:
            books_view.controls.remove(book)
        page.update()

    def move_to_book_view(e, book):
        """mover a book_view"""
        move_book = ft.ListTile(
            title=book.title,
            subtitle=book.subtitle,
            trailing=ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        text="Eliminar",
                        on_click=lambda e: delete_book(e, move_book)
                    ),
                    ft.PopupMenuItem(
                        text="Añadir a lista deseos",
                        on_click=lambda e: add_wishlist(e, move_book)
                    )
                ],
                tooltip="Mostrar menú"
            )
        )
        books_view.controls.append(move_book)
        if book in wishlist_view.controls:
            wishlist_view.controls.remove(book)
        page.update()

    def add_book(e):
        """agregar libro"""
        # en caso de que no ingrese el título del libro
        if not title_field.value:
            # mensaje de error
            title_field.error_text = "Por favor ingresa un título"
            page.update()
            # sale de la función
            return
        # si hay valor del título
        # crear un elmento título de lista para agregar al list view de la sección
        new_book = ft.ListTile(
            # agregar el titulo con text
            title=ft.Text(value=title_field.value),
            # agregar subtitulo con text
            subtitle=ft.Text(
                value=author_field.value if author_field.value else "Autor desconocido",
            ),
            # agregar boton de opciones al final de cada titulo de la lista
            trailing=ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                # elementos del menú desplegable
                items=[
                    # elemento del menú cotextual
                    ft.PopupMenuItem(
                        text="Eliminar",
                        # funcionalidad al clikear (eliminar)
                        on_click=lambda e: delete_book(e, new_book)
                    ),
                    # tarea
                    ft.PopupMenuItem(
                        text="Añadir a lista de deseos",
                        on_click=lambda e: add_wishlist(e, new_book)
                    )
                ],
                tooltip="Mostrar menú"
            )
        )
        # agregar a la vista books_view el elemento creado
        books_view.controls.append(new_book)
        # limpiar los campos
        title_field.value = ""
        author_field.value = ""
        title_field.error_text = None
        page.update()

    # elementos
    titulo = ft.Text(
        value="Biblioteca Personal",
    )

    theme_icon_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        tooltip="Cambiar tema",
        on_click=change_theme
    )

    app_bar = ft.AppBar(
        title=titulo,
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[theme_icon_button]
    )

    # vistas
    # vista books_view
    books_view = ft.ListView(
        expand=1,
        spacing=10,
        padding=20
    )

    # vista wishlist_view
    wishlist_view = ft.ListView(
        expand=1,
        spacing=10,
        padding=20
    )

    # vista add_books_view
    title_field = ft.TextField(
        label="Título del libro",
        width=300,
    )

    author_field = ft.TextField(
        label="Autor",
        width=300
    )

    add_button_view = ft.ElevatedButton(
        text="Añadir libro",
        on_click=add_book
    )

    add_book_view = ft.Column(
        controls=[
            ft.Text(
                value="Añadir un libro",
                size=20,
                weight=ft.FontWeight.BOLD
            ),
            title_field,
            author_field,
            add_button_view
        ],
        spacing=10
    )

    # navigation rail
    rail = ft.NavigationRail(
        # selecciona el index de inicio (sección)
        selected_index=0,
        # modo en que se muestra la etiqueta de cada sección
        label_type=ft.NavigationRailLabelType.SELECTED,
        # ancho mínimo del rail
        min_width=100,
        # ancho máximo del rail
        min_extended_width=400,
        # se crean la secciones como destinos en lista
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.BOOK,
                label="Mis Libros"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD,
                label="Añadir Libo"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE,
                label="Lista de Deseos"
            )
        ],
        # cambio al seleccionar as secciones
        on_change=destination_change
    )

    # variable para ir cambiando los contenidos de cada sección
    content = ft.Column(
        controls=[
            books_view
        ],
        expand=True
    )

    # page
    page.add(
        app_bar,
        # se agrega en modo de fila el rail y el contenido(content)
        ft.Row(
            controls=[
                rail,
                ft.VerticalDivider(width=1),
                content
            ],
            expand=True
        )
    )


ft.app(main)
