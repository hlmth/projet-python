# Application pour trouver la meilleure station essence proche de chez soi

Suite à la crise énergétique qu'a enclenché la guerre entre l'Ukraine et la Russie, les prix des carburants ont explosé et malgré les mesures mise en place par le gouvernement pour contrer cet effet, il est devenu dur pour de nombreux usagers de se fournir du carburant au meilleur prix.
C'est pour cela que nous avons voulu à travers ce projet créer une application, à vrai dire plutôt les codes permettant de créer une application pour aider les usagers de la route et permettre à chacun de trouver la station la plus "rentable" avec son carburant. En effet, notre code permet aux usagers de trouver la station essence où le plein leur reviendra le moins cher en prenant en compte la distance de la station (nous avons choisi une consommation moyenne de 6L/100Km) et le prix du carburant dans cette station. En un mot, notre programme indique s'il vaut mieux aller plus loin pour payer moins cher ou non.  

### Nos objectif principaux et les problèmes que nous avons rencontrés

Nos objectifs : notre projet que nous avons tenté de résumer en un parapgrahe ci-dessus se décompose en plusieurs étapes progressives. 

1.la visualisation : 

Tout d'abord nous avons fait une analyse des données à notre disposition pour justifier l'intérêt et la faisabiltié du projet. Nous avons aussi pu nous familiariser avec les jeux de données par la même occasion.

2. Les dix plus proches stations avec geopandas : 

Nous voulions d'abord voir s'il était possible de proposer à l'usager les 10 stations les plus proches de chez lui. Pour cela, nous avons utilisé le module geopandas puisque des données geojson étaient disponibles et car nous nous étions familiarisé avec le module en cours. Cepdendant ce premier essai n'a pas était concluant.

3. Les dix plus proches stations avec pandas et une fonction distance :

Nous avons donc continué avec des dataframes classiques et une fonction qui calcule la distance en métre et deux points GPS. Les résultats ont été beaucoup plus concluant et cela nous à permis d'avancer vers l'objectif principal de notre projet.

 
4. fonction pour la station la plus rentable : 

Nous pouvons enfin ici travailler sur l'objectif principal du projet. En effet, dans cette partie, nous avons mis au point une fonction qui calcule le prix d'un plein en fonction du prix du carburant et de la distance de la station. C'est pas ce biais que nous avons pu obtenir le résultat éscompté, à savoir déterminer la station essence la plus rentable. Cette station la plus rentable l'est bien à condition que l'on calcule la distance réelle et non celle à vol d'oiseau. C'est pour cela, que nous avons utilisé des outils permettant de calculer des itinéraires ainsi que leurs longueurs.

 

5. modélisation 

Nous n'avons pas pu produire de code pour cette partie par manque de donnée mais si l'application venait à être utilisée par le grand pubic, nous pourions au début proposer aux utilisateurs plusieurs choix de station ayant des caractéristiques de prix et de distance différentes pour créer une base de données. À partir de cette base, nous pourions alors faire une régression linéaire sur le prix et la distance pour élire les stations qui ont le meilleur rapport accessibilité par voie routière-prix et donc les conseiller à nos utilisateurs. 


Les limites : 

Pour réduire la complexité algorithmique, principalement de la création des graphes, nous nous sommes restreints à une analyse régionale. En effet, générer un graphe de la France entière est très gourmand. Or, nous utilisons le graphe pour calculer les itinéraires, mais surtout la distance routière entre un point A et un point B. Une amélioration évidente de notre projet serait de trouver un moyen plus léger de calculer ces distances et itinéraires afin de pouvoir travailler sur l'intégralité du territoire. 

### Les différents notebooks de notre projet :

Module_projet : module regroupant l'ensemble des fonctions définient lors du projet (pour ne pas se répéter dans les notebooks)

1. Visualisation : Récupération des données ainsi que visiualisation des variables les plus utiles pour notre projet 
2. Géopandas :  les 10 plus proches stations avec géopandas
3. Pandas et distance : les 10 plus proches stations avec pandas et une fonction distance 
4. Rentabilité : fonction pour trouver la station la plus rentable, calcul d'itinéraire


