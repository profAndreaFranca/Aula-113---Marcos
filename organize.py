import os
import shutil
import time

from_dir = "D:/ProfAndrea/Downloads"
to_dir = "./"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#classe gerenciadora de Eventos
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)

#instanciando o objeto da classe gerenciadora de eventos
event_handler = FileMovementHandler()

#instanciando o objeto do observador
observer = Observer()

#Agendando/configurando o observador
observer.schedule(event_handler, from_dir,recursive=True)

#incializando o obsevador
observer.start()


while True:
    time.sleep(2)
    print("Executando...")