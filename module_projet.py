
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

def Adresse_to_gps2(Adresse) : 
    geolocator = Nominatim(user_agent="arman.akgonul@ensae.fr")
    location = geolocator.geocode(Adresse)
    return str(str(location.longitude) + ','+ str(location.latitude))

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
    data_1 = data_carb(df, carb, ['adresse', 'ville', 'geom', 'prix_valeur', 'prix_nom'])
    pos = list(map(float,Adresse_to_gps(posi).split(',')))
    def distancetoposi(p2):
        pos_carb = list(map(float, p2.split(',')))
        return distanceGPS(pos, pos_carb)
    new_df = data_1['geom'].apply(distancetoposi).sort_values().head(10)
    return data_1.loc[new_df.index.to_list()]

### fonctions donnant itinéraires en Île-De-France

