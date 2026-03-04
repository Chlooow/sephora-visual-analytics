import pandas as pd
import re

# Normalisons "size" car on ne peut pas avoir "oz" et "ml" dans la même colonne
def extraction_ml(size_str):
    if pd.isna(size_str):
        return None
    # si on a un virgule on transforme en point
    s = str(size_str).lower().replace(',','.').strip()

    # gestion des "no size" 
    if 'no size' in s:
        return None
    
    if '/' in s:
        s = s.split('/')[-1] # on garde que le chiffre en ml

    # Extraction des chiffres
    ml_match = re.search(r'(\d+(\.\d+)?)\s*(ml)', s)
    if ml_match:
        return round(float(ml_match.group(1)))

    # au cas ou si il n'y aurait pas de ml que que oz on convertit
    # 1 oz = 29.5735 ml
    oz_match = re.search(r'(\d+(\.\d+)?)\s*(oz)', s)
    if oz_match:
        return round(float(oz_match.group(1)) * 29.5735, 2)
    return None 