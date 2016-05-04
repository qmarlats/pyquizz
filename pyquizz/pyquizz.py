"""PyQuizz - Python blind test"""

from music import Music

def test():
    music = Music("6e759f6da358f4a36421af5006c5dbcd6ccabbdb")
    print(music.is_exists())
    music.play()

if __name__ == '__main__':
    # code if script is executed by user (and not imported from another file)
    test()
