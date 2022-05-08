Un commanditaire vous a demandé de récupérer les données ultra secrètes d'une entreprise concurrente. Vous avez tenté plusieurs approches de recherche de vulnérabilités sur les serveurs exposés qui se sont malheureusement révélées infructueuses : les serveurs de l'entreprise ont l'air solides et bien protégés. L'intrusion physique dans les locaux paraît complexe vu tous les badges d'accès nécessaires et les caméras de surveillance.

Une possibilité réside dans l'accès distant qu'ont les employés de l'entreprise à leur portail de travail collaboratif : l'accès à celui-ci se fait via deux facteurs d'authentification, un mot de passe ainsi qu'un token physique à brancher sur l'USB avec reconnaissance biométrique d'empreinte digitale. Même en cas de vol de celui-ci, il sera difficile de l'exploiter. Installer un malware evil maid sur un laptop de l'entreprise n'est pas une option : ceux-ci sont très bien protégés avec du secure boot via TPM, et du chiffrement de disque faisant usage du token.

Mais tout espoir n'est pas perdu ! Vous profitez du voyage en train d'un des employés et de sa fugace absence au wagon bar pour brancher discrètement un sniffer USB miniaturisé sur le laptop. Vous glissez aussi une caméra cachée au dessus de son siège qui n'a pu capturer que quelques secondes. Vous récupérez la caméra et le sniffer furtivement après sa séance de travail : saurez-vous exploiter les données collectées pour mener à bien votre contrat ?

Pour obtenir le flag de X-Factor 1/2, vous devez vous logguer avec login et mot de passe. Puis avec le deuxième facteur d'authentification pour obtenir le flag pour X-Factor 2/2.

    Note : les fichiers sont les mêmes pour les deux épreuves X-Factor.

    SHA256(capture_USB.pcapng) = 1543448477f925070b598f306b59a97610ba013f7ec4aa5d6c8c2484d555525a.
    SHA256(login_password.mkv) = 0b1361a0261a2cdb13d47d4629c8ec93dc5a7e829ee778d82a7a4a14912f107a.


