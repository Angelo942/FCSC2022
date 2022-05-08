Myster Mask a conçu une implémentation qui craint un max !

Vous allez devoir analyser les traces de consommation d'un début d'implémentation de l'AES faite par Myster Mask. Saurez-vous exploiter ces traces pour faire la différence ?

La partie à cibler correspond à l'étape d'inversion présente dans le calcul de la boîte S dans le premier tour de l'AES. Seule cette étape est implémentée, il n'est pas necessaire de connaître l'AES puisque ce challenge est spécifiquement centré sur l'étape d'inversion.

Les traces de consommation fournies dans le fichier traces.npz à charger avec numpy correspondent à la ligne suivante dans le code myster_mask.py :

masked_inversion(L)

Attention, en tant que bon détective, Myster Mask a protégé cette inversion en faisant honneur à son nom. À vous de jouer !
