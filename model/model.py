import pygame
import threading

class Mp3Player():
    def __init__(self):
        pygame.mixer.init()
        
    def play_song(self, song_name):
        
        def play_audio(song_name):
            pygame.mixer.music.load(song_name)
            pygame.mixer.music.play()
            
            
        if song_name != None:  
            try:
                play_audio(song_name)
                return (None, )
            except pygame.error as e:
                print(e)
                return 'No se puede reproducir el partido', e
        
        else:
            return (None, )
    # def thread_song(self, song_name):
        # audio_thread = threading.Thread(group=None, target=self._play_song, name=None, args=(song_name,) )
        # audio_thread.start()