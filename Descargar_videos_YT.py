#Se importa empezando la libreria yt_dlp
#si no se tiene instalada se instala con pip install yt_dlp
import yt_dlp as yt


#se hace una funcion la cual tenga todas las opciones de yt_dlp y pueda descargar
def download_video(url, formato):
    #Estas son las opciones que usaran paraa poder descargar los videos en MP4 o MP3
    if formato == 1:
        ydl_opts = {
            'format': 'bestvideo+bestaudio', #Format es para escoger el mejor en video y audio
            'outtmpl': '%(title)s.%(ext)s', #Este es para la salida al descargar el video titulo y extensión
            'merge_output_format': 'mp4', #Este es el formato al cual se va a transformar
        }
    elif formato == 2:
        ydl_opts = {
            'format': 'bestaudio', #Format es para escoger el mejor en video y audio
            'outtmpl': '%(title)s.%(ext)s', #Este es para la salida al descargar el mp3, titulo y extensión
            'postprocessors': [{
            'key': 'FFmpegAudioConvertor', #Usar FFmpeg para la mejora y convertir de forma mas eficiente
            'preferredcodec': 'mp3',  # Convierte a MP3
            'preferredquality': '320',  # Calidad de 320 kbps
        }] #Este es el formato al cual se va a transformar
        }
    else:
        print('formato no valido')
        return
    #Aqui es para que empiece la descargar
    with yt.YoutubeDL(ydl_opts) as ydl: #se llama la libreria y se le imgresa las opciones
            ydl.download([url]) #Aqui ya empieza la descarga

#Llamamos las funcion y le ingresamos un url por consola
url=input("Ingresa Url: ")
opcion=int(input('1. MP4    2.MP3\n'))
download_video(url, opcion)
print('Completado')