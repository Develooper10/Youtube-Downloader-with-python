#Se importa empezando la libreria yt_dlp
#si no se tiene instalada se instala con pip install yt_dlp
import yt_dlp as yt


#se hace una funcion la cual tenga todas las opciones de yt_dlp y pueda descargar
def download_video(url):
    #Estas son las opciones que usaran paraa poder descargar los videos en MP4
    ydl_opts_mp4 = {
            'format': 'bestvideo+bestaudio', #Format es para escoger el mejor en video y audio
            'outtmpl': '%(title)s.%(ext)s', #Este es para la salida al descargar el video titulo y extensión
            'merge_output_format': 'mp4', #Este es el formato al cual se va a transformar3
        }
    #Aqui es para que empiece la descargar
    with yt.YoutubeDL(ydl_opts_mp4) as ydl: #se llama la libreria y se le imgresa las opciones
            ydl.download([url]) #Aqui ya empieza la descarga
            
#Llamamos las funcion y le ingresamos un url por consola
url=input("Ingresa Url: ")
download_video(url)