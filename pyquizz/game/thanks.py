"""
.. module:: thanks
   :platform: Linux, Windows
   :synopsis: Ask user to rate project

.. moduleauthor:: Louis Lhosmot

"""

from pyquizz import settings
from database.models import Rating

def thanks():
	""" Show thanks and ask an user rating."""

	print ("Remerciements à toute l'équipe qui à contribuée à ce projet ainsi qu'à notre professeur M. Bachard.")

	# Initialize user_input
	user_input = None

	# Ask for a rating
	while user_input is None:
		user_input = input("Votre avis nous intéresse, donnez-nous une note entre 0 et 5 svp : ")
		try:
			user_input = int(user_input)
		except ValueError:
			print(settings.errors['NOT_A_NUMBER'])

		if user_input in range(0,6):
			try:
				Rating.create(rating=user_input)
			except Exception:
				print("Impossible d'enregistrer la note.")
		else:
			user_input = None
			print("Veuillez entrer une note comprise entre 0 et 5.")
