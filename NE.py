import pygame
import time
import threading
from PIL import Image
import pystray
from pystray import MenuItem as item

# Инициализация микшера pygame
pygame.mixer.init()

# Загрузка аудиофайла
pygame.mixer.music.load("silent.mp3")  # Замените "your_audio_file.mp3" на путь к вашему аудиофайлу

# Функция для зацикливания аудио
def play_audio_loop():
    pygame.mixer.music.play(loops=-1)  # loops=-1 означает бесконечное воспроизведение

# Запуск аудио в отдельном потоке, чтобы не блокировать основной поток
audio_thread = threading.Thread(target=play_audio_loop)
audio_thread.daemon = True  # Завершить поток, когда основной поток завершится
audio_thread.start()

# Функция для остановки аудио и выхода из программы
def quit_action(icon, item):
    pygame.mixer.music.stop()
    icon.stop()

# Загрузка изображения для значка в трее
def load_image():
    return Image.open("icon.png")  # Замените "icon.png" на путь к вашему PNG-изображению

# Создание значка в трее
icon = pystray.Icon("Noise Eater 1.0r")
icon.icon = load_image()
icon.title = "Noise Eater 1.0r"
icon.menu = pystray.Menu(
    item('Exit', quit_action)  # Добавление пункта "Quit" в меню
)

# Запуск значка в трее
icon.run()
