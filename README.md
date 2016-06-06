# Dependencies

PyQuizz uses `simpleaudio` to play music, so you need this package (`pip install simpleaudio`) and its dependencies ([see here](http://simpleaudio.readthedocs.io/en/latest/installation.html)):

* Python3 and its development packages
* ALSA and its development packages

# Limitations

Limitations are the same as `simpleaudio` ([see here](http://simpleaudio.readthedocs.io/en/latest/capabilities.html)), so PyQuizz can only read:

* WAV files
* 1 or 2 channels (mono or stereo)
* 8, 11.025, 16, 22.05, 32, 44.1, 48, 88.2, 96, or 192 kHz

# Installation tutorial

An example of installation on Debian based distros:

* Install simpleaudio dependencies : `sudo apt install -y python3-dev libasound2-dev`
* Install `python3-pip`: `sudo apt install python3-pip`
* You should use a virtualenv:
 * Use the existing one: `source env/bin/activate`
 * If not working, create one:
   * Create the env: `virtualenv my_env`
   * Use it: `source my_env/bin/activate`
   * Install required packages: `pip install simpleaudio wave sphinx peewee`

# Usage

In `pyquizz` folder, run `pyquizz.py` **with Python3** (`python3 pyquizz.py`), the play.
