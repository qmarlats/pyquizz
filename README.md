# Dependencies

PyQuizz uses `simpleaudio` to play music, so you need this package (`pip install simpleaudio`) and its dependancies ([see here](http://simpleaudio.readthedocs.io/en/latest/installation.html)):

* Python3 and its development packages
* ALSA and its development packages


# Limitations

Limitations are the same as `simpleaudio` ([see here](http://simpleaudio.readthedocs.io/en/latest/capabilities.html)), so PyQuizz can only read:

* WAV files
* 1 or 2 channels (mono or stereo)
* 8, 11.025, 16, 22.05, 32, 44.1, 48, 88.2, 96, or 192 kHz
