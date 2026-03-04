import pandas as pd

# Ce script a pour but de créer un fichier de référence pour les marques 
# présentes dans notre dataset, afin de pouvoir les mapper 
# avec des informations supplémentaires telles que le pays d'origine, 
# l'année de fondation

# Charger le dataset
df = pd.read_csv('../data/sephora_website_dataset.csv')

# Extraire les marques uniques, les nettoyer et les trier
brands_unique = pd.DataFrame(df['brand'].unique(), columns=['brand'])
brands_unique = brands_unique.sort_values(by='brand').reset_index(drop=True)

# Ajouter des colonnes vides à remplir
brands_unique['country_founding'] = ''
brands_unique['year_founding'] = ''
brands_unique['parent_group'] = '' # Bonus : LVMH, L'Oréal, Estée Lauder...

# Sauvegarder pour remplissage
brands_unique.to_csv('../data/brands_reference.csv', index=False)

print(f"Fichier créé avec {len(brands_unique)} marques à mapper.")