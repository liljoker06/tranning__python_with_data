# Titanic Dataset - Analyse et Exploration des Données

## Description de l'Exercice
Ce projet a pour objectif d'explorer et d'analyser le dataset Titanic à l'aide de Python et des bibliothèques Pandas, Seaborn et Matplotlib. Nous allons :

- Charger et comprendre la structure des données
- Analyser des statistiques descriptives
- Effectuer une analyse exploratoire des données (EDA)
- Nettoyer et traiter les valeurs manquantes
- Visualiser des tendances et corrélations dans les données

---

## Prérequis
Avant d'exécuter le script, assurez-vous d'avoir installé les bibliothèques suivantes :

```sh
pip install pandas seaborn matplotlib
```

---

## Contenu du Script

### 1. **Chargement des Données**
Le dataset est chargé depuis le fichier `titanic-train.csv`.

### 2. **Exploration des Données**
- Affichage des types de données et des informations générales
- Nombre total de passagers
- Aperçu des premières lignes du dataset
- Statistiques descriptives globales
- Analyse ciblée de certaines colonnes : `Pclass`, `Survived`, `Age`

### 3. **Analyse Exploratoire des Données (EDA)**
- Répartition des survivants
- Répartition des classes
- Taux de survie par sexe
- Distribution des âges
- Analyse des tarifs selon la classe

Des visualisations sont générées à l'aide de Seaborn et Matplotlib.

### 4. **Nettoyage et Traitement des Données**
- Extraction des titres des noms (Mr, Mrs, Miss, etc.) pour mieux analyser l'âge
- Remplacement des valeurs `NaN` dans `Age` par la moyenne des groupes basés sur le titre

---

## Exécution du Script
Lancez le script avec Python :
```sh
python titanic_analysis.py
```
Le script affichera des statistiques, des graphiques et des conclusions basées sur l'analyse des données.

---

## Exemples de Sorties Attenues

**Taux de Survie par Sexe :**
```
Sex
female    0.74  (74% des femmes ont survécu)
male      0.19  (Seulement 19% des hommes ont survécu)
```

**Moyenne d'âge par Titre :**
```
Initial
Master.    4.57
Miss.     21.80
Mr.       32.37
Mrs.      35.90
Other     45.88
```

**Valeurs Manquantes Apres Traitement :**
```
Valeurs manquantes après traitement : 0
```

---

## Améliorations Possibles
- Entraîner un modèle de Machine Learning pour prédire la survie
- Explorer d'autres corrélations entre les variables
- Améliorer le prétraitement des données

---

## Auteur
Projet réalisé dans le cadre d'une analyse de données avec Python.
LILJOKER 

🚀 Bon apprentissage et exploration du Titanic Dataset !