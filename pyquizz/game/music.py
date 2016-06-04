#!/usr/bin/env python

"""
.. module:: music
   :platform: Linux, Windows
   :synopsis: A module to use Music objects.

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

import os, wave, simpleaudio
from pyquizz import settings

class Music(object):
    def __init__(self, music):
        """Create a Music object.

        :param music: music identifier
        :type music: str
        :returns:  Music

        """

        self.music = music

    def is_exists(self):
        """Check if music file exists in music repository.

        :returns:  bool

        """

        return os.path.isfile("%s/%s.wav" % (settings.MUSICS_DIR, self.music.name))

    def play(self):
        """Play a music.

        :raises KeyboardInterrupt: if user stops the music with his keyboard (by pressing Ctrl-C for example)

        """

        try:
            # Open music file
            wave_file = wave.open("%s/%s.wav" % (settings.MUSICS_DIR, self.music.name), 'rb')

            # Create variables
            audio_data = wave_file.readframes(wave_file.getnframes())
            n_channels = wave_file.getnchannels()
            bytes_per_sample = wave_file.getsampwidth()
            sample_rate = wave_file.getframerate()
            music = simpleaudio.play_buffer(audio_data, n_channels, bytes_per_sample, sample_rate)

            # Play music
            music.wait_done()
        except (KeyboardInterrupt):
            print("Musique arrêtée par l'utilisateur.")
            # Stop music when pressing "Ctrl-C"
            music.stop()
        except:
            print("Impossible de lire la musique.")
