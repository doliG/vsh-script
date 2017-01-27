# Automatisation d'impressions
Le but est de créer un script pour automatiser l'impression des photos que les clients laissent à la borne.

## Principe
Le client passe à la borne. Il choisit les photos qu'il veut imprimer. Les photos sont copiées de son support vers le stockage de la borne, dans le chemin relatif suivant :
```
tirages/[numéroClient]/[formatPapier]/[finitionPapier]/
```
Avec :
- numeroClient : int (par ex 000558)
- formatPapier : int (une seule possibilité : 152*102)
- finitionPapier : string
 - glossy (papier brillant, on imprime)
 - mat (**ne doit pas être traité**)

Voici un exemple de chemin :
```
tirages/000558/152x102/glossy/fill
```

**IMPORTANT :** Nom exacte des dossiers `mat/` et `glossy/` à vérifier.

## Fonctionnement du script
1. Scan régulier du dossier `tiarges/`
2. Detection d'un nouveau dossier : **attente jusqu'a la fin de la copie des photos !important**
3. On entre dans `[nouveauDossier]/152x102/`, recherche à l'interieur d'un dossier nommé `glossy/`.
4.
 - **Si** le dossier `glossy/` n'existe pas, arrêt script
 - **Sinon**, copie de tous les fichiers `.jpg` dans `glossy/` vers `HOTFOLDER/`
