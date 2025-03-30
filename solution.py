# Importation des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv('data/data-2019.csv')

# Calcul de la moyenne du score de bonheur par région
average_happiness_by_region = df.groupby('Region')['Score 2019'].mean().reset_index()

# Trier le résultat pour voir les régions avec les meilleurs scores de bonheur en premier
average_happiness_by_region = average_happiness_by_region.sort_values(by='Score 2019', ascending=False)

# Afficher le classement de la moyenne du score de bonheur par region  
print(average_happiness_by_region)

# Classer les pays par GDP par habitant et afficher les top 10 et bottom 10
top_10_gdp = df[['Country', 'GDP 2019']].sort_values(by='GDP 2019', ascending=False).head(10)
bottom_10_gdp = df[['Country', 'GDP 2019']].sort_values(by='GDP 2019', ascending=True).head(10)

# Afficher les 10 premiers
print("Top 10 des pays par GDP :")
print(top_10_gdp)

# Afficher les 10 derniers
print("\nBottom 10 des pays par GDP :")
print(bottom_10_gdp)

# Calcul de la corrélation entre GDP et le score de bonheur
correlation = df[['GDP 2019', 'Score 2019']].corr()

print("Corrélation entre GDP et le score de bonheur :")
print(correlation)

# Créer un graphique de dispersion pour GDP vs score de bonheur
plt.figure(figsize=(10, 6))
plt.scatter(df['GDP 2019'], df['Score 2019'], color='blue', alpha=0.5)
plt.title('GDP vs Score de Bonheur')
plt.xlabel('GDP par habitant')
plt.ylabel('Score de Bonheur')
plt.grid(True)

# Sauvegarder les résumés statistiques sous forme de fichiers CSV
average_happiness_by_region.to_csv('average_happiness_by_region.csv', index=False)
top_10_gdp.to_csv('top_10_gdp.csv', index=False)
bottom_10_gdp.to_csv('bottom_10_gdp.csv', index=False)

# Sauvegarder le graphique sous forme d'image
plt.savefig('gdp_vs_happiness.png')
plt.show()