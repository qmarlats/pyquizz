def scores(score):
	print("Félicitation ! vous venez de terminer PyQuizz")
	print("Veuillez entrer les informations demandées afin d'enregistrer votre score:")

	sexe1 = "M."
	sexe2 = "Mme"
	sexe3 = "Mlle"

	sexe_input = input("Titre de civilité ?\n" "1 M.\n2 Mme\n3 Mlle")

	sexe_input = 0
	while sexe_input < 1 or sexe_input > 3:
		category_input = input("Votre choix : ")

		try:
			sexe_input = int(sexe_input)
		except ValueError:
			sexe_input = 0
			print("Veuillez entrer un nombre.")

		if sexe_input >= 1 and sexe_input <= 3:
			if int(sexe_input) == 3:
				sexe = sexe3
			elif int(sexe_input) == 2:
				sexe = sexe2
			elif int(sexe_input) == 1:
				sexe = sexe1
		else:
			print("Ce choix n'existe pas.")

	age_input = 0
	while age_input < 1:
		age_input = input("Votre choix : ")

		try:
			age_input = int(age_input)
		except ValueError:
			age_input = 0
			print("Veuillez entrer un nombre.")

		if age_input >= 1 and age_input <= 150:

		else:
			print("Ce choix n'est pas possible.")

	nom_input = input("Quel est votre prénom ? ")

	if score == 0:
		print (sexe + " " + nom + " " + age + " ans, vous avez un score de %s/10. Vous l'avez fait exprès rassurez moi ?!" % score )
	elif score <2:
	    print (sexe + " " + nom + " " + age + " ans, vous avez un score de {}/10. Vous n'êtes pas très fort, même nul! Révisez :(" .format(score))
	elif score >=2 and score <5:
	    print (sexe + " " + nom + " " + age + " ans, vous avez un score de " + str(score) + "/10 Vous n'êtes vraiment pas très fort, il faudrait sortir le soir !")
	elif score >=5 and score <7:
	    print (sexe + " " + nom + " " + age + " ans, vous avez un score de %s/10. c'est pas trop mal :)" % score )
	elif score >=7 and score <10:
	    print (sexe + " " + nom + " " + age + " ans, vous avez un score de {}/10. Vous êtes vraiment doué !" .format(score))
	elif score == 10:
	    print (sexe + " " + nom + " " + age + " ans, vous avez un score de " + str(score) + "/10. Tricheur !")


	models.Category.create(sexe = sexe)
	models.Category.create(age = age)
	models.Category.create(nom = nom)
