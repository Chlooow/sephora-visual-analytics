# Sephora Visual Analytics

Projet réalisé dans le cadre de l'**UE Visualisation des données massives** — Master 1 Informatique et Big Data (IBD).

---

## 🎯 Problématique

> **Comment Sephora peut-elle optimiser son portefeuille de produits en s'appuyant sur la satisfaction et l'engagement client tout en renforçant son positionnement premium ?**

L'objectif est d'explorer les données produits du site Sephora afin d'identifier des leviers d'action concrets : quelles catégories et marques génèrent le plus d'engagement client ? Quels produits affichent une forte satisfaction malgré un prix élevé ? Y a-t-il des segments sous-exploités ou au contraire sursaturés ?

---

## 📊 Dashboard Tableau Public

Le dashboard interactif est publié en ligne et accessible via le lien ci-dessous :

🔗 **[Voir le dashboard sur Tableau Public](https://public.tableau.com/views/Classeur1_17726676383620/Dashboard01-Catalogue?:language=fr-FR&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

Il comprend plusieurs vues interactives (catalogue produits, analyse des marques, satisfaction client, positionnement prix) avec filtres et actions croisées entre visualisations.

---

## 🗂️ Arborescence du projet

```
sephora-visual-analytics/
│
├── Classeur/                                        # Fichiers Tableau
│   └── Sephora_Analytics_Makoundou_2026.twbx        # Classeur Tableau exporté (.twbx)
│
├── data/                                            # Données
│   ├── orginal_data/                                # Données brutes d'origine (archive zip Kaggle)
│   ├── helps/                                       # Fichiers de référence et d'enrichissement
│   │   ├── Brand_references_filled.csv/.xlsx        # Référentiel marques complété
│   │   ├── brands_reference.csv                     # Référentiel marques initial
│   │   ├── categories.csv                           # Référentiel catégories
│   │   ├── categories_univers.csv                   # Catégories avec univers
│   │   └── sephora_website_dataset_enriched.csv     # Dataset enrichi
│   ├── data_cleaned/                                # Données nettoyées prêtes pour Tableau
│   │   └── sephora_clean_final_2026.csv             # Dataset final utilisé dans le dashboard
│   └── sephora_website_dataset.csv                  # Dataset principal brut
│
├── notebooks/                                       # Notebooks Jupyter (exploration & nettoyage)
│   ├── 00-eda-brouillon.ipynb                       # Brouillon d'exploration (EDA)
│   └── 00-eda-clean.ipynb                           # Exploration propre et documentée
│
├── rapport/                                         # Documents de rendu
│   ├── enonce-projet.md                             # Énoncé officiel du projet
│   └── note-methodologique-Sephora-CM.pdf           # Note méthodologique (démarche, justifications, limites)
│
├── utils/                                           # Scripts Python utilitaires
│   ├── brand.py                                     # Traitement et enrichissement des données marques
│   └── outils.py                                    # Fonctions utilitaires générales
│
├── .gitattributes
├── LICENSE
└── README.md
```

---

## 📦 Dataset

Source : **Kaggle — All products available on Sephora website**  
🔗 https://www.kaggle.com/datasets/raghadalharbi/all-products-available-on-sephora-website

Le dataset contient des informations sur les produits disponibles sur le site Sephora : nom, marque, catégorie, prix, note moyenne, nombre d'avis, etc.

---

## 🛠️ Démarche

1. **Exploration et nettoyage** des données brutes via des notebooks Jupyter (`notebooks/`)
2. **Enrichissement** du dataset avec des référentiels de marques et catégories (`data/helps/`)
3. **Production du dataset final** utilisé dans Tableau (`data/data_cleaned/`)
4. **Conception du dashboard** interactif dans Tableau Public (`Classeur/`)
5. **Rédaction de la note méthodologique** (`rapport/note-methodologique-Sephora-CM.pdf`)

---

## 📋 Contexte académique

| Élément        | Détail                                      |
|----------------|---------------------------------------------|
| UE             | Visualisation des données massives          |
| Formation      | Master 1 Informatique et Big Data (IBD)     |
| Outil          | Tableau Public                              |
| Travail        | Individuel                                  |
| Soutenance     | 02 avril 2026                               |
