# Application pour trouver la meilleure station essence proche de chez soi

Suite à la crise énergétique qu'a enclenché la guerre entre l'Ukraine et la Russie, les prix des carburants ont explosé et malgré les mesures mise en place par le gouvernement pour contrer cet effet, il est devenu dur pour de nombreux usagers de se fournir du carburant au meilleur prix.
C'est pour cela que nous avons voulu à travers ce projet créer une application, à vrai dire plutôt les codes permettant de créer une application pour aider les usagers de la route et permettre à chacun de trouver la station la plus "rentable" avec son carbuarant. En effet, notre code permet aux usagers de trouver la station essence où le plein leur reviendra le moins cher en prenant en compte la distance de la station (nous avons choisi une consommation moyenne de 6L/100Km) et le prix du carburant dans cette station. En un mot, notre programme indique s'il vaut mieux aller plus loin pour payer moins cher ou non.  

### Nos objectif principaux et les problèmes que nous avons rencontrés

Nos objectifs : notre projet que nous avons tenté de résumer en un parapgrahe ci-dessus se décompose en plusieurs étapes progressives. 

1.la visualisation : 

Tout d'abord nous avons fait une analyse visuelle des données à notre disposition pour justifier l'interet et la faisabiltié du projet. Nous avons aussi pu nous familiariser avec les jeux de données par la même occasion.

2. dix plus proches stations avec geopanda :

3. dix plus proches stations avec panda et une fonction de distance : (à justifier : c'est plus rapide qu'avec géopanda), 

4. les itinéraires : 

5. fonction pour la station la plus rentable : 

Nous pouvons enfin ici travailler sur l'objectif principal du projet. En effet, dans cette partie, nous avons mis au point une fonction qui calcule le prix d'un plein en fonction du prix du carburant et de la distance de la station. C'est pas ce biais que nous avons pu obtenir le résultat éscompté d'afficher la station essence la plus rentable. 
 
(voir si c'est le même résultat avec la méthode de 2. ou de 3. ) 6. modélisation (il faut vrmt trouver vite pour ça)

Ce que nous avons fait :



Les limites : 

Pour réduire la complexité algorithmique, principalement de la création des graphes, nous nous sommes restreints à une analyse régionale. En effet, générer un graphe de la France entière est très gourmand. Or, nous utilisons le graphe pour calculer les itinéraires, mais surtout la distance routière entre un point A et un point B. Une amélioration évidente de notre projet serait de trouver un moyen plus léger de calculer ces distances et itinéraires afin de pouvoir travailler sur l'intégralité du territoire. 

### Les différents notebooks de notre projet :

Module_projet : module regroupant l'ensemble des fonctions définient lors du projet (pour ne pas se répéter dans les notebooks)

1. Visualisation : Récupération des données ainsi que visiualisation des variables les plus utiles pour notre projet 
2. iti (nom à changer) : essai de deuxième objectif avec géopanda
3. intro : essai du second objectif avec panda 
4. gpd (il faut enlever ce qui se recoupe entre 2. 3. et celui là) : affichage des itinéraires 
5. Rentabilité : fonction pour trouver la station la plus rentable 
6. il faut modéliser

