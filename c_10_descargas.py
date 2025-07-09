"""Ventana para descarga de archivos"""

import time
import flet as ft


def main(page: ft.Page):
    """maon page"""
    # atributos de la ventana
    page.title = "Simulador de Descarga"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # funciones
    def simular_descarga(e):
        """simula descarga"""
        # agrega el checkbox por cada uno en el file_list que este habilitado
        archivos_seleccionados = [
            checkbox for checkbox in file_list.controls if checkbox.value]

        # validar si se han seleccionado los checkbox
        if not archivos_seleccionados:
            txt_status.value = "Por favor, selecciona al menos un archivo"
            page.update()
            return

        # resetear los progress
        progress_bar.value = 0
        progress_ring.value = 0
        page.update()

        # toma la cantidad de MB de los archivos dividiendo el texto convirtiendo a floar y sumando
        total_size = sum([
            float(archivo.label.split("(")[1].split(" MB")[0]) for archivo in archivos_seleccionados
        ])
        downloaded = 0

        # obtener el tamaño de cada archivo y asignarle el label y el tamaño
        # de cada archivo seleccionado al txt_status
        for archivo in archivos_seleccionados:
            file_size = float(archivo.label.split("(")[1].split(" MB")[0])
            txt_status.value = f"Descargando: {archivo.label}..."

            # simulación de la descarga
            for _ in range(10):
                time.sleep(0.3)
                downloaded += file_size / 10
                progress = min(downloaded / total_size, 1)
                progress_bar.value = progress
                progress_ring.value = progress
                page.update()

        # descarga finalizada
        progress_ring.value = 1
        progress_bar.value = 1
        txt_status.value = "¡Descarga Completa!"
        page.update()

        # esperar y resetear elementos
        time.sleep(1.5)
        progress_bar.value = 0
        progress_ring.value = 0
        txt_status.value = ""
        for checkbox in file_list.controls:
            checkbox.value = False
        page.update()

    # elementos
    titulo = ft.Text(
        value="Simulador de Descarga de Archivos",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE
    )

    archivos = ft.Text(
        value="Selecciona los archivos para descargar",
        size=16,
        color=ft.Colors.WHITE70
    )

    file_list = ft.Column(
        controls=[
            ft.Checkbox(
                label="Documento.pdf (2.5 MB)",
                value=False
            ),
            ft.Checkbox(
                label="Imagen.jpg (5 MB)",
                value=False
            ),
            ft.Checkbox(
                label="Video.mp4 (50 MB)",
                value=False
            ),
            ft.Checkbox(
                label="Archivo.zip (100 MB)",
                value=False
            ),
        ]
    )

    contenedor = ft.Container(
        content=file_list,
        padding=20
    )

    progress_bar = ft.ProgressBar(
        width=400,
        color="amber",
        bgcolor="#263238",
        value=0
    )

    progress_ring = ft.ProgressRing(
        stroke_width=5,
        color="amber",
        value=0,
    )

    fila = ft.Row(
        controls=[
            progress_bar,
            progress_ring,
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    txt_status = ft.Text(
        value="",
        color=ft.Colors.WHITE
    )

    btn_descarga = ft.ElevatedButton(
        text="Iniciar Descarga",
        on_click=simular_descarga,
        bgcolor=ft.Colors.AMBER,
        color=ft.Colors.BLACK
    )

    # page
    page.add(
        titulo,
        archivos,
        contenedor,
        fila,
        txt_status,
        btn_descarga
    )


ft.app(main)
