"""Menú con pestañas"""

import random as rd
import flet as ft


def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Tabs en Flet"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # pestaña tareas
    def generar_tareas():
        """tareas"""
        tareas = ["Hacer las compras", "Llamar al médico", "Estudiar para el Exámen,"
                  "Hacer ejersicio", "Leer un libro", "Preparar la cena"]
        # sample escoge random sin repetir y cuantos kieres choise si repite
        return rd.sample(population=tareas, k=4)

    lista_tareas = ft.ListView(spacing=10)

    def actualizar_tareas():
        """actualiza tareas"""
        lista_tareas.controls.clear()   # limpia el control del listview
        # renueva la lista de tareas
        for tarea in generar_tareas():  # por cada tarea del retorno de generar tareas
            lista_tareas.controls.append(   # agrega la tarea a lista tareas
                ft.Text(
                    value=tarea,
                    color=ft.Colors.WHITE
                )
            )
        page.update()

    # ejecutar al abrir la ventana
    actualizar_tareas()

    btn_actualizar = ft.ElevatedButton(
        text="Actualizar tareas",
        on_click=lambda _: actualizar_tareas(),
    )

    # contenido
    contenido_tareas = ft.Container(
        content=ft.Column(
            controls=[
                lista_tareas,
                btn_actualizar
            ],
            spacing=10
        ),
        padding=20,
    )

    # pestaña perfil
    txf_nombre = ft.TextField(
        label="Nombre",
        bgcolor=ft.Colors.BLUE_GREY_700,
    )

    txf_email = ft.TextField(
        label="E-mail",
        bgcolor=ft.Colors.BLUE_GREY_700
    )

    btn_guardar = ft.ElevatedButton(
        text="Guardar perfil"
    )

    contenido_perfil = ft.Container(
        content=ft.Column(
            controls=[
                txf_nombre,
                txf_email,
                btn_guardar
            ],
            spacing=10
        ),
        padding=20
    )

    # pestaña configuración
    switch_notificaciones = ft.Switch(
        label="Notificaciones",
        value=True
    )

    slider_volumen = ft.Slider(
        min=0,
        max=100,
        divisions=10,
        label="Volumen"
    )

    contenido_configuraciones = ft.Container(
        content=ft.Column(
            controls=[
                switch_notificaciones,
                slider_volumen
            ],
            spacing=10
        ),
        padding=20
    )

    # ventana
    # elementos
    titulo = ft.Text(
        value="Ejemplo de Tabs en Flet",
        size=24,
        color=ft.Colors.WHITE
    )

    # pestañas
    tabs = ft.Tabs(
        selected_index=0,   # indica el indice de la pestaña seleccionada al iniciar
        animation_duration=1000,  # duración de la ransición entre pestañas
        tabs=[  # pestañas
            ft.Tab(
                text="Tareas",
                icon=ft.Icons.LIST_ALT,
                content=contenido_tareas
            ),
            ft.Tab(
                text="Perfil",
                icon=ft.Icons.PERSON,
                content=contenido_perfil,
            ),
            ft.Tab(
                text="Configuración",
                icon=ft.Icons.SETTINGS,
                content=contenido_configuraciones
            )
        ],
        expand=1,
    )

    # page
    page.add(
        titulo,
        tabs
    )


ft.app(main)
