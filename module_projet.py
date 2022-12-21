
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from math import sin, cos, acos, pi
  
pd.options.mode.chained_assignment = None  # default='warn'


### Définition des dataframes avec leurs colonnes "utiles"
def data_carb(df, carb, colonnes_utiles):
    data_1 = df[df.prix_nom == carb]
    d = data_1[colonnes_utiles]
    d.drop_duplicates(keep = 'first', inplace=True) 
    return d

### Fonction pour passer de coordonnées GPS à une adresse et inversement

def Adresse_to_gps(Adresse) : 
    geolocator = Nominatim(user_agent="arman.akgonul@ensae.fr")
    location = geolocator.geocode(Adresse)
    return str(str(location.latitude) + ','+ str(location.longitude))

def Gps_to_adresse(coord):
    geolocator = Nominatim(user_agent="arman.akgonul@ensae.fr")
    location = geolocator.reverse(coord)
    return location 


### Fonctions pour calculer la distance entre 2 points à partir de coordonnées GPS
def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m/60 + s/3600
 
def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd-d)*60
    m = int(x)
    s = (x-m)*60
    return d, m, s
 
def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd/180*pi
 

def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd/pi*180
 
#############################################################################
def distanceGPS(p1, p2):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    latA, longA = p1
    latB, longB = p2
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(sin(latA)*sin(latB) + cos(latA)*cos(latB)*cos(abs(longB-longA)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S*RT

### Fonctions finales 

def dix_plus_proche_card(df, posi, carb):
    data_1 = data_carb(df, carb, ['adresse', 'ville', 'geom', 'prix_valeur', 'prix_nom']).sort_values('prix_valeur')
    pos = list(map(float,Adresse_to_gps(posi).split(',')))
    def distancetoposi(p2):
        pos_carb = list(map(float, p2.split(',')))
        return distanceGPS(pos, pos_carb)
    new_df = data_1['geom'].apply(distancetoposi).sort_values().head(10)
    return data_1.loc[new_df.index.to_list()]

### fonctions donnant itinéraires en Île-De-France

def create_graph(loc, dist, transport_mode, loc_type="address"):
###Transport mode = ‘walk’, ‘bike’, ‘drive’, ‘drive_service’, ‘all’, ‘all_private’, ‘none’
    if loc_type == "address":
        G = ox.graph_from_address(loc, dist=dist, network_type=transport_mode)
    elif loc_type == "points":
        G = ox.graph_from_point(loc, dist=dist, network_type=transport_mode )
    return G

G = create_graph("Ile de France", 50000, "drive")

G = ox.add_edge_speeds(G) #Impute
G = ox.add_edge_travel_times(G)
G = ox.distance.add_edge_lengths(G) 

def itinéraire(position, station): #attention il faut mettre (longitude, latitude)
    a,b = position
    x,y = station
    start_node = ox.nearest_nodes(G, a,b)
    end_node = ox.nearest_nodes(G, x,y) # Calculate the shortest path
    route = nx.shortest_path(G, start_node, end_node, weight='length') #Plot the route and street networks
    length = nx.shortest_path_length(G, source=start_node, target=end_node, weight='length', method="dijkstra")
    return(route, length)

def x_plus_proche(data, position, carb, nbr_stations):
    data_1 = md.data_carb(data, carb, ['adresse', 'ville', 'prix_valeur', 'prix_nom', 'geom'])
    pos = list(map(float,md.Adresse_to_gps(position).split(',')))
    def iti(station):
        pos_sta = list(map(float, station.split(',')))
        return(itinéraire(pos, pos_sta)[1])
    vector = data_1['geom'].apply(iti).sort_values().head(nbr_stations)
    return(vector)
