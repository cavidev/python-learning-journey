from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(self.command)

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            # print(f'{event.src_path} ha sido modificado, reiniciando...')
            self.start_process()


if __name__ == "__main__":
    # Ruta del directorio a monitorear
    path = Path(Path(__file__).parent.parent)
    # Reemplaza 'tu_script.py' con tu archivo Python
    command = ['python', 'Day 6/__main__.py']
    event_handler = ChangeHandler(command)
    print(event_handler)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
