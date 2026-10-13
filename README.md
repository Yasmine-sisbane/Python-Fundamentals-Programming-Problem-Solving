# TP1 Python — Partie 1

Projet de TP comprenant les six exercices de programmation présents dans le notebook de départ.

## Contenu du dépôt

- `TP1python_partie1_corrige.ipynb` : notebook corrigé, avec **sorties obtenues par exécution Python**.
- `Reponses_TP1_Python.docx` : explications et réponses aux six exercices.
- `captures/` : six captures PNG extraites de l'affichage HTML du notebook exécuté (preuve des sorties de test).
- `execution_TP1.html` : affichage HTML autonome du notebook exécuté.
- `tests/test_tp.py` : tests automatiques sur plusieurs cas (y compris conditions limites).

## Reproduire l'exécution

1. Installer Python 3 et Jupyter Notebook / JupyterLab (ou utiliser Google Colab).
2. Ouvrir `TP1python_partie1_corrige.ipynb`.
3. Faire **Kernel > Restart Kernel and Run All Cells**, puis saisir les données demandées dans les cellules interactives.
4. Comparer les affichages aux sorties de test sauvegardées.

Entrées utilisées dans les sorties sauvegardées :

- Ex. 1 : `CNE123456`, `16`, `14`, `2`, `3`.
- Ex. 2 : `1`, `-3`, `2`.
- Ex. 3 : `4`, `3.5`, `5`.
- Ex. 5 : `5`, `10`, `9`, `12`, `14`, `16`, `18`.

**Transparence :** les entrées ont été injectées dans l'exécuteur Python pour créer des sorties de démonstration reproductibles. Les captures montrent réellement les sorties rendues du notebook, mais ne constituent pas une capture d'une session interactive humaine dans Jupyter.

La cellule d'explication `while condition:` du fichier initial était un exemple de syntaxe, non exécutable tel quel ; elle a été remplacée par une démonstration `while` fonctionnelle pour que le notebook soit intégralement exécutable.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Rendu sur GitHub

1. Créer un nouveau dépôt GitHub public (ou privé si l'enseignant y a accès), par exemple `TP1-Python-Partie1`.
2. Importer tous les fichiers de ce dossier (en conservant `captures/` et `tests/`).
3. Vérifier que le notebook, le document et les captures sont visibles.
4. Remettre à l'enseignant **seulement le lien du dépôt GitHub**.
