import os

from pathlib import Path
from pygame.mixer import Sound, music
from debugcontrols import music_off


class MusicLib:
    music_path = Path(os.path.abspath(os.path.join((os.path.dirname(__file__)), '..', 'music',)))
    currently_playing = None

    @classmethod
    def play_race_start(cls):
        if not cls.currently_playing == 'race_start':
            music.load(str(cls.music_path / 'race_start.wav'))
            if not music_off:
                music.play(-1)
            cls.currently_playing = 'race_start'

    @classmethod
    def play_game(cls):
        if not cls.currently_playing == 'title':
            music.load(str(cls.music_path / 'race_audio.wav'))
            if not music_off:
                music.play(-1)
            cls.currently_playing = 'title'

    @classmethod
    def update_volume(self, volume):
        music.set_volume(volume)
        if volume <= 0.05:
            self.currently_playing = None


class SoundLib:
    sound_path = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sounds', )))

    @classmethod
    def woodblock(cls):
        sound = Sound(str(cls.sound_path / 'woodblock.wav'))
        sound.play()

    @classmethod
    def chime(cls):
        sound = Sound(str(cls.sound_path / 'chime.wav'))
        sound.play()

    @classmethod
    def winsound(cls, file):
        sound = Sound(str(cls.sound_path / file))
        sound.play()

