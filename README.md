# Automatisation d'impressions

Le but est de créer un script pour automatiser l'impression des photos que les clients laissent à la borne.

**SOMMAIRE :**
- Principe
- Focntionnement du script
- Langages utilisés
- Ressources
 - Langages utilisés
 - Liens utiles
 - Commandes utiles

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
 - mat (**autre traitement, à voir dans un second temps**)

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


## Ressources

### Langages utilisés
Dans la mesure du possible, nous voudrions utiliser du `batch`.

Cependant, il n'est pas possible de détecter lorsque un nouveau dossier est créé avec du batch. Il faut donc soit passer un script de detection en boucle qui cherche un dossier en fonction de sa **date de création** (possible en shell, à voir en batch), soit utiliser `powershell`.


### Liens utiles

- [Search by date using command-line, Stackoverflow](http://stackoverflow.com/questions/9234207/search-by-date-using-command-line)
- [Monitor a folder and trigger a command-line action when a file is created](http://superuser.com/questions/226828/how-to-monitor-a-folder-and-trigger-a-command-line-action-when-a-file-is-created)
- [Batch - ouvrir deux fenêtres avec un seul script](https://openclassrooms.com/forum/sujet/batch-ouvrir-deux-fenetres-avec-un-seul-script-28126)
- [shutil - lib py](https://docs.python.org/3.6/library/shutil.html#shutil.copy)
- [stat - lib py](https://docs.python.org/3.6/library/stat.html) (pour savoir quand la copie est finie : `stat.S_ISREG(mode)`)


### Commandes utiles

Ouvrir un nouveau terminal dans un dossier spécifique :
```batch
start cmd /K "cd [PATH]"
```


### Notes

Idéalement, il faudrait que la fonction `isItId()` travaille avec les regex.
