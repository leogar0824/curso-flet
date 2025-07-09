"""Lista de tareas"""

import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Mi lista de Tareas"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # funciones
    # agregar tarea
    def agregar_tarea(e):
        """agrega las tareas"""
        if campo_tarea.value:
            tarea = ft.ListTile(
                title=ft.Text(campo_tarea.value),
                leading=ft.Checkbox(on_change=seleccionar_tarea)
            )
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()

    # seleccionar tareas
    def seleccionar_tarea(e):
        """seleccionar tarea"""
        # agregar el titulo de cada tarea en tareas si se habilita el check
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        # cambiar el texto de tareas seleccionadas
        tareas_seleccionadas.value = "Tareas seleccionadas: " + \
            ", ".join(seleccionadas)
        page.update()

    # actualiza la lista
    def actualizar_lista():
        """actualiza la lista"""
        lista_tareas.controls.clear()   # limpia la lista
        lista_tareas.controls.extend(tareas)  # agrega el lista de las tareas
        page.update()

    # elementos
    # titulo de la page
    titulo = ft.Text(
        value="Mi lista de Tareas con Flet",
        size=30,
        weight=ft.FontWeight.BOLD,
    )

    # campo donde se escribe la tarea
    campo_tarea = ft.TextField(
        hint_text="Esribe una nueva tarea..."
    )

    # boton para agregar la tarea
    boton_agregar = ft.FilledButton(
        text="Agregar tarea",
        on_click=agregar_tarea
    )

    # lista de las tareas
    lista_tareas = ft.ListView(
        expand=1,
        spacing=3
    )

    # lista de tareas vacía para ir agregando
    tareas = []

    # label que muestra las tareas que se van seleccionando
    tareas_seleccionadas = ft.Text(
        value="",
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    # page
    page.add(
        titulo,
        campo_tarea,
        boton_agregar,
        lista_tareas,
        tareas_seleccionadas,
    )


ft.app(main)
