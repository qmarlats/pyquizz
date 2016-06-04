"""
.. module:: scores
   :platform: Linux, Windows
   :synopsis: Functions to play blindtest itself

.. moduleauthor:: Benjamin Mitifiot, Charly Adam

"""

from pyquizz import settings
from database.models import Score as ScoreModel

class Score(object):
	def __init__(self, score):
		"""Create a Score object.

		:returns:  Score

		"""

		self.score = score
		self.gender = None
		self.age = None
		self.name = None
		self.update_user()

	def update_user(self):
		"""Update user informations. Must be executed at least once when a Score object is created."""

		print("Pour enregistrer votre score, renseignez les informations demandées ci-dessous.\nRemarque : ces informations permettent de réaliser des statistiques et vous permettrons également de retrouver vos scores.")

		genders = ["M.", "Mme", "Mlle"]

		print("Veuillez choisir votre sexe :\n1 M.\n2 Mme\n3 Mlle\n")
		user_input = None
		while user_input is None:
			user_input = input("Votre sexe : ")
			try:
				user_input = int(user_input)
			except ValueError:
				print(settings.errors['NOT_A_NUMBER'])

			if user_input in range(1,4):
				self.gender = genders[user_input - 1]
			else:
				user_input = None
				print(settings.errors['CHOICE_NOT_EXISTS'])

		user_input = None
		while user_input is None:
			user_input = input("Votre âge : ")

			try:
				user_input = int(user_input)
			except ValueError:
				print(settings.errors['NOT_A_NUMBER'])

			if user_input in range(1, 151): # On ne sait jamais, peut-être que d'ici quelques années on vivera jusqu'à 150 ans
				self.age = user_input
			else:
				user_input = None
				print("Vous n'avez probalement ni moins de 1 an, ni plus de 150 ans.")

		user_input = None
		while user_input is None:
			user_input = input("Votre nom : ")

			if len(user_input) <= 30: # On ne sait jamais, peut-être que d'ici quelques années on vivera jusqu'à 150 ans
				self.name = user_input
			else:
				user_input = None
				print("Votre nom ne fait probablement pas plus de 30 caractères... Si c'est le cas, désolé pour vous.")

	def save(self):
		"""Save user informations and score in database."""

		if (self.name or self.gender or self.age or self.score) is not None:
			try:
				ScoreModel.create(name = self.name, gender = self.gender, age = self.age, score = self.score)
			except:
				print("Impossible d'enregistrer le score dans la base de données.")
		else:
			print("Informations sur l'utilisateur incomplètes.")

	def show(self):
		"""Show score with a message."""

		if self.score == 0:
			print("%s, %s, %i ans, vous avez un score de %i/10. Vous l'avez fait exprès rassurez-nous ?!" % (self.gender, self.name, self.age, self.score))
		elif self.score == 1:
			print("%s, %s, %i ans, vous avez un score de %i/10. Vous n'êtes pas très fort, même nul ! Révisez :(" % (self.gender, self.name, self.age, self.score))
		elif self.score in range(2, 5):
			print("%s, %s, %i ans, vous avez un score de %i/10. Vous n'êtes vraiment pas très fort, il faudrait sortir le soir !" % (self.gender, self.name, self.age, self.score))
		elif self.score in range(5, 7):
			print("%s, %s, %i ans, vous avez un score de %i/10. C'est pas trop mal :)" % (self.gender, self.name, self.age, self.score))
		elif self.score in range(7, 10):
			print("%s, %s, %i ans, vous avez un score de %i/10. Vous êtes vraiment doué !" % (self.gender, self.name, self.age, self.score))
		elif self.score == 10:
			print("%s, %s, %i ans, vous avez un score de %i/10. Tricheur !" % (self.gender, self.name, self.age, self.score))
		else:
			print("Hum... On va dire que vous avez un score de 10/10... :-°")
