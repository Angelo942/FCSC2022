La société MegaSecure mets à disposition un serveur sécurisé permettant de lancer des opérations tout en maîtrisant la consommation énergétique de ce dernier.

Le serveur permet d'exécuter des commandes de manière sécurisée. En effet, il repose sur un composant sécurisé afin de vérifier la signature de toute commande reçue avant de l'exécuter.

Le code Python équivalent à la signature est le suivant :

def sign(self, m):
    return pow(int(sha256(m), 16), self.d, self.N)

et la vérification est faite de la manière suivante :

def verif(self, m, s):
    return int(sha256(m), 16) == pow(int(s), self.e, self.N)

Néanmoins, étant en phase de test seules deux commandes (ls -la flag.txt et cat flag.txt) sont disponibles. Par ailleurs, il a été remarqué que le serveur présente des comportements étranges dans certaines configurations.
