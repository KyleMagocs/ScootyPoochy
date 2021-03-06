import os

from pathlib import Path
from pygame.mixer import Sound, music
from debugcontrols import music_off


class MusicLib:
    music_path = Path(os.path.abspath(os.path.join((os.path.dirname(__file__)), '..', 'music',)))
    currently_playing = None

    @classmethod
    def play_race_start_old(cls):
        if not cls.currently_playing == 'race_start_old':
            music.load(str(cls.music_path / 'RaceTheme.wav'))
            if not music_off:
                music.play(-1)
            cls.currently_playing = 'race_start_old'

    @classmethod
    def play_race_start(cls):
        if not cls.currently_playing == 'race_start':
            music.load(str(cls.music_path / 'RaceTheme_mt.wav'))
            MusicLib.update_volume(.75)
            if not music_off:
                music.play(-1)
            cls.currently_playing = 'race_start'


    @classmethod
    def play_title(cls):
        if not cls.currently_playing == 'title':
            music.load(str(cls.music_path / 'poochhopLoopableMixdown.wav'))
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
    def score1(cls):
        sound = Sound(str(cls.sound_path / 'score1.wav'))
        sound.play()
    @classmethod
    def score2(cls):
        sound = Sound(str(cls.sound_path / 'score2.wav'))
        sound.play()
    @classmethod
    def score3(cls):
        sound = Sound(str(cls.sound_path / 'score3.wav'))
        sound.play()

    @classmethod
    def winchime(cls):
        sound = Sound(str(cls.sound_path / 'score4.wav'))
        sound.play()


    @classmethod
    def playsound(cls, file, volume = 1):
        sound = Sound(str(cls.sound_path / file))
        sound.set_volume(volume)
        sound.play()


