import models
from random import shuffle
from music import Music

def play(category):
	# Get Category
	category = models.Category.get(id=category)
	# Convert musics from this category to a list and shuffle it
	musics_shuffle = list(category.musics)
	shuffle(musics_shuffle)

	# Generate a string with the non-shuffled list of musics
	musics_list = ""
	for music in category.musics:
		musics_list = musics_list + ("\n\t" + str(music.id) + " " + music.name)

	for i, music in enumerate(musics_shuffle):
		# Show answers list
		print("Propositions :%s\n" % musics_list)

		# Play music
		music_to_play = Music(music)
		if music_to_play.is_exists():
			music_to_play.play()

		right_answer = music.id

		user_answer = input("Votre réponse : ")
		if int(user_answer) == right_answer:
			print("votre réponse est juste")
		else:
			print("votre réponse est fausse")
		print("vous avez tapé %i c'était %i" % (int(user_answer), right_answer))
