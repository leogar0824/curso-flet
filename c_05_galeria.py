"""Galeria de productos"""

import os
import base64
import flet as ft

# creear el producto


def crear_producto(nombre, precio, color, imagen_nombre):
    """crear producto"""
    # se crear el path de la carpeta y la imagen
    imagen_path = os.path.join(
        os.path.dirname(__file__), "c_05_assets", imagen_nombre
    )

    # se intenta decodificar la imagen
    try:
        with open(imagen_path, "rb") as image_file:  # CLAVE decodificar en binario con "rb"
            imagen_bytes = base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        print(
            f"Advertencia: la imagen {imagen_nombre}, no existe en {imagen_path}")
        imagen_bytes = None

    return ft.Container(
        content=ft.Column([
            ft.Image(
                src_base64=imagen_bytes,    # se toma la codificación de la imagen en base64
                width=150,
                height=150,
                fit=ft.ImageFit.CONTAIN,    # se ajusta la imagen a 150 x 150
                error_content=ft.Text("Imagen no encontrada")
            ) if imagen_bytes else ft.Text("Imagen no encontrada"),

            ft.Text(
                value=nombre,
                size=18,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Text(
                value=f"${precio}",
                size=14
            ),

            ft.ElevatedButton(
                text="Agregar al carrito",
                color=ft.Colors.WHITE
            )
        ]),
        bgcolor=color,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center
    )


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Galería de productos Responsiva"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900

    # elementos
    titulo = ft.Text(
        value="Galería de productos",
        size=32,
        weight=ft.FontWeight.BOLD,
    )

    # lista de productos llamando a la fucnión crear_producto
    productos = [
        crear_producto("Producto 1", 19.99,
                       ft.Colors.BLUE_500, "Producto1.png"),
        crear_producto("Producto 2", 29.99,
                       ft.Colors.GREEN_500, "Producto2.png"),
        crear_producto("Producto 3", 39.99,
                       ft.Colors.ORANGE_500, "Producto3.png"),
        crear_producto("Producto 4", 49.99,
                       ft.Colors.PURPLE_500, "Producto4.png"),
        crear_producto("Producto 5", 59.99,
                       ft.Colors.PINK_500, "Producto5.png"),
        crear_producto("Producto 6", 69.99,
                       ft.Colors.CYAN_500, "Producto6.png"),
        crear_producto("Producto 7", 79.99,
                       ft.Colors.YELLOW_500, "Producto7.png"),
        crear_producto("Producto 8", 89.99,
                       ft.Colors.TEAL_500, "Producto8.png"),
    ]

    # crear la galería para hacer filas responsivas
    galeria = ft.ResponsiveRow(
        [ft.Container(producto, col={"sm": 12, "md": 6, "lg": 3})
         for producto in productos],
        spacing=20,
        run_spacing=20
    )

    # contenido del page
    contenido = ft.Column(
        controls=[
            titulo,
            ft.Divider(
                height=20,
                color=ft.Colors.WHITE24,
            ),
            galeria
        ],
        scroll=ft.ScrollMode.AUTO,  # agregar scroll al contenedor
        expand=True
    )

    # page
    page.add(
        contenido
    )


ft.app(main)
