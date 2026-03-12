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

# nettoyage de "how to use" pour en faire une colonne binaire : instruction ou pas d'instruction
def clean_how_to_use(text):
    if pd.isna(text):
        return False
    
    s = str(text).lower().strip()

    # si ca commence par suggested usage = TRUE
    if 'suggested usage' in s:
        return True
    
    # sinon c'est no instruction = False
    if 'no instruction' in s or s == '' or s == 'unknown':
        return False
    
    # securité de logique 
    return len(s) > 20


# normalisation de la colonne d'options
def count_options(options_str):
    if pd.isna(options_str) or str(options_str).lower().strip() == 'no options':
        return 1
    
    s = str(options_str).strip()

    # on compte par nombre de -
    parts = [p for p in s.split(' - ') if p.strip()]

    return max(len(parts), 1)

# ajout d'une colonne gamme en fonction du value_price
def segment_prix(price):
    if price < 20:
        return 'access'
    elif price <= 50:
        return 'middle'
    elif price <= 100:
        return 'premium'
    else:
        return 'luxury'

# ajout du "brand_age"
def calculate_brand_age(year):
    try:
        y = int(year)   
        # precond : year aberrante
        if y <= 0 or y > 2026:
            return None
        return 2026 - y
    except (ValueError, TypeError):
        return None

# determiner le statut de la marque grace a son age
def brand_status(brandage):
    if brandage is None :
        return None
    elif brandage <= 5:
        return 'rookie'
    elif brandage <= 10:
        return 'emerging'
    elif brandage <= 30:
        return 'established'
    elif brandage <= 70:
        return 'classic'
    else :
        return 'heritage'
    
# regroupement des categories de produits
def mapping_categories(cat):
    c = str(cat).lower()

    # 1. TOOLS & ACCESSORIES
    if any(x in c for x in [
        'brush', 'dryer', 'iron', 'mirror', 'sponge', 'tweezers',
        'applicator', 'bag', 'case', 'sharpener', 'roller', 'comb',
        'spa tool', 'high tech', 'lid shadow', 'powder brush',
        'cleansing brush', 'facial cleansing'
    ]):
        return 'Tools & Accessories'
    if c in ['accessories', 'tools']:
        return 'Tools & Accessories'

    # 2. WELLNESS & OTHER
    if any(x in c for x in ['candle', 'diffuser', 'supplement', 'wellness', 'mini size', 'teeth whitening', 'holistic']):
        return 'Wellness & Other'
    if 'value' in c or 'gift set' in c:
        return 'Wellness & Other'

    # 3. FRAGRANCE
    if any(x in c for x in ['perfume', 'cologne', 'rollerball']):
        return 'Fragrance'
    if c == 'fragrance':
        return 'Fragrance'

    # 4. HAIR
    if any(x in c for x in [
        'shampoo', 'conditioner', 'scalp', 'color care', 'curls',
        'dry shampoo', 'leave-in', 'hair spray', 'hair oil',
        'hair primer', 'hair mask', 'hair thinning', 'hair loss',
        'hair styling', 'hair products', 'hair accessories', 'hair removal'
    ]):
        return 'Hair'
    if c == 'hair':
        return 'Hair'

    # 5. BATH & BODY
    if any(x in c for x in [
        'bath', 'shower', 'deodorant', 'shaving', 'aftershave',
        'body wash', 'body lotion', 'body oil', 'body moisturizer',
        'body spray', 'body sunscreen', 'body mist', 'body product',
        'for body', 'antiperspirant', 'cellulite', 'stretch mark',
        'self tanner', 'bubble bath', 'bath soak', 'lotions & oils'
    ]):
        return 'Bath & Body'
    if c in ['body', 'bath & body', 'shaving']:
        return 'Bath & Body'

    # 6. MAKEUP (avant Skincare — évite que primer/remover partent en soin)
    if any(x in c for x in [
        'foundation', 'concealer', 'blush', 'bronzer', 'mascara',
        'eyeliner', 'eyeshadow', 'eyebrow', 'eyelash', 'eye set',
        'eye palette', 'eye primer', 'lip gloss', 'lip liner',
        'lip stain', 'lip plumper', 'lipstick', 'liquid lipstick',
        'lip set', 'nail', 'highlighter', 'contour', 'color correct',
        'bb & cc', 'cheek', 'palette', 'primer', 'setting spray',
        'setting powder', 'blotting', 'false eyelash', 'makeup',
        'tinted moisturizer', 'face set'
    ]):
        return 'Makeup'

    # 7. SKINCARE
    if any(x in c for x in [
        'anti-aging', 'acne', 'blemish', 'sunscreen', 'sun care',
        'eye cream', 'eye mask', 'eye treatment', 'night cream',
        'face mask', 'face serum', 'face wash', 'face oil',
        'face wipe', 'face sunscreen', 'facial peel', 'hand cream',
        'foot cream', 'moisturizer', 'cleanser', 'cleansing', 'toner',
        'essence', 'mist', 'exfoliat', 'scrub', 'treatment', 'peel',
        'serum', 'balm', 'lip balm', 'lip treatment', 'lip sunscreen',
        'sheet mask', 'decollete', 'neck cream', 'after sun',
        'skincare', 'for face', 'remover'
    ]):
        return 'Skincare'

    return 'Other'
