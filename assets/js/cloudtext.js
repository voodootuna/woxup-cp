$(function(){
	var A=new Array({text:"tarif plombier",weight:5},{text:"tarif horaire plombier",weight:3},{text:"plombier tarif",weight:1},{text:"tarifs plombier",weight:6},{text:"tarif plombier paris",weight:3},{text:"plombier tarif horaire",weight:7},{text:"tarif déplacement plombier",weight:3},{text:"plombier paris tarif",weight:3},{text:"tarif intervention plombier",weight:5},{text:"plombier urgence",weight:6},{text:"urgence plombier",weight:6},{text:"plombier en urgence",weight:7},{text:"plombier chauffagiste",weight:5},{text:"plombier chauffagiste salaire",weight:6},{text:"plombier chauffagiste nantes",weight:9},{text:"plombier chauffagiste toulouse",weight:6},{text:"chauffagiste plombier",weight:7},{text:"plombiers chauffagistes",weight:3},{text:"grille salaire plombier chauffagiste",weight:5},{text:"artisan plombier chauffagiste",weight:5},{text:"plombier chauffage",weight:6},{text:"entreprise plombier chauffagiste",weight:7},{text:"plombier chauffagiste essonne",weight:4},{text:"auto entrepreneur plombier chauffagiste",weight:2},{text:"plombier chauffagiste métier",weight:3},{text:"dépannage plombier",weight:1},{text:"dépannage plomberie",weight:5},{text:"dépannage plombier paris",weight:7},{text:"plombier dépannage",weight:6},{text:"dépannage plomberie paris",weight:5},{text:"tarif dépannage plomberie",weight:9},{text:"dépannage chaudière",weight:8},{text:"plombier depannage paris",weight:3},{text:"depannage plomberie lyon",weight:1},{text:"dépannage plomberie nantes",weight:3},{text:"plomberie",weight:7},{text:"entreprise de plomberie",weight:6},{text:"plomberie pro",weight:7},{text:"entreprise plomberie",weight:2},{text:"plomberie paris",weight:6},{text:"devis plomberie",weight:8},{text:"plomberie per",weight:1},{text:"entreprise plomberie paris",weight:9},{text:"plomberie pas cher",weight:7},{text:"plomberie sanitaire",weight:2},{text:"plomberie chauffage",weight:8},{text:"tarif plomberie",weight:9},{text:"prix plomberie",weight:8},{text:"exemple devis plomberie",weight:6},{text:"travaux de plomberie",weight:2},{text:"plomberie en ligne",weight:3},{text:"raccords plomberie",weight:8},{text:"travaux plomberie",weight:2},{text:"urgence plomberie",weight:8},{text:"devis plomberie en ligne",weight:3},{text:"fournisseur plomberie",weight:4},{text:"plomberie discount",weight:4},{text:"plomberie chauffagiste",weight:7},{text:"société de plomberie",weight:2},{text:"plomberie salle de bain",weight:2},{text:"societe plomberie",weight:4},{text:"plomberie maison",weight:5},{text:"entreprise plomberie chauffage",weight:6},{text:"urgence plomberie paris",weight:5},{text:"chauffage plomberie",weight:8},{text:"devis plomberie gratuit",weight:8},{text:"tarifs plomberie",weight:8},{text:"societe plomberie paris",weight:4},{text:"plomberie salaire",weight:8},{text:"emploi plomberie",weight:5},{text:"devis de plomberie",weight:7},{text:"prix plombier",weight:4},{text:"prix horaire plombier",weight:9},{text:"prix intervention plombier",weight:6},{text:"plombier prix",weight:1},{text:"devis plombier",weight:3},{text:"plombier devis",weight:1},{text:"plombier devis gratuit",weight:7},{text:"devis plombier gratuit",weight:7},{text:"devis plombier paris",weight:1},{text:"devis plombier en ligne",weight:3},{text:"plombier paris devis gratuit",weight:4},{text:"plombier sanitaire",weight:2},{text:"installateur sanitaire",weight:2},{text:"installation sanitaire",weight:8}),N=new Array({text:"double vitrage",weight:6},{text:"fenetre pvc prix",weight:6},{text:"changer fenetre",weight:1},{text:"fenetre pvc pas cher",weight:4},{text:"fenetre sur mesure",weight:2},{text:"porte fenetre coulissante",weight:2},{text:"pose fenetre",weight:4},{text:"fenetre pas cher",weight:4},{text:"fenetre coulissante pvc",weight:9},{text:"prix fenetre",weight:4},{text:"renovation fenetre",weight:1},{text:"fenetres bois",weight:10},{text:"fenetre pvc renovation",weight:9},{text:"prix fenetre sur mesure",weight:5},{text:"pose de fenetre pvc",weight:8},{text:"remplacement fenetre",weight:9},{text:"changer une fenetre",weight:6},{text:"changement fenetre",weight:3},{text:"achat fenetre",weight:3},{text:"double vitrage prix",weight:3},{text:"triple vitrage",weight:7},{text:"vitrage",weight:5},{text:"prix double vitrage",weight:5},{text:"prix fenetre double vitrage",weight:2},{text:"fenetre triple vitrage",weight:10},{text:"vitrage isolant",weight:3},{text:"vitrage anti effraction",weight:9},{text:"fenetre double vitrage prix",weight:2},{text:"vitrage sur mesure",weight:4},{text:"triple vitrage prix",weight:9},{text:"prix fenetre pvc double vitrage",weight:8},{text:"prix double vitrage m2",weight:1},{text:"tarif vitrerie",weight:1},{text:"devis vitrerie",weight:3},{text:"vitrerie en ligne",weight:10},{text:"vitrerie prix",weight:3},{text:"la vitrerie",weight:1},{text:"entreprise de vitrerie",weight:4},{text:"vitrerie pas cher",weight:5},{text:"entreprise vitrerie",weight:4},{text:"marseille vitrerie",weight:9},{text:"vitrerie urgence",weight:8},{text:"vitrerie miroir",weight:1},{text:"miroitier",weight:2},{text:"miroitiers",weight:9},{text:"mastic vitrier",weight:8},{text:"mastic de vitrier",weight:9},{text:"pose mastic vitrier",weight:3},{text:"mastic vitrier en cartouche",weight:3},{text:"pose de mastic de vitrier",weight:5},{text:"vitres",weight:3},{text:"vitre sur mesure",weight:9},{text:"remplacement vitre",weight:1},{text:"vitre pas cher",weight:1},{text:"devis vitre",weight:9},{text:"remplacement de vitre",weight:1},{text:"vitres pas cher",weight:5},{text:"vitre pas chere",weight:9},{text:"remplacement vitres",weight:9},{text:"urgence serrurier",weight:3},{text:"urgence vitrier",weight:5},{text:"vitrier urgence",weight:4},{text:"vitrier paris",weight:8},{text:"outil de vitrier",weight:2},{text:"outils de vitrier",weight:5},{text:"diamant vitrier",weight:5},{text:"couteau de vitrier",weight:2},{text:"outil vitrier",weight:7},{text:"le vitrier rapide",weight:7},{text:"vitrier uccle",weight:5},{text:"outillage vitrier",weight:6},{text:"emploi vitrier",weight:2},{text:"serrurier vitrier",weight:8},{text:"un vitrier",weight:7},{text:"vitrier laval",weight:7},{text:"vitrier formation",weight:6},{text:"outils vitrier",weight:10}),L=new Array({text:"livraison bois de chauffage",weight:6},{text:"chauffage poele a bois",weight:7},{text:"installation chauffage",weight:2},{text:"installation chauffage central",weight:4},{text:"installateur chauffage",weight:8},{text:"installation de chauffage",weight:10},{text:"installation chauffage gaz",weight:4},{text:"schema installation chauffage central",weight:3},{text:"installation chauffage central gaz",weight:1},{text:"installation chauffage bois",weight:4},{text:"installation chauffage au sol",weight:10},{text:"installation chauffage centrale",weight:5},{text:"installation de chauffage central",weight:8},{text:"installation chauffage au gaz",weight:8},{text:"chauffage fioul",weight:7},{text:"chauffage au fioul",weight:9},{text:"chaudiere fioul",weight:1},{text:"chauffage a fioul",weight:8},{text:"entretien chaudiere fioul",weight:6},{text:"chauffage central fioul",weight:1},{text:"depannage chaudiere fioul",weight:4},{text:"quel chauffage choisir",weight:7},{text:"quel type de chauffage choisir",weight:2},{text:"choisir son chauffage",weight:3},{text:"comment choisir son chauffage",weight:7},{text:"quelle chauffage choisir",weight:5},{text:"quel mode de chauffage choisir",weight:10},{text:"choisir chauffage",weight:7},{text:"quel chauffage electrique choisir",weight:9},{text:"choisir chauffage electrique",weight:5},{text:"economie de chauffage",weight:4},{text:"systeme de chauffage le plus economique",weight:1},{text:"economie chauffage",weight:6},{text:"mode de chauffage le plus economique",weight:7},{text:"chauffage electrique le plus economique",weight:1},{text:"le chauffage le plus economique",weight:9},{text:"type de chauffage le plus economique",weight:10},{text:"systeme de chauffage economique",weight:8},{text:"quel est le chauffage le plus economique",weight:1},{text:"chauffage economique electrique",weight:8},{text:"systeme chauffage economique",weight:10},{text:"economie chauffage electrique",weight:4},{text:"plomberie chauffagiste",weight:4},{text:"materiel plomberie chauffage",weight:4},{text:"entreprise plomberie ",weight:2},{text:"entreprise de plomberie ",weight:3},{text:"plombier chauffagiste",weight:1},{text:"plombier chauffagiste ",weight:7},{text:"cv plombier chauffagiste",weight:7},{text:"cap plombier chauffagiste",weight:1},{text:"logo plombier chauffagiste",weight:8},{text:"entreprise plombier chauffagiste",weight:10},{text:"plombier chauffagiste salaire",weight:5},{text:"recherche plombier chauffagiste",weight:4},{text:"chauffagiste plombier",weight:4},{text:"artisan plombier chauffagiste",weight:1},{text:"devenir plombier chauffagiste",weight:3},{text:"plombiers chauffagistes",weight:4},{text:"thermostat chauffage",weight:9},{text:"thermostat chauffage gaz",weight:3},{text:"thermostat chauffage central",weight:2},{text:"thermostat de chauffage",weight:8},{text:"thermostat chauffage sans fil",weight:9},{text:"calcul puissance chauffage",weight:2},{text:"calcul chauffage",weight:7},{text:"calcul chauffage maison",weight:9},{text:"calcul de puissance de chauffage",weight:5},{text:"calcul puissance radiateur chauffage central",weight:3},{text:"calcul chauffage central",weight:7},{text:"calcul puissance chauffage electrique",weight:7},{text:"calcul puissance de chauffage",weight:5},{text:"calcul de chauffage",weight:6},{text:"chauffage air air",weight:3},{text:"chauffage air chaud",weight:8},{text:"chauffage a granule",weight:10},{text:"chauffage a granule de bois",weight:1},{text:"chauffage au granule",weight:2},{text:"radiateur de chauffage",weight:1},{text:"radiateur",weight:2},{text:"radiateur chauffage",weight:1},{text:"chauffage radiateur",weight:8},{text:"radiateur prix",weight:1},{text:"radiateurs chauffage",weight:7},{text:"chauffage pellet",weight:2},{text:"chauffage pellets",weight:5},{text:"chauffage au pellet",weight:6},{text:"chauffage central pellets",weight:3},{text:"chauffage pellets prix",weight:3},{text:"chauffage aux pellets",weight:9},{text:"chaudiere electrique",weight:7},{text:"chaudiere bois",weight:1},{text:"chaudiere condensation",weight:7},{text:"chaudiere frisquet",weight:6},{text:"chaudiere a bois",weight:9},{text:"chaudiere gaz condensation",weight:7},{text:"prix chaudiere",weight:8},{text:"chaudieres gaz",weight:1},{text:"prix entretien chaudiere",weight:2},{text:"installation chaudiere gaz",weight:6},{text:"depanneur chaudiere",weight:1},{text:"probleme chaudiere",weight:5},{text:"chaudiere mazout",weight:5},{text:"panne chaudiere",weight:1},{text:"panne chaudiere gaz",weight:1},{text:"tarif entretien chaudiere",weight:3},{text:"reparateur chaudiere",weight:6},{text:"maintenance chaudiere",weight:8},{text:"depannage plombier",weight:6},{text:"depannage gaz",weight:7},{text:"depannage chauffe eau ",weight:5},{text:"depannage climatisation",weight:4},{text:"gaz depannage",weight:2},{text:"depannage pompe a chaleur",weight:7},{text:"depannage chaudiere frisquet",weight:1},{text:"depannage chaudiere ",weight:1},{text:"regulateur chauffage",weight:9},{text:"regulateur de chauffage",weight:6},{text:"regulation chauffage electrique",weight:1},{text:"chauffage fuel",weight:7},{text:"chauffage au fuel",weight:5},{text:"chauffage central fuel",weight:9},{text:"chauffage central au fuel",weight:6},{text:"chauffage a fuel",weight:4},{text:"programmateur chauffage gaz",weight:4},{text:"programmateur chauffage",weight:9},{text:"programmateur chauffage electrique",weight:4},{text:"programmateur de chauffage",weight:3},{text:"programmation chauffage",weight:9},{text:"programmateur chauffage sans fil",weight:10},{text:"chauffage au sol prix",weight:4},{text:"prix chauffage au sol",weight:5},{text:"chauffage fioul prix",weight:5},{text:"prix circulateur chauffage",weight:5},{text:"prix chauffage",weight:6},{text:"chauffage a granule prix",weight:2},{text:"prix du fuel de chauffage",weight:2},{text:"chauffage electrique prix",weight:9},{text:"chauffage au fioul prix",weight:8},{text:"chauffage solaire prix",weight:10},{text:"prix chauffage au sol electrique",weight:8},{text:"prix chauffage par le sol",weight:1},{text:"chauffage geothermie prix",weight:8},{text:"prix du fuel chauffage",weight:8},{text:"chauffage par le sol prix",weight:4},{text:"prix fuel chauffage",weight:10},{text:"chauffage au sol electrique prix",weight:8},{text:"chauffage sol prix",weight:1},{text:"prix mazout chauffage",weight:3},{text:"prix du fioul de chauffage",weight:5},{text:"pompe de circulation chauffage",weight:4},{text:"pompe chauffage",weight:4},{text:"chauffage au sol pompe a chaleur",weight:1},{text:"pompe circulation chauffage",weight:3},{text:"pompe chauffage central",weight:5},{text:"formation plombier chauffagiste",weight:4},{text:"formation chauffagiste",weight:4},{text:"formation plombier chauffagiste greta",weight:2},{text:"formation plomberie chauffage",weight:2},{text:"formation de plombier chauffagiste",weight:2},{text:"cout chauffage electrique",weight:8},{text:"cout chauffage au sol",weight:5},{text:"cout chauffage gaz",weight:3},{text:"cout installation chauffage central",weight:4},{text:"cout installation chauffage gaz",weight:3},{text:"cout du chauffage electrique",weight:9},{text:"chauffage le moins cher",weight:5},{text:"chauffage pas cher",weight:10},{text:"chauffage moins cher",weight:6},{text:"prix chaudiere gaz",weight:5},{text:"chauffage au gaz prix",weight:7},{text:"prix chauffage gaz",weight:5},{text:"prix entretien chaudiere gaz",weight:5},{text:"prix du chauffage au gaz",weight:10},{text:"prix chauffage au gaz",weight:5},{text:"chauffage central gaz",weight:6},{text:"chauffage central au gaz",weight:4},{text:"radiateur chauffage central gaz",weight:5},{text:"chauffage centrale au gaz",weight:10},{text:"schema chauffage central gaz",weight:3},{text:"chauffage solaire",weight:4},{text:"chauffage solaire thermique",weight:4},{text:"kit chauffage solaire",weight:3},{text:"chauffage central solaire",weight:5},{text:"chauffage panneau solaire",weight:6},{text:"le chauffage solaire",weight:7},{text:"chauffage central prix",weight:10},{text:"prix installation chauffage central gaz",weight:6},{text:"prix installation chauffage central",weight:5},{text:"prix chauffage central",weight:8},{text:"chauffage central electrique prix",weight:8},{text:"chauffage electrique inertie",weight:6},{text:"consommation chauffage electrique",weight:5},{text:"comparatif chauffage electrique",weight:5},{text:"le chauffage electrique",weight:2},{text:"systeme de chauffage electrique",weight:1},{text:"chauffage exterieur electrique",weight:3},{text:"type de chauffage electrique",weight:5},{text:"chauffage electrique exterieur",weight:10},{text:"forum chauffage electrique",weight:9},{text:"meilleur chauffage",weight:9},{text:"meilleur systeme de chauffage",weight:8},{text:"le meilleur chauffage",weight:1},{text:"meilleur type de chauffage",weight:1},{text:"meilleur chauffage economique",weight:7},{text:"emploi plombier chauffagiste",weight:4},{text:"emploi chauffagiste",weight:4},{text:"emploi chauffage",weight:8},{text:"offre emploi plombier chauffagiste",weight:9},{text:"recherche emploi plombier chauffagiste",weight:10},{text:"plombier chauffagiste emploi",weight:9},{text:"chauffage camping car",weight:3},{text:"chauffage pour camping car",weight:10},{text:"chauffage gaz camping car",weight:7},{text:"chauffage camping",weight:1},{text:"chauffage truma camping car",weight:5},{text:"chauffage gasoil camping car",weight:9},{text:"chauffage webasto camping car",weight:7},{text:"chauffage camping car truma",weight:10},{text:"chauffage camping car gasoil",weight:7},{text:"chauffage de camping",weight:3},{text:"devis chauffage",weight:10},{text:"devis chauffage electrique",weight:2},{text:"devis chauffage central",weight:1},{text:"devis chauffage au sol",weight:9},{text:"devis chauffagiste",weight:5},{text:"devis chauffage gaz",weight:1},{text:"chauffage piscine",weight:2},{text:"chauffage piscine hors sol",weight:3},{text:"chauffage pour piscine",weight:9},{text:"chauffage de piscine",weight:8},{text:"chauffage piscine intex",weight:4},{text:"chauffage piscine pas cher",weight:9},{text:"chauffage pour piscine hors sol",weight:3},{text:"chauffage piscine electrique",weight:4},{text:"chauffage piscine bois",weight:8},{text:"chauffage electrique piscine",weight:8},{text:"chauffage maison",weight:8},{text:"chauffage solaire maison",weight:2},{text:"chauffage maison individuelle",weight:7},{text:"chauffage economique maison ancienne",weight:5},{text:"chauffage economique maison",weight:8},{text:"chauffage terrasse",weight:4},{text:"chauffage de terrasse",weight:9},{text:"chauffage terrasse electrique",weight:8},{text:"chauffage terrasse gaz",weight:2},{text:"chauffage pour terrasse",weight:10},{text:"chauffage solaire piscine",weight:5},{text:"chauffage piscine solaire",weight:2},{text:"chauffage solaire pour piscine",weight:2},{text:"chauffage piscine panneaux solaires",weight:4},{text:"panneau solaire chauffage piscine",weight:10},{text:"piscine chauffage solaire",weight:5},{text:"chaudiere electrique pour chauffage central",weight:8},{text:"radiateur pour chauffage au gaz",weight:6},{text:"chauffage pour aquarium",weight:1},{text:"radiateur pour chauffage central",weight:9},{text:"chauffage pour serre",weight:7},{text:"radiateur pour chauffage gaz",weight:10},{text:"chauffage pour veranda",weight:5},{text:"chauffage pour tente",weight:10},{text:"tuyau chauffage",weight:2},{text:"tuyau de chauffage",weight:10},{text:"isolation tuyau chauffage",weight:1},{text:"tuyau multicouche chauffage",weight:9},{text:"isolant tuyau chauffage",weight:3},{text:"chauffage accumulation",weight:2},{text:"chauffage par accumulation",weight:4},{text:"chauffage accumulateur",weight:7},{text:"accumulateur chauffage",weight:3},{text:"chauffage",weight:8},{text:"chauffagiste ",weight:5},{text:"chauffage discount",weight:7},{text:"circulateur chauffage",weight:5},{text:"entretien chauffage",weight:4},{text:"entreprise chauffage",weight:5},{text:"type de chauffage",weight:10},{text:"chauffagiste lyon",weight:6},{text:"entreprise de chauffage",weight:5},{text:"chauffage sanitaire",weight:5},{text:"ballon tampon chauffage",weight:8},{text:"comparatif chauffage",weight:8},{text:"circulateur de chauffage",weight:3},{text:"chauffagiste 91",weight:5},{text:"chauffage radiant",weight:2},{text:"chauffagiste 95",weight:9},{text:"chauffagiste 78",weight:8},{text:"chauffagiste 94",weight:6},{text:"chauffagistes",weight:9},{text:"chauffage eau chaude",weight:3},{text:"credit impot chauffage",weight:2},{text:"chauffagiste lille",weight:2},{text:"chauffage thermodynamique",weight:8},{text:"chauffage biomasse",weight:8},{text:"chauffage industriel",weight:8},{text:"france chauffage",weight:6},{text:"chauffage plinthe",weight:10},{text:"le chauffage",weight:5},{text:"antigel chauffage",weight:10},{text:"chauffage francais",weight:3},{text:"forum chauffage",weight:6},{text:"chauffages",weight:8},{text:"ideal standard chauffage",weight:9},{text:"grossiste chauffage",weight:1},{text:"chauffage infrarouge",weight:1},{text:"chauffage salle de bain",weight:5},{text:"chauffagiste marseille",weight:9},{text:"mode de chauffage",weight:2},{text:"different type de chauffage",weight:3},{text:"vanne 4 voies chauffage",weight:6},{text:"deville chauffage",weight:2},{text:"chauffage par plinthe",weight:2},{text:"moyen de chauffage",weight:1},{text:"types de chauffage",weight:6},{text:"chauffage soufflant",weight:1},{text:"vase expansion chauffage",weight:4},{text:"tube chauffage",weight:2},{text:"puissance chauffage",weight:3},{text:"chauffagiste toulouse",weight:2},{text:"electrovanne chauffage",weight:8},{text:"location chauffage",weight:10},{text:"conseil chauffage",weight:9},{text:"chauffagiste bordeaux",weight:8},{text:"tube multicouche chauffage",weight:8},{text:"chauffage appoint",weight:7},{text:"chauffage aquarium",weight:4},{text:"chauffage monotube",weight:3},{text:"chauffagiste bruxelles",weight:5},{text:"chauffage atelier",weight:10},{text:"chauffage individuel",weight:3},{text:"chauffage climatisation",weight:8},{text:"appareil de chauffage",weight:7},{text:"chauffage thermique",weight:7},{text:"chauffage caravane",weight:4},{text:"chauffagiste 77",weight:10},{text:"chauffage pac",weight:3},{text:"materiel chauffage",weight:4},{text:"accelerateur chauffage",weight:9},{text:"per chauffage",weight:2},{text:"technicien chauffagiste",weight:5},{text:"multicouche chauffage",weight:10},{text:"discount chauffage",weight:6},{text:"accelerateur de chauffage",weight:7},{text:"chauffage et climatisation",weight:1},{text:"reduction impot chauffage",weight:10},{text:"solution chauffage",weight:4},{text:"chauffage par ionisation",weight:4},{text:"chauffage inertie",weight:4},{text:"flexible chauffage",weight:4},{text:"chauffage voiture",weight:9},{text:"chauffage de chantier",weight:4},{text:"chauffage webasto",weight:6},{text:"chauffage rayonnant",weight:8},{text:"brico depot chauffage",weight:4},{text:"chauffage caloporteur",weight:6},{text:"outillage chauffagiste",weight:7},{text:"chauffage domotique",weight:10},{text:"chauffage elec",weight:3},{text:"chauffage hors gel",weight:5},{text:"chauffage en fonte",weight:2},{text:"viessmann chauffage",weight:9},{text:"chauffage serre",weight:8},{text:"chauffage mural",weight:3},{text:"dimensionnement chauffage",weight:6},{text:"domotique chauffage",weight:3},{text:"quel type de chauffage",weight:2},{text:"chauffage mazout",weight:2},{text:"comparaison chauffage",weight:1},{text:"chauffage 12v",weight:6},{text:"chauffage design",weight:6},{text:"chauffage eco",weight:1},{text:"chauffage chantier",weight:6},{text:"chauffage clim reversible",weight:4},{text:"climatisation chauffage",weight:8},{text:"chauffage voiture allume cigare",weight:1},{text:"pieces detachees chauffage",weight:7},{text:"chauffage ionique",weight:10},{text:"chauffage mobile",weight:5},{text:"puissance chauffage par m2",weight:9},{text:"chauffage du nord",weight:10},{text:"ventilateur chauffage",weight:3},{text:"chauffage par induction",weight:2},{text:"chauffage radian",weight:8},{text:"chauffagiste  15",weight:8},{text:"chauffage par plinthes",weight:1},{text:"chauffage ionisation",weight:4},{text:"collecteur chauffage",weight:4},{text:"chauffage convecteur",weight:10},{text:"artisan chauffagiste",weight:5},{text:"chauffagiste 93",weight:9},{text:"chauffage energie renouvelable",weight:4},{text:"chauffage deville",weight:10},{text:"chauffage propane",weight:8},{text:"poele chauffage",weight:4},{text:"raccord chauffage",weight:3},{text:"chauffage salle de bain soufflant",weight:7},{text:"chauffage plafond",weight:1},{text:"programateur chauffage",weight:5},{text:"sauter chauffage",weight:9},{text:"salaire chauffagiste",weight:10},{text:"chauffage radiant infrarouge",weight:9},{text:"chauffage condensation",weight:3},{text:"radiant chauffage",weight:2},{text:"chauffage terrarium",weight:2},{text:"chauffage insert",weight:3},{text:"credit impots chauffage",weight:7},{text:"chauffagiste viessmann",weight:6},{text:"isolation tuyaux chauffage",weight:4},{text:"chauffage fonte",weight:8},{text:"chauffage par rayonnement",weight:8},{text:"mini chauffage",weight:8},{text:"comparatif mode de chauffage",weight:5},{text:"chauffage panneau rayonnant",weight:2},{text:"chauffage a huile",weight:6},{text:"chauffage de serre",weight:2},{text:"chauffage soufflant industriel",weight:9},{text:"chauffagiste  17",weight:5},{text:"subvention chauffage",weight:10},{text:"chauffagiste  18",weight:2},{text:"chauffagiste versailles",weight:3},{text:"magasin de chauffage",weight:9},{text:"chauffage gainable",weight:5},{text:"siemens chauffage",weight:1},{text:"honeywell chauffage",weight:5},{text:"chauffagiste  14",weight:10},{text:"magasin chauffage",weight:10},{text:"chauffage parasol",weight:6},{text:"ventilation chauffage",weight:4},{text:"guide chauffage",weight:8},{text:"logiciel sav chauffage",weight:8},{text:"chauffage de voiture",weight:3},{text:"reduction impots chauffage",weight:10},{text:"chauffage de salle de bain",weight:10},{text:"chauffage tente",weight:7},{text:"chauffage seche serviette",weight:4},{text:"chauffage au plafond",weight:9},{text:"chauffage charbon",weight:5},{text:"chauffagiste  11",weight:2},{text:"vanne 3 voies chauffage",weight:7},{text:"chauffage au charbon",weight:7},{text:"petit chauffage",weight:5},{text:"chauffage appoint salle de bain",weight:7},{text:"chauffage photovoltaique",weight:1},{text:"buderus chauffage",weight:5},{text:"chauffagiste salaire",weight:2},{text:"chauffage garage",weight:10},{text:"tube acier chauffage",weight:9},{text:"chauffage catalyse",weight:1},{text:"insert chauffage",weight:2},{text:"chauffage poele",weight:8},{text:"chauffagiste yvelines",weight:9},{text:"chauffage alternatif",weight:3},{text:"chauffage basse consommation",weight:6},{text:"charbon de chauffage",weight:5},{text:"chauffage ",weight:6},{text:"le chauffagiste",weight:5},{text:"chauffage clim",weight:7},{text:"chauffage spa",weight:6},{text:"chauffagiste essonne",weight:3},{text:"chauffagiste 92",weight:5},{text:"chauffagiste  5",weight:2},{text:"chauffage appoint petrole",weight:4},{text:"chauffage chaleur douce",weight:7},{text:"chauffage coleman",weight:10},{text:"tuyaux de chauffage",weight:9},{text:"roca chauffage",weight:4},{text:"vente chauffage",weight:6}),S=new Array({text:"electricien en batiment",weight:7},{text:"stage electricien batiment",weight:7},{text:"cherche emploi electricien batiment",weight:3},{text:"electricien dans le batiment",weight:5},{text:"electricien de batiment",weight:6},{text:"travaux du batiment",weight:2},{text:"recrutement electricien batiment",weight:7},{text:"emplois electricien batiment",weight:3},{text:"qualification electricien batiment",weight:3},{text:"tous travaux batiment",weight:7},{text:"travaux dans le batiment",weight:10},{text:"artisan electricien ",weight:4},{text:"artisans electricien",weight:6},{text:"electricien artisan",weight:4},{text:"taux horaire artisan electricien",weight:6},{text:"artisan electricien toulouse",weight:4},{text:"salaire artisan electricien",weight:7},{text:"artisan electricien salaire",weight:8},{text:"artisan electricien bordeaux",weight:6},{text:"electricien depannage",weight:1},{text:"depannage electrique ",weight:4},{text:"tarif depannage electrique",weight:1},{text:"schema electrique maison",weight:4},{text:"installation electrique maison",weight:4},{text:"refaire installation electrique maison",weight:6},{text:"installation electrique domestique",weight:3},{text:"prix installation electrique",weight:6},{text:"electrique installation",weight:10},{text:"realiser une installation electrique",weight:6},{text:"renover une installation electrique",weight:3},{text:"installation electrique immeuble",weight:9},{text:"les installation electrique",weight:10},{text:"fournisseur electricite",weight:1},{text:"electricite generale",weight:1},{text:"societe electricite",weight:9},{text:"electricite de france",weight:2},{text:"electricite auto",weight:7},{text:"electricite domestique",weight:4},{text:"emploi electricite",weight:8},{text:"exemple de devis electricite",weight:2},{text:"sous traitance electricite",weight:2},{text:"ecl electricite",weight:7},{text:"devis electricite batiment",weight:5},{text:"devis electrique",weight:6},{text:"electricien devis",weight:1},{text:"electricien devis gratuit",weight:9},{text:"exemple devis electricien",weight:2},{text:"exemple de devis electricien",weight:1},{text:"logiciel devis electricien",weight:10},{text:"electricien auto lyon",weight:10},{text:"caisse a outils electricien",weight:9},{text:"caisse a outil electricien",weight:3},{text:"caisse a outils electricien complete",weight:3},{text:"outils electricien facom",weight:2},{text:"outil pour electricien",weight:5},{text:"entreprise electrique",weight:8},{text:"devis travaux electrique",weight:1},{text:"electricien auto entrepreneur",weight:9},{text:"auto entrepreneur electricien batiment",weight:10},{text:"assurance auto entrepreneur electricien",weight:6},{text:"logiciel pour electricien",weight:5},{text:"materiel pour electricien",weight:6},{text:"aiguille pour electricien",weight:3},{text:"logiciel pour electricien gratuit",weight:4},{text:"prise de courant electrique",weight:8},{text:"installation electrique industriel",weight:6},{text:"montage electrique industriel",weight:9},{text:"des travaux",weight:5},{text:"tous les travaux",weight:1},{text:"artisan tous travaux",weight:6},{text:"de travaux",weight:3},{text:"travaux artisan",weight:4},{text:"electricien noisy le grand",weight:3},{text:"electricien yerres",weight:7},{text:"bac pro electricien",weight:9},{text:"materiel electrique",weight:10},{text:"norme electrique",weight:4},{text:"cablage electrique",weight:1},{text:"tableau electrique",weight:4},{text:"renovation electrique",weight:4},{text:"implantation electrique",weight:5},{text:"terme electrique",weight:4},{text:"plans electrique",weight:1}),R=new Array({text:"serrurier pas cher",weight:4},{text:"serrurerie serrurier",weight:5},{text:"serrurerie porte",weight:1},{text:"bricard serrurerie",weight:3},{text:"travaux serrurerie",weight:1},{text:"fourniture serrurerie",weight:7},{text:"tarif serrurier ouverture de porte",weight:6},{text:"tarif serrurier ",weight:9},{text:"serrurier tarifs",weight:3},{text:"serrurier urgence",weight:2},{text:"urgence serrurier",weight:9},{text:"serrure fichet",weight:2},{text:"serrurie",weight:10},{text:"serrure",weight:1},{text:"changement de serrure",weight:4},{text:"serrures",weight:4},{text:"serrure mottura",weight:7},{text:"fichet serrure",weight:8},{text:"prix serrure",weight:4},{text:"changement serrure",weight:8},{text:"serrures fichet",weight:6},{text:"serrurie ",weight:5},{text:"serrure pas cher",weight:3},{text:"serrure prix",weight:3},{text:"depannage serrure ",weight:7},{text:"remplacement serrure",weight:7},{text:"reparation serrure",weight:4},{text:"devis serrure",weight:10},{text:"serrure fichet ",weight:1},{text:"prix pour changer une serrure",weight:2},{text:"serrures ",weight:8},{text:"tarif changement de serrure",weight:2},{text:"vente de serrure",weight:3},{text:"tarif serrure",weight:10},{text:"serrures pas cher",weight:4},{text:"serrure porte pas cher",weight:6},{text:"serrurier serrure",weight:5},{text:"prix serrurier",weight:4},{text:"serrurier prix",weight:4},{text:"prix intervention serrurier",weight:9},{text:"prix depannage serrurier",weight:2},{text:"prix serrurier ",weight:2},{text:"prix serrurier ouverture de porte",weight:7},{text:"bricard",weight:8},{text:"serrure bricard",weight:8},{text:"bricard serrure",weight:1},{text:"serrures bricard",weight:2},{text:"serrurier bricard",weight:9},{text:"bricard ",weight:7},{text:"serrurier bricard ",weight:3},{text:"formation serrurier",weight:5},{text:"serrurier formation",weight:9},{text:"formation serrurier depannage",weight:4},{text:"formation serrurier depanneur",weight:2},{text:"formation de serrurier",weight:9},{text:"emploi serrurier metallier",weight:5},{text:"ouverture de porte",weight:6},{text:"ouverture de porte ",weight:9},{text:"serrurier ouverture de porte",weight:7},{text:"ouverture de porte pas cher",weight:1},{text:"copie de cles",weight:3}),I=new Array({text:"Volet roulant",weight:10},{text:"Rideaux métalliques",weight:9},{text:"Réparation rideaux métalliques",weight:7},{text:"Réparation volet roulant",weight:10},{text:"Déblocage rideau métallique",weight:4},{text:"Volets roulants",weight:10},{text:"Dépannage installation volet roulant",weight:5},{text:"Installation rideaux métalliques",weight:5},{text:"Installation de volet roulant",weight:6},{text:"Réparation de volet roulant",weight:1},{text:"Installation de rideaux métallique",weight:10},{text:"Réparation rideaux métallique",weight:3},{text:"Installation réparation volet roulant",weight:4},{text:"Réparation de volet roulant id",weight:9},{text:"Installation volet roulant",weight:7},{text:"Vente volet roulant",weight:8},{text:"Pose Volet Roulant",weight:4},{text:"Volet Roulant Garage",weight:5},{text:"Prix volet roulant",weight:2},{text:"Moteur pour volet roulant",weight:6},{text:"Motorisation volet roulant",weight:9},{text:"Domotique volet roulant",weight:9},{text:"Volet roulant électrique",weight:3},{text:"Moteur volet roulant électrique",weight:6},{text:"Prix volet roulant électrique",weight:6},{text:"Volet roulant aluminium",weight:6},{text:"Volet roulant sur mesure",weight:5},{text:"Rideau métallique",weight:7},{text:"Volet roulant alu",weight:1},{text:"Volet roulant pvc",weight:8},{text:"Manivelle volet roulant  ",weight:5},{text:"Pose volet roulant électrique ",weight:6},{text:"Montage volet roulant ",weight:3},{text:"Centralisation volet roulant ",weight:9},{text:"Motoriser Volet roulant ",weight:8},{text:"Branchement volet roulant ",weight:4},{text:"Tarif volet roulant ",weight:5},{text:"Motoriser un volet roulant ",weight:8},{text:"Installation volet roulant ",weight:7});


var config = {removeOverflowing:true,delayedMode:true,shape:"rectangular"};
$("#wordcloud1").jQCloud(A,config),$("#wordcloud2").jQCloud(L,config),$("#wordcloud3").jQCloud(S,config),$("#wordcloud4").jQCloud(N,config),$("#wordcloud5").jQCloud(R,config),$("#wordcloud6").jQCloud(I,config)});
