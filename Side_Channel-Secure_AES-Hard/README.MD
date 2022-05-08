Nous avons accès à un serveur qui permet de chiffrer des messages aléatoires en utilisant l'algorithme AES. Comme ce serveur à été utilisé pour chiffrer des messages importants, nous souhaitons récupérer la clé de chiffrement. Notre expert en attaques par faute a mis au point un système permettant d'injecter des fautes dans l'état interne de l'AES. Malheureusement, la puce sécurisée assurant le chiffrement possède une implémentation redondée de l'AES et nous sommes capables de ne fauter qu'une seule instance à la fois comme présenté sur le schéma suivant :

      Msg
       |
  +----+----+
  |         |
  v         v
+---+     +---+
|AES|     |AES|<--Faute
+---+     +---+
  |         |
  | +-----+ |
  +-| ==? |-+
    +-----+
       |
       v
      Res

De fait, les fautes sont détectées. Néanmoins, notre expert est formel : il devrait être possible de retrouver la clé en utilisant une attaque SIFA (pour Statistically Ineffective Fault Attack). Il a d'ailleurs implémenté une interface qui permet de cibler précisément quel octet de l'état interne de l'AES fauter lorsqu'on demande au serveur de chiffrer un message selon l'indexation suivante :

+--+--+--+--+
| 0| 4| 8|12|
+--+--+--+--+
| 1| 5| 9|13|
+--+--+--+--+
| 2| 6|10|14|
+--+--+--+--+
| 3| 7|11|15|
+--+--+--+--+

Il nous informe néanmoins qu'il n'est pas possible d'obtenir plus de 200 chiffrés. Enfin, l'expert avertit qu'une telle attaque peut nécessiter plusieurs heures de calcul.

Notre objectif est de déchiffrer le message que le serveur nous envoie lorsque l'on s'y connecte.
