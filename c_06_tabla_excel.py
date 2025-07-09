"""Crear tabla y exportar a Excel"""

from datetime import datetime
import flet as ft
from openpyxl import Workbook


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "DataTable en Flet con Excel"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # funciones
    # agregar fila
    def agragar_fila(e):
        """agrega la fila con los datos de los textfield"""
        nueva_fila = ft.DataRow(
            cells=[  # se crea celda por celda de cada fila
                ft.DataCell(
                    ft.Text(value=str(len(data_table.rows) + 1), color=ft.Colors.WHITE)),
                ft.DataCell(
                    ft.Text(value=nombre_input.value, color=ft.Colors.WHITE)),
                ft.DataCell(
                    ft.Text(value=edad_input.value, color=ft.Colors.WHITE)),
            ]
        )
        data_table.rows.append(nueva_fila)  # se agrega la fila a la tabla
        nombre_input.value = ""
        edad_input.value = ""
        page.update()

    # guardar en excel
    def guardar_excel(e):
        """guarda la tabla en excel"""
        wb = Workbook()  # se crea el libro
        ws = wb.active  # se crea la hoja activa
        ws.title = "BBDD"   # nombre de la hoja
        ws.append(["ID", "Nombre", "Edad"])  # se crea los encabezados fila 1
        # recorrer cada fila de la tabla
        for row in data_table.rows:
            # agregar el contenido de cada celda de cada fila
            ws.append([cell.content.value for cell in row.cells])

            # obtener la fecha y hora actual con formato
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            # guardar el archivo excel con la fecha y hora actual
            nombre_archivo = f"{fecha_hora}_datos_tabla.xlsx"    # nombre
            wb.save(nombre_archivo)  # guardar

            # mostrar mensaje del archivo guardado
            snack_bar = ft.SnackBar(    # barra temporal en la ventana
                content=ft.Text(f"Datos guardados en: {nombre_archivo}")
            )
            # mostrar la snack_bar sobre todo en la ventana
            page.overlay.append(snack_bar)
            snack_bar.open = True   # mostrar la barra
            page.update()

    # elementos
    titulo = ft.Text(
        value="DataTable en Flet",
        size=24,
        color=ft.Colors.WHITE
    )

    # tabla
    data_table = ft.DataTable(
        bgcolor=ft.Colors.BLUE_GREY_700,
        border=ft.border.all(
            width=2,
            color=ft.Colors.BLUE_GREY_200
        ),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(
            width=3,
            color=ft.Colors.BLUE_GREY_200
        ),
        horizontal_lines=ft.border.BorderSide(
            width=1,
            color=ft.Colors.BLUE_GREY_400
        ),
        columns=[
            ft.DataColumn(ft.Text(value="ID", color=ft.Colors.BLUE_200)),
            ft.DataColumn(
                ft.Text(value="Nombre", color=ft.Colors.BLUE_200)),
            ft.DataColumn(
                ft.Text(value="Edad", color=ft.Colors.BLUE_200)),
        ],
        rows=[]
    )

    # campos de texto
    nombre_input = ft.TextField(
        label="Nombre",
        bgcolor=ft.Colors.BLUE_GREY_700,
        color=ft.Colors.WHITE
    )

    edad_input = ft.TextField(
        label="Edad",
        bgcolor=ft.Colors.BLUE_GREY_700,
        color=ft.Colors.WHITE
    )

    # botones
    btn_agregar = ft.ElevatedButton(
        text="Agregar",
        on_click=agragar_fila,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE
    )

    btn_guardar = ft.ElevatedButton(
        text="Guardar en Excel",
        on_click=guardar_excel,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREEN
    )

    # contenedor
    input_contaider = ft.Row(
        controls=[
            nombre_input,
            edad_input,
            btn_agregar,
            btn_guardar
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # page
    page.add(
        titulo,
        data_table,
        input_contaider
    )


ft.app(main)
