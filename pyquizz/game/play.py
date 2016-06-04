"""
.. module:: pyquizz
   :platform: Linux, Windows
   :synopsis: Functions to play blindtest itself

.. moduleauthor:: Quentin Marlats, Pierre Daudey

"""

from random import shuffle
from pyquizz import settings
from utils.numbers import reduce_id
from database.models import Category
from game.music import Music
from game.thanks import thanks
from game.score import Score

def play(category):
	""" Play the blindtest itself, save and show score and ask a rating for the project."""

	# Get Category
	try:
		category = Category.get(id=category)
	except Exception:
		print("Impossible de récupérer la catégorie dans la base de données.")

	# Execute rest of code only if category exists
	if category is not None:
		# Convert musics from this category to a list
		musics = list(category.musics)
		# Generate a shuffled list
		shuffled_musics = list(musics)
		shuffle(shuffled_musics)

		# Initialize score
		points = 0

		# Generate a string with the non-shuffled list of musics
		musics_list = ""
		for music in musics:
			musics_list = musics_list + ("\n\t%i %s" % (reduce_id(music.id), music.name))

		# Play musics one by one and ask user what music is it
		for i, music in enumerate(shuffled_musics):
			# Define the right answer
			answer = reduce_id(music.id)
			# Initialize user_input
			user_input = None

			# Show answers list
			print("Propositions :%s\n" % musics_list)

			# Play music
			music_to_play = Music(music)

			# Execute code only if the music exists
			if music_to_play is not None:
				if music_to_play.is_exists():
					music_to_play.play()

				# Ask user for the answer
				while user_input is None:
					user_input = input("Votre réponse : ")
					try:
						user_input = int(user_input)
					except ValueError:
						print(settings.errors['NOT_A_NUMBER'])

					if user_input in range(1, 11):
						if user_input == answer:
							print("Votre réponse était JUSTE.")
							points = points + 1
						else:
							print("Votre réponse était FAUSSE.")
					else:
						user_input = None
						print("Veuillez entrer un nombre entre 1 et 10.")

		# Save and show score
		score = Score(points)
		score.save()
		score.show()

		# Ask for a rating
		thanks()
