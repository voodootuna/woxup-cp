# -*- coding: latin-1 -*-
import random
mot_clef_list = {"electricien" : """Installation électrique
Chauffe-eau électrique
Dépannage électrique
Mise aux normes NF
Rénovation électrique
Chauffage électrique
Réparation électrique
Panne totale électricité
Armoire et tableau électrique
Tous travaux d'électricité
Devis électricité
Dépanneur électricien
Urgence électricien
Installation électricité
Réparation électricité
Dépannage électricité
Installation courant-faible
Réparation électrique
Installation électrique
Dépannage haute-tension
Remise aux normes électrique
Chauffage électrique
Panne électrique
Chauffe-eau électrique
Dépannage basse-tension
Recherche de court-circuit
Artisan électricien
Electricien pas cher
Electricien
""", 
"plombier" : """Plomberie
Dépannage plomberie
Plomberie chauffage
Plomberie sanitaire
Plombier
Plombier chauffagiste
Plombier paris
Plombiers
Artisan plombier
Dépannage plomberie
Remplacement sanitaires
Fuites d'eau
Eviers bouchés
Remplacement broyeur
Débouchage
Dégorgement canalisations
Réfection évacuation d'eau
Dépannage chauffe-eau
WC bouchés
Pose de robinetterie
Inspection par vidéo des canalisations
Entretien canalisations
Dépannage Broyeurs
Inspection des canalisations
Dégorgement WC
Détection de fuites
Débouchage éviers
Recherche de fuites d'eau
Remplacement tout type de joints
Remplacement lavabos
Installation de sanitaires
Réparation de chasse d'eau
Débouche canalisation
Dépanneur plombier
Tous travaux de plomberie
Plomberie ile de France
Assainissement canalisation
Déboucher des toilettes
Installation de cuisine
Plombier tarif
Vidange assainissement
Déboucher une canalisation
Déboucher des canalisations
Débouchage évier
Débouchage tuyauterie
Installation sanitaire
Dégorgement domestique
Mise en conformité plomberie
Prix plombier
Assainissement ile de France
Déboucher baignoire
Déboucher canalisations
Remplacement de joint
Urgence plombier
Dégorgement canalisation
Le plombier
Débouchage WC
Déboucheur WC
Assainissement
Détartrage canalisation
Déboucheur canalisations
Déboucher WC
Installation robinetterie
Déboucher un évier
Dégorgement
Dépannage plomberie
""", 
"chauffagiste" : """Plombier Chauffagiste Chaffoteaux
Entretien Chaudiere Chaffoteaux
Contrat Maintenance Chaudiere Chaffoteaux
Chauffagiste Pas Cher Chaffoteaux
Depannage Chaudiere Chaffoteaux
Installation Chaudiere Chaffoteaux
Remplacement Chaudiere Chaffoteaux
Reparation Chaudiere Chaffoteaux
Changement Chaudiere Chaffoteaux
Chauffagiste Chaffoteaux
Plombier Chauffagiste Chappee
Entretien Chaudiere Chappee
Contrat Maintenance Chaudiere Chappee
Chauffagiste Pas Cher Chappee
Depannage Chaudiere Chappee
Installation Chaudiere Chappee
Remplacement Chaudiere Chappee
Reparation Chaudiere Chappee
Changement Chaudiere Chappee
Chauffagiste Chappee
Plombier Chauffagiste De Dietrich
Entretien Chaudiere De Dietrich
Contrat Maintenance Chaudiere De Dietrich
Chauffagiste Pas Cher De Dietrich
Depannage Chaudiere De Dietrich
Installation Chaudiere De Dietrich
Remplacement Chaudiere De Dietrich
Reparation Chaudiere De Dietrich
Changement Chaudiere De Dietrich
Chauffagiste De Dietrich
Plombier Chauffagiste Elm Leblanc
Entretien Chaudiere Elm Leblanc
Contrat Maintenance Chaudiere Elm Leblanc
Chauffagiste Pas Cher Elm Leblanc
Depannage Chaudiere Elm Leblanc
Installation Chaudiere Elm Leblanc
Remplacement Chaudiere Elm Leblanc
Reparation Chaudiere Elm Leblanc
Changement Chaudiere Elm Leblanc
Chauffagiste Elm Leblanc
Plombier Chauffagiste Franco Belge
Entretien Chaudiere Franco Belge
Contrat Maintenance Chaudiere Franco Belge
Chauffagiste Pas Cher Franco Belge
Depannage Chaudiere Franco Belge
Installation Chaudiere Franco Belge
Remplacement Chaudiere Franco Belge
Reparation Chaudiere Franco Belge
Changement Chaudiere Franco Belge
Chauffagiste Franco Belge
Plombier Chauffagiste Frisquet
Entretien Chaudiere Frisquet
Contrat Maintenance Chaudiere Frisquet
Chauffagiste Pas Cher Frisquet
Depannage Chaudiere Frisquet
Installation Chaudiere Frisquet
Remplacement Chaudiere Frisquet
Reparation Chaudiere Frisquet
Changement Chaudiere Frisquet
Chauffagiste Frisquet
Plombier Chauffagiste Saunier Duval
Entretien Chaudiere Saunier Duval
Contrat Maintenance Chaudiere Saunier Duval
Chauffagiste Pas Cher Saunier Duval
Depannage Chaudiere Saunier Duval
Installation Chaudiere Saunier Duval
Remplacement Chaudiere Saunier Duval
Reparation Chaudiere Saunier Duval
Changement Chaudiere Saunier Duval
Chauffagiste Saunier Duval
Plombier Chauffagiste Vaillant
Entretien Chaudiere Vaillant
Contrat Maintenance Chaudiere Vaillant
Chauffagiste Pas Cher Vaillant
Depannage Chaudiere Vaillant
Installation Chaudiere Vaillant
Remplacement Chaudiere Vaillant
Reparation Chaudiere Vaillant
Changement Chaudiere Vaillant
Chauffagiste Vaillant
Plombier Chauffagiste Viessmann
Entretien Chaudiere Viessmann
Contrat Maintenance Chaudiere Viessmann
Chauffagiste Pas Cher Viessmann
Depannage Chaudiere Viessmann
Installation Chaudiere Viessmann
Remplacement Chaudiere Viessmann
Reparation Chaudiere Viessmann
Changement Chaudiere Viessmann
Chauffagiste Viessmann
Plombier Chauffagiste
Entretien Chaudiere
Contrat Maintenance Chaudiere
Chauffagiste Pas Cher
Depannage Chaudiere
Installation Chaudiere
Remplacement Chaudiere
Reparation Chaudiere
Changement Chaudiere
Dépannage Chauffage
Installation Chauffage
Dépannage Chaudière Gaz
Révision Chauffage
Dépannage Urgence Chauffage
Remise En Route Chaudière
Contrat Entretien
Dépannage Chaudière
Révision Chaudière
Dépanneur Chauffagiste
Dépanneur Chauffage
Tous Travaux De Chauffage
Dépannage Chaudière Fioul
Dépannage Chauffe-Eau
Urgence Chauffagiste
Entretien Chaudière
Entretien Chauffage
Entretien Chaudière Gaz
Artisan Chauffagiste
Prix Chaudière Gaz
Chaudière Mazout
Dépannage Chaudière électrique
Chaudière Gaz Condensation
Chauffage Chaudière
Dépannage Chauffage Fioul
Dépannage Chaudière Gaz
Vidange Chauffage
Chaudière Frisquet
Chaudière Saunier Duval
Entretien Chaudière Mazout
Chauffage Français Chaudières
Comparatif Chaudière Gaz
Problème Chaudière
Installation Chauffage Gaz
Entretien Chaudière Gaz Fioul
Chauffagiste
""",
 "serrurier": """Serrurerie
Changement de serrure
Artisans serrurier
Remplacement de serrure
Blindage de porte
Ouverture de porte
Serrurier métallier
Réparation de serrure
Pose de verrous
Déblocage de porte
Ouverture à la radio
Dépannage en serrurerie
Serrurier professionnel
Blindage de porte
Dépannage serrurerie
Urgence serrurerie
Perte de clefs
Serrurier
Pose volet roulant électrique 
Montage volet roulant 
Centralisation volet roulant 
Motoriser Volet roulant 
Branchement volet roulant 
Tarif volet roulant 
Motoriser un volet roulant 
Installation volet roulant 
Serrurier agrée toutes marques de serrures
Serrure briard
Serrure Pollux
Installation de bloc-porte
Serrure picard
Serrure city
Ouverture de porte
Pose de verrou
Serrure vachette
Remplacement de serrure
Serrure Kelso
Réparation après effraction
Serrure pm
Dépanneur serrurier
Serrure la perche
Serrure va
Serrurier
Pose porte blindée
Dépannage serrurerie
Serrurier pas cher
Urgence serrurier
Serrure fichet
Installation porte coupe-feu
Fermeture provisoire
Dépanneur serrure
Tous travaux de serrurerie
Serrure relax
Changement de serrure
Serrure dom
Installation serrure
Serrure mottera
Serrure Héraclès
Serrure Muel
Artisan serrurier
Serrure métaux
Réparation de serrure
""", 
"voletiste" : """Volet Roulant
Prix volet roulant
Déblocage rideau métallique
Installation volet roulant
Moteur pour volet roulant
Motorisation volet roulant
Domotique volet roulant
Volet roulant électrique
Moteur volet roulant électrique
Prix volet roulant électrique
Volet roulant aluminium
Volet roulant sur mesure
Rideau métallique
Volet roulant alu
Volet roulant
Volet roulant pvc
Manivelle volet roulant  
Volet roulant
Rideaux métalliques
Réparation rideaux métalliques
Réparation volet roulant
Déblocage rideau métallique
Volets roulants
Dépannage installation volet roulant
Installation rideaux métalliques
Installation de volet roulant
Réparation de volet roulant
Installation de rideaux métallique
Réparation rideaux métallique
Installation réparation volet roulant
Réparation de volet roulant 
Installation volet roulant
Vente volet roulant
Installation Volet Roulant
Pose Volet Roulant
Volet Roulant Garage
""",
"vitrier": """Remplacement de vitrage cassé
Remplacement de verrières
Baies vitrées
Pose de vitres toutes dimensions
Pose immédiate de vitres
Verre de sécurité
Vitrine de magasins
Double-vitrage
Remplacement de vitrages magasins
SOS Vitrerie
Changement de vitres suite à effraction
Pose de portes vitrées
Dépannage miroiterie
Remplacement double vitrage
Remplacement vitre brisée
Isolation thermique
Pose double vitrage
Pose de survitrage
Remplacement vitrine
Tous travaux de vitrerie
Isolation acoustique
Vitrier pas cher
Réparation bris de glace
Pose verre blindé
Urgence vitrier
Placage provisoire
Installation vitre
Vitrier miroitier
Dépanneur vitrier
Dépannage vitrerie
Remplacement de vitre
Pose simple vitrage
Artisan vitrier
Vitrier
""" }
ville = "Strasbourg"
metiers = ["plombier","chauffagiste","electricien","vitrier", "serrurier","voletiste"]



with open("test.txt","w") as f:
	for m in metiers:
		sh_list = mot_clef_list[m].split("\n")
		random.shuffle(sh_list)
		try:
			#x = "<li>{}</li>".format(" {}</li><li>".format(ville).join(sh_list[:19]))
			f.write("{}".format(sh_list))
		except UnicodeEncodeError as e:
			print(e.value)
			print(x)
	f.close()