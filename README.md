# Shadows Empire

Projet de développement d'un jeu de gestion détournant les classiques du genre med-fan pour les adapter à l'univers de la mafia et du grand banditisme.

## Personnes impliquées
- Benjamin (code)
- Emilien (code)

## Jalons du projet
- Définition des spécifications [en cours]

## Idées pour les specs du projet
- Un jeu basé sur du texte (console, ASCII). Le but pour le héros (avatar du joueur) étant d'évoluer dans une ville med-fan typique. Par "évoluer" on entend survivre, prospérer puis régner dans le "milieu" de la ville en question. Cela inclut différentes activités considérées comme illégales (vol, racket, assassinat, prostitution, traffic (drogues, armes, ???), corruption, terrorisme, ???)
- Le joueur commence avec de la vente de produits à la frontière de la légalité (cigarettes, alcool etc ...) ou alors commence directement dans l'illégal mais en bas de l'échelle (petit dealer, mule ...)
- Notion de gain, ex : il peut se contenter de rester petit dealer mais s'il veut monter son empire du mal, il faudra qu'il gagne plus et donc qu'il monte les échelons.

### Personnages
- Le héros peut recruter d'autres personnages (des sbires) au fur et à mesure pour l'aider dans sa "quête".
- Les différents personnages gagnent en expérience et donc en compétences. [Penser à faire un arbre de compétences]
- Les différents personnages peuvent être de sexe/race différents, avec ses avantages et inconvénients. [Penser à faire une liste des races et un tableau des bonus/malus]

#### Caractéristiques d'un personnage
- Caractéristiques opposées (crainte/sympathie, loyauté/autorité) qui marcheraient sur le principe d'un compteur de -10 à +10 (-7 signifiant 7 en crainte et 7 signifiant 7 en sympathie) ?

- Crainte inspirée
- Loyauté
- Influence
- Charisme
- Avidité
- Valeur morale (jusqu'où le personnage est capable d'aller)

#### Carrières des personnages (s'inspirer des classes de Warhammer JdR)
- Un système qui pourrait être cool, c'est celui des carrières dans les sims, on isole une carrière pour chaque domaine, et on imagine 10 (ou 5) niveaux pour chaque carrière, avec la possibilité si on a été un artisan légal dans le domaine d'attaquer au niveau 3 ou 4 par exemple.
- On monterait en grade avec l'expérience et parfois en ayant besoin d'objets (pour les fabriquants d'armes/drogue ...), d'un réseau (??? idée à creuser), d'une pièce spécifique ...
- Possibilité d'imaginer des carrières avec un tronc commun à 5 niveaux qui se spécialise en deux sous-carrière à partir du niveau 5 (ex. alchimiste qui devient fabriquant de drogue/fabriquant de poisons)
- On peut imaginer des synergies entre les carrières (du genre un assassin a plus de chance de réussir s'il y a un fabriquant de poison/d'arme dans le repère ...)

##### Titres légaux
- Buraliste
- Tavernier
- Forgeron
- Hérault

##### Titres illégaux
- Petit dealer 
- Mule
- Petite frappe
- Cambrioleur
- Câjoleuse / Gigolo
- Coupe-jarret
- Producteur de drogue

### Bâtiments
- Premier système : liste de bâtiments en dur, et on progresse petit à petit en achetant un nouveau (on peut imaginer débloquer des nouveaux "tiers" avec chaque achat)
<<<<<<< HEAD
- Petite grotte
- Grande grotte
- Petite cave
- Grande cave
- Chaumière
- Maison
- Château
- Forteresse de génie du mal
=======
	- Petite grotte
	- Grande grotte
	- Petite cave
	- Grande cave
	- Chaumière
	- Maison
	- Château
	- Forteresse de génie du mal
>>>>>>> 978722f03915b20774b01cca58c53032df8eaf8b

- Second système : un système de bâtiments avec une échelle portant sur la position du repère (montagnes/fôret/quartier pauvre/centre-ville/quartier riche) avec un système de bonus/malus pour certains domaines en fonction de la position (quartier riche + corruption = ++, quartier riche + racket = -- ...). Pour représenter la taille du repère et les bonus apportés, on peut aménager le repère avec des pièces à la Dungeon keeper (chambre = +4 capacité du repère, forge = +10% de réussite pour assassinats, traffic arme ...).

- Troisième système : mix des deux précédents avec une petite grotte ne pouvant contenir que trois pièces, une maison en contient 6 ...

### Coupures de presse
- Sorte de "grades" ou de "succès" qui servent de score/objectif/motivateur pour le joueur (Casanova : avoir 4 prostituées, Triades : atteindre le niveau x dans trois domaines différents, Requiem for a Dwarf : vendre de la cam' à 100 clients nains)

### Activités
- Drogue
- Prostitution
- Guilde de voleurs
- Guilde d'assassins∏

## Mots clés brut
- Système de corruption
- Notion de distance (Pour aller assassiner un personnage, ça prend plus ou moins de temps en fonction de la distance)
- Gangs
- Rascisme (au sens propre pour une fois)
- Arbre de technologiqes (on parlerait de "organisation" puisqu'on a pas vraiement de technologie mais plus des optimisations dans le fonctionnement de la mafia)
- Matérialiser les clients / indics / flics ... pour avoir plus de mécanismes d'interaction avec l'environnement
<<<<<<< HEAD
- Imaginer des peines de prison ? (Jusqu'à présent, un perso qui se fait choper est un perso mort, mais un qui part en prison peut redevenir disponible plus tard, avec des compétences en moins ... ou en plus)
=======
- Imaginer des peines de prison ? (Jusqu'à présent, un perso qui se fait choper est un perso mort, mais un qui part en prison peut redevenir disponible plus tard, avec des compétences en moins ... ou en plus)
>>>>>>> 978722f03915b20774b01cca58c53032df8eaf8b
