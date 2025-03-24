# #importation importante de mon TP 

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# # on charge le CSV titanic 
# df = pd.read_csv('./titanic-train.csv')



# # Imprimer les schémas du dataframe
# print('Question 1 : Imprimer les schémas du dataframe ')
# print(df.dtypes)


# # Comptez le nombre total de passagers dans le Titanic
# print('Question 2 : Comptez le nombre total de passagers dans le Titanic')
# print(df['PassengerId'].count())


# #Affichage de quelques lignes (5)
# print('Question 3 : Affichage de quelques lignes (5)')
# print(df.head())


# # Résumé des données, affichage des statistiques descriptives de notre dataframe
# print ('Question 4 : Résumé des données, affichage des statistiques descriptives de notre dataframe')
# print(df.describe())

# # sélectionner quelques fonctionnalités et vérifier les données

# print('Question 5 : sélectionner quelques fonctionnalités et vérifier les données')
# print('Pclass, Survived, Age leurs head qui est les 5 premières lignes')
# print(df[['Pclass', 'Survived', 'Age']].head())
# print('Pclass, Survived, Age leurs description')
# print(df[['Pclass', 'Survived', 'Age']].describe())
# print('Pclass, Survived, Age leurs types')
# print(df[['Pclass', 'Survived', 'Age']].dtypes)
# print('Pclass, Survived, Age leurs valeurs manquantes')
# print(df[['Pclass', 'Survived', 'Age']].isnull().sum())




# # Faisons une analyse exploratoire simple des données (EDA)

# # Affichage du nombre de survivants et de non survivants
# print('Question 6 : Affichage du nombre de survivants et de non survivants')

# sns.countplot(x='Survived', data=df, palette='Set2')
# plt.title('Répartition des survivants')
# plt.xticks([0, 1], ['Non Survivant', 'Survivant'])
# plt.show()


# # Virtualisation des classes par passagers

# sns.countplot(x='Pclass', data=df, palette='muted')
# plt.title('Répartition des classes par passagers')
# plt.xticks([0, 1, 2], ['1ére Classe', '2ème Classe', '3ème Classe'])
# plt.show()


# # Répartition des survivant en fonction du Sexe 

# sns.countplot(x='Sex', hue='Survived' ,data=df, palette='pastel')
# plt.title('Répartition des survivants en fonction du Sexe')
# plt.xlabel("Sexe")
# plt.ylabel("Nombre de passagers")
# plt.legend(['Non Survivant', 'Survivant'])
# plt.show()


# # Afficher les taux de survie par sexe
# survival_sex = df.groupby("Sex")["Survived"].mean()
# print(survival_sex)

# # Explication des résultats
# if survival_sex["female"] > survival_sex["male"]:
#     print("\nLes femmes avaient une bien meilleure chance de survie que les hommes.")
# else:
#     print("\nLes hommes avaient un taux de survie plus élevé, ce qui serait surprenant !")


# #histogramme des âges 
# plt.figure(figsize=(8, 5))
# sns.histplot(df['Age'].dropna(), bins=30, kde=True, color='blue')
# plt.title('Répartition des âges des passagers')
# plt.xlabel('Age')
# plt.ylabel('Nombre de passagers')
# plt.show()


# #Boxplot des tarifs en fonction de classe 
# plt.figure(figsize=(10, 6))

# # Création du boxplot avec swarmplot pour voir chaque point individuellement
# sns.boxplot(x='Pclass', y='Fare', data=df, palette='coolwarm', showfliers=False)  
# sns.stripplot(x='Pclass', y='Fare', data=df, color="black", alpha=0.3, jitter=True) 
# plt.title('Prix des billets selon la classe des passagers', fontsize=14)
# plt.xlabel('Classe de billet (1 = 1ère classe, 2 = 2ème classe, 3 = 3ème classe)', fontsize=12)
# plt.ylabel('Prix du billet (en monnaie Titanic)', fontsize=12)
# plt.show()



############   reformulation du code pour une meilleur expérience utilisateur ################### 


#Importation des bibliothèques
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

# Chargement du dataset Titanic
df = pd.read_csv('./titanic-train.csv')

#Question 1 : Affichage des schémas du dataframe
print("\n" + "="*50)
print("📊 QUESTION 1 : Schémas du DataFrame (Types de données)")
print("="*50)
print(df.dtypes)
print("\n")

# Question 2 : Nombre total de passagers
print("="*50)
print("📊 QUESTION 2 : Nombre total de passagers")
print("="*50)
print(f"Total Passagers : {df['PassengerId'].count()}")
print("\n")

#Question 3 : Affichage des premières lignes du dataset
print("="*50)
print("📊 QUESTION 3 : Aperçu des 5 premières lignes du dataset")
print("="*50)
print(df.head())
print("\n")

#Question 4 : Statistiques descriptives du dataset
print("="*50)
print("📊 QUESTION 4 : Statistiques descriptives du dataset")
print("="*50)
print(df.describe())
print("\n")

#Question 5 : Sélection de certaines colonnes et analyse
print("="*50)
print("📊 QUESTION 5 : Analyse de Pclass, Survived et Age")
print("="*50)
print("▶️ Aperçu des 5 premières lignes :\n", df[['Pclass', 'Survived', 'Age']].head(), "\n")
print("▶️ Statistiques descriptives :\n", df[['Pclass', 'Survived', 'Age']].describe(), "\n")
print("▶️ Types de données :\n", df[['Pclass', 'Survived', 'Age']].dtypes, "\n")
print("▶️ Valeurs manquantes :\n", df[['Pclass', 'Survived', 'Age']].isnull().sum(), "\n")

#Question 6 : Visualisation des survivants
print("="*50)
print("📊 QUESTION 6 : Répartition des survivants")
print("="*50)
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Répartition des survivants')
plt.xticks([0, 1], ['Non Survivant', 'Survivant'])
plt.show()

#Visualisation des classes de passagers
print("="*50)
print("📊 QUESTION 7 : Répartition des passagers par classe")
print("="*50)
sns.countplot(x='Pclass', data=df, palette='muted')
plt.title('Répartition des classes de passagers')
plt.xticks([0, 1, 2], ['1ère Classe', '2ème Classe', '3ème Classe'])
plt.show()

#Taux de survie par sexe
print("="*50)
print("📊 QUESTION 8 : Taux de survie par sexe")
print("="*50)
sns.countplot(x='Sex', hue='Survived', data=df, palette='pastel')
plt.title('Répartition des survivants en fonction du Sexe')
plt.xlabel("Sexe")
plt.ylabel("Nombre de passagers")
plt.legend(['Non Survivant', 'Survivant'])
plt.show()

#Affichage des taux de survie par sexe
survival_sex = df.groupby("Sex")["Survived"].mean()
print("\n▶️ Taux de survie par sexe :\n", survival_sex, "\n")

if survival_sex["female"] > survival_sex["male"]:
    print("✅ Les femmes avaient une bien meilleure chance de survie que les hommes.\n")
else:
    print("⚠️ Les hommes avaient un taux de survie plus élevé, ce qui serait surprenant !\n")

# Histogramme de la distribution des âges
print("="*50)
print("📊 QUESTION 9 : Distribution des âges des passagers")
print("="*50)
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution des âges des passagers')
plt.xlabel('Âge')
plt.ylabel('Nombre de passagers')
plt.show()

# 🔹 Boxplot des tarifs en fonction de la classe
print("="*50)
print("📊 QUESTION 10 : Prix des billets selon la classe des passagers")
print("="*50)
plt.figure(figsize=(10, 6))

# Création du boxplot avec swarmplot pour voir chaque point individuellement
sns.boxplot(x='Pclass', y='Fare', data=df, palette='coolwarm', showfliers=False)
sns.stripplot(x='Pclass', y='Fare', data=df, color="black", alpha=0.3, jitter=True)

plt.title('Prix des billets selon la classe des passagers', fontsize=14)
plt.xlabel('Classe de billet (1 = 1ère classe, 2 = 2ème classe, 3 = 3ème classe)', fontsize=12)
plt.ylabel('Prix du billet (en monnaie Titanic)', fontsize=12)
plt.show()


# Extraction du titre des noms
df['Initial'] = df['Name'].apply(lambda x: re.search(r"[A-Za-z]+\.", x).group(0))  # Extrait Mr., Mrs., Miss., etc.

# Affichage des différentes valeurs extraites
print("Différents titres trouvés dans le dataset :")
print(df['Initial'].unique())

# Remplacement des titres rares par des catégories plus générales
df['Initial'] = df['Initial'].replace(['Mlle.', 'Ms.'], 'Miss.')  # Mlle = Miss
df['Initial'] = df['Initial'].replace(['Mme.'], 'Mrs.')  # Mme = Mrs.
df['Initial'] = df['Initial'].replace(['Dr.', 'Rev.', 'Col.', 'Major.', 'Capt.', 'Jonkheer.', 'Don.', 'Sir.', 'Lady.', 'Countess.'], 'Other')

#Calcul des âges moyens par titre
print("\nMoyenne d'âge par titre :")
print(df.groupby('Initial')['Age'].mean())

# Remplacement des valeurs NaN en fonction du titre
df['Age'] = df.groupby('Initial')['Age'].transform(lambda x: x.fillna(x.mean()))

# Vérification après remplacement
print("\nValeurs manquantes après traitement :", df['Age'].isnull().sum())



