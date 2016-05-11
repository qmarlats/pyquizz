# Benjamin

metal = "a1"
electro = "a2"
variete_française = "a3"
annees_80 = "a4"


score = 20

if score <5:
    print ("Vous avez un score de {}/20. Vous êtes nul! :(" .format(score))
elif score >=5 and score <10:
    print ("Vous avez un score de " + str(score) + "/20 Vous n'êtes vraiment pas très fort, il faut sortir le soir !")
elif score >=10 and score <15:
    print ("Vous avez un score de %s/20 c'est pas trop mal :)" % score )
elif score >=15 and score <20:
    print ("Vous avez un score de {}/20. Vous êtes vraiment doué !" .format(score))
elif score == 20:
    print ("Vous avez un score de " + str(score) + "/20 Epèce de tricheur")
