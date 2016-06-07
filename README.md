Site du projet : https://qmarlats.github.com/pyquizz
Documentation : https://qmarlats.github.com/pyquizz/docs

# Dépendences

PyQuizz utilise `simpleaudio` pour lire la musique, il faut installer ce module (`pip install simpleaudio` ou `pip3 install simpleaudio` si l'OS n'utilise pas Python3 par défaut) ainsi que ses dépendences ([voir ici](http://simpleaudio.readthedocs.io/en/latest/installation.html)):

* Python3 et ses paquets de développement
* ALSA et ses paquets de développement

Le projet lui-même nécessite Python 3.5+ (il ne fonctionnera pas sur Python 3.4).

# Limitations

Les limitations sont les même que `simpleaudio` ([voir ici](http://simpleaudio.readthedocs.io/en/latest/capabilities.html)), PyQuizz ne peut donc que lire :

* format WAV
* 2 canneaux (mono ou stéréo)
* 8, 11.025, 16, 22.05, 32, 44.1, 48, 88.2, 96, ou 192 kHz

# Installation

Installation sur Debian et dérivées (attention, Python 3.5+ est requis) :

* Installer les dépendences de `simpleaudio` : `sudo apt install -y python3-dev libasound2-dev`
* Installer `python3-pip`: `sudo apt install python3-pip`
* Il est recommandé d'utiliser un environnement virtuel :
  * Utiliser celui existant déjà dans le projet : `source env/bin/activate`
  * Si ce dernier ne fonctionne pas, en créer un :
    * Créer l'environnement : `virtualenv my_env`
    * Entrer dedans : `source my_env/bin/activate`
    * Installer les modules Python : `pip3 install simpleaudio wave sphinx peewee`

Sur Arch Linux :

* Python est déjà installé dans une version compatible et avec les paquets de développement (si `base-devel` est installé)
* Paquets de développement de ALSA : `sudo pacman -S alsa-libs`
* L'environnement virtuel à utiliser est `env-3` au lieu de `env`
* Si la création d'un environnement est nécessaire, il faut utiliser `pip` et non `pip3`

# Utilisation

Il faut d'abord rentrer dans l'environnement virtuel. Dans le dossier racine de PyQuizz : `source env/bin/activate` pour les systèmes utilisant Python 2 par défaut (par exemple Debian et dérivées), `source env-3/bin/activate` pour les systèmes utilisant Python 3 par défaut (par exemple Arch Linux et dérivées).

Puis dans le dossier `pyquizz`, exécuter `pyquizz.py` **avec Python3** (`python3 pyquizz.py` ou `python pyquizz.py` si l'OS utilise Python 3 par défaut).

**Bon amusement !**
