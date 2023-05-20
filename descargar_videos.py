import yt_dlp
import os

# Introducir URL que queremos descargar
url = str(input("Introduce la URL: "))

# Direccion en la que se encuentra el codigo --> donde se va a descargar el video
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configuramos las opciones de descarga para el video
video_options = {
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio/best[height<=1080][ext=mp4]/best[ext=mp4]',   # La maxima calidad de descarga es 1080 y busca el mejor audio
    'outtmpl': os.path.join(current_dir, '%(title)s'),   # Se va a guardar en la misma carpeta y con el titulo que tiene en YouTube
    '--concurrent-fragments': '4',
}

# Creamos una instancia de yt_dlp y descargamos el video y el audio de forma paralela
with yt_dlp.YoutubeDL(video_options) as ydl:
    ydl.download([url])
    
# Imprimimos un mensaje en la terminal para indicar que se ha completado la tarea
print('Descarga y combinación completas.')

'''
Este es el primer codigo que hago por voluntad propia (sin ser trabajo de la uni) porque YouTube no me dejaba descargar mis propios videos a mejor calidad de 720.

Entrar a otras paginas web externas no servia, la mayoria no descarga a 1080 y te llenan de publicidad. A parte de que los videos que queria descargar duran mas de 1 hora
y las paginas web suelen tener un limite de tiempo. 

La maxima calidad es 1080 porque mi monitor no es 4K, la mayoria de veces descarga en mkv o en mp4. De todas las pruebas una vez me ha descargado en webm, pero hay muchos
conversores que son bastante buenos. A mi de momento este codigo me sirve para poder editar mis videos y descargar sin problemas.

Si haceis algun cambio que sea importante no dudeis en decirmelo. 
'''