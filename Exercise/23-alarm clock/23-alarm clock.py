# Python Alarm Clock


import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Exercise/23-alarm clock/Dua_Lipa-Physical__Remixes_-LODATO__Remix__Extended-72436644.mp3"     #sound_file is on .gitignore - zipdj tracks are not meant for sharing
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😫")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)