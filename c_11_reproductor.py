"""Reproductor de música"""

import os
import asyncio  # librería para trabajar con funciones asincronas
import flet as ft
import pygame as pg
from mutagen.mp3 import MP3

# async es una función que procesa los datos requeridos en segundo plano
# sin interferir o pausar la ejeción principal de la app
# en este caso se carga la canción mientras se ejecuta la reproducción

# clases


class Song():
    """clase canción"""

    def __init__(self, filename):
        self.filename = filename
        # separa el título de la extención
        self.title = os.path.splitext(filename)[0]
        # llama a una función de lla misma clase
        self.duration = self.get_duration()

    def get_duration(self):
        """obtener duración"""
        # indicar el path de la canción
        audio = MP3(os.path.join("c_11_Musica", self.filename))
        return audio.info.length


async def main(page: ft.Page):
    """main page"""
    # propiedades de la ventana
    page.title = "Reproductor de Música"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20

    # funciones
    def load_song():
        """carga la canción"""
        # carga la canción ubicada en la lista playlist en el índice current_song¿g_index
        pg.mixer.music.load(
            os.path.join("c_11_Musica",
                         playlist[current_song_index].filename)
        )

    def play_pause(e):
        """play/pause"""
        # si se esta reproduciendo una canción pausar y cambiar el icono
        if pg.mixer.music.get_busy():
            pg.mixer.music.pause()
            play_button.icon = ft.Icons.PLAY_ARROW
        else:
            # si el tiempo de reproduccion es -1 llamar a la función
            # load_song() para cargar la primera canción y reproducila
            if pg.mixer.music.get_pos() == -1:
                load_song()
                pg.mixer.music.play()
            else:
                # la canción estaba en pausa y se despausa
                pg.mixer.music.unpause()
            play_button.icon = ft.Icons.PAUSE
        page.update()

    def change_song(delta):
        """cambiar la canción"""
        # llamado a varible no local
        nonlocal current_song_index
        # cambiar el valor del índice de la canción actual mas el delta adelantar atrazar (+1 o -1)
        # % len(listplay) mantiene el índice dentro de la cantidad de elemento de la lista
        # y para ir a la última canción en caso de retroceder en la primera
        current_song_index = (current_song_index + delta) % len(playlist)
        # cargar la canción con el índice actualizado
        load_song()
        # reproducir la canción actual
        pg.mixer.music.play()
        # actualizar la info de la canción
        update_song_info()
        # cambiar el ícono del botón play/pause
        play_button.icon = ft.Icons.PAUSE
        page.update()

    # actualizar la info de la canción cargada

    def update_song_info():
        """actializar la info de la canción"""
        # asignar al valor song la canción del playliste en el indice actual
        song = playlist[current_song_index]
        # cambiar el valor de la etiqueta de la canción por el titulo del song
        song_info.value = f"{song.title}"
        # cambiar la etiqueta de duración por la duración de la canción con formato
        duration.value = format_time(song.duration)
        # reiniciar la barra y el currente time de la canción
        progress_bar.value = 0.0
        current_time_text.value = "00:00"
        page.update()

    def format_time(seconds):
        """dar formato al tiempo"""
        # dividir los segundos totales en min y segudos dividiendo / 60 tomando los int
        minutes, seconds = divmod(int(seconds), 60)
        # retornar en formato de tiempo
        return f"{minutes:02d}:{seconds:02d}"

    # función asincrona porque mientras se reproduce el mizer se actualizarpa la barra
    async def update_progress():
        """actializar progreso"""
        # ejecutarce mientras siempre
        while True:
            # si se está reproduciendo un canción
            if pg.mixer.music.get_busy():
                # dividir la pocisión actual de la canción / 1000 porque es en milisegundos
                current_time = pg.mixer.music.get_pos() / 1000
                # rellenar la barra con la pocición actual
                progress_bar.value = current_time / \
                    playlist[current_song_index].duration
                # actualizar la etiqueta del tiempo actual aplicandole formato
                current_time_text.value = format_time(current_time)
                page.update()
            # realizar este proceso cada segundo con una espera asincrona
            await asyncio.sleep(1)

    # inicializar el reproductor de pygame
    pg.mixer.init()

    # crear una playlist recorriendo todos los archivos de la carpeta si es que terminan en .mp3
    # el cpodigo comentado permite identificar si los archivos mp3 estan correctamente codificados
    # playlist = []
    # for f in os.listdir("c_11_Musica"):
    #     if f.lower().endswith("mp3"):
    #         try:
    #             song = Song(f)
    #             playlist.append(song)
    #             print(
    #                 f"Canción añadida: {f} Duración: {song.duration:.2f} seg")
    #         except Exception as e:
    #             print(f"Error con el archivo {f}: {str(e)}")
    playlist = [Song(f) for f in os.listdir(
        "c_11_Musica") if f.lower().endswith("mp3")]

    # crear un index para cada canción e identificarla como la canción actual
    current_song_index = 0

    # elementos
    # etiqueta para la info de la canción
    song_info = ft.Text(
        size=20,
        color=ft.Colors.WHITE
    )

    # etiqueta para el tiempo transcurrido
    current_time_text = ft.Text(
        value="00:00",
        color=ft.Colors.WHITE60
    )

    # etiqueta duración de la canción
    duration = ft.Text(
        value="00:00",
        color=ft.Colors.WHITE60
    )

    # barra de progreso para la canción
    progress_bar = ft.ProgressBar(
        value=0.0,
        width=300,
        color="white",
        bgcolor="red"
    )

    # botones de reproducción
    play_button = ft.IconButton(
        icon=ft.Icons.PLAY_ARROW,
        on_click=play_pause,
        icon_color=ft.Colors.WHITE
    )
    next_button = ft.IconButton(
        icon=ft.Icons.SKIP_NEXT,
        # función lambda porque se entregan parámetros
        on_click=lambda _: change_song(1),
        icon_color=ft.Colors.WHITE
    )
    prev_button = ft.IconButton(
        icon=ft.Icons.SKIP_PREVIOUS,
        # función lambda porque se entregan parámetros
        on_click=lambda _: change_song(-1),
        icon_color=ft.Colors.WHITE
    )

    # organizar los botones en una fila
    controls = ft.Row(
        controls=[
            prev_button,
            play_button,
            next_button
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # organizar el reproductor
    fila_reproductor = ft.Row(
        controls=[
            current_time_text,
            progress_bar,
            duration
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # agrupar los elementos ya organizados
    columna = ft.Column(
        controls=[
            song_info,
            fila_reproductor,
            controls
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # page
    page.add(
        columna
    )

    # si la plaulist no está vacía actualizar la info de la canción
    if playlist:
        load_song()
        update_song_info()
        page.update()
        # se utiliza await porque se llama a una función asincrona
        await update_progress()
    else:
        song_info.value = "no se encontraron canciones en la carpeta del origen"
        page.update()

ft.app(main)
