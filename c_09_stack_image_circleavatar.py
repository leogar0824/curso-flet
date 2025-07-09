"""Uso dels Stack - Image - CircleAvatar"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de ventana
    page.title = "Demostraci+on de Stack, Image y CircleAvattar"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"

    # funciones
    def create_example(title, description, content):
        """base del contenedor para reuso"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value=title,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_200
                    ),
                    ft.Text(
                        value=description,
                        color=ft.Colors.GREY_300
                    ),
                    ft.Container(
                        content=content,
                        padding=10,
                        border=ft.border.all(
                            width=1,
                            color=ft.Colors.BLUE_400
                        )
                    )
                ]
            ),
            margin=ft.margin.only(bottom=20)
        )

    # elementos
    txt_titulo = ft.Text(
        value="Stack - Image - CircleAvatar",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_200
    )

    # stack
    stack_ejemplo = ft.Stack(
        controls=[
            ft.Container(
                width=200,
                height=200,
                bgcolor=ft.Colors.BLUE_900
            ),
            ft.Container(
                width=150,
                height=150,
                bgcolor=ft.Colors.ORANGE_700,
                left=25,
                top=25
            ),
            ft.Container(
                width=100,
                height=100,
                bgcolor=ft.Colors.GREY_700,
                left=50,
                top=50
            ),
            ft.Text(
                value="Stack Demo",
                size=12,
                color=ft.Colors.WHITE,
                left=70,
                top=90
            )
        ],
        width=200,
        height=200
    )

    stack_example = create_example(
        title="Stack",
        description="Stack permite superponer widgets uno encima de otro",
        content=stack_ejemplo
    )

    # imagen
    imagen_internet = ft.Image(
        src="https://picsum.photos/200/200",
        width=200
    )

    imagen_local = ft.Image(
        src="c_09_images/imagen.jpg",   # usar / o \\ para el path
        width=200
    )

    columna_imagen = ft.Column(
        controls=[
            imagen_internet,
            ft.Text(
                value="Tmagen desde URL",
                size=14,
                color=ft.Colors.GREEN_300
            ),
            imagen_local,
            ft.Text(
                value="Imagen local (si está disponible)",
                size=14,
                color=ft.Colors.GREY_300
            )
        ]
    )

    imagen_example = create_example(
        title="Image",
        description="Image permite mostrar imágenes desde diversas fuentes",
        content=columna_imagen
    )

    # CircleAvatar
    avatar_imagen = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/0000005",
        radius=80
    )

    avatar_texto = ft.CircleAvatar(
        content=ft.Text(
            value="LG",
            color=ft.Colors.BLUE_GREY_800,
        ),
        radius=80,
        bgcolor=ft.Colors.BLUE_200
    )

    fila_avatars = ft.Row(
        controls=[
            avatar_imagen,
            avatar_texto
        ]
    )

    avatar_example = create_example(
        title="CircleAvatar",
        description="CircleAvatar crea un avatar circular, útil para perfiles de usuario",
        content=fila_avatars
    )

    # divider
    separador = ft.Divider(
        height=1,
        color=ft.Colors.GREY_400
    )

    # page
    page.add(
        txt_titulo,
        separador,
        stack_example,
        separador,
        imagen_example,
        separador,
        avatar_example
    )


ft.app(main)
