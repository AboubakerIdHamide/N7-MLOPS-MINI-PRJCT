# mlops-ml-project — baseline ML reproductible

Projet de classification Iris conçu pour fournir une baseline simple et reproductible. La configuration du modèle et du découpage des données se trouve dans `config/train.yaml`.

## Prérequis

- Python 3.10 ou une version plus récente
- `pip`

## Installation

Depuis la racine du projet, créez et activez un environnement virtuel, puis installez les dépendances :

```bash
python -m venv .venv
```

Linux / macOS :

```bash
source .venv/bin/activate
```

Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Installez ensuite les dépendances :

```bash
pip install -r requirements.txt
```

## Entraînement

Depuis la racine du projet, lancez :

```bash
python scripts/train.py
```

Le script charge la configuration, sépare les données en ensembles d'entraînement et de test (avec `random_state` et `test_size` définis dans le YAML), entraîne le pipeline, puis affiche l'accuracy et le F1 macro sur le jeu de test.

## Évaluation

```bash
python scripts/evaluate.py
```

Cette commande génère un rapport de classification dans `artifacts/report.json`.

**Note :** le script actuel calcule ce rapport sur l'ensemble du dataset, y compris les exemples d'entraînement. Son score est donc optimiste et ne doit pas être interprété comme une mesure indépendante des performances du modèle.

## Tests

```bash
python -m pytest -q
```

Les tests vérifient la présence des sections de configuration, la validité de `test_size` et le chargement d'un dataset non vide.

## Artefacts générés

Les fichiers ci-dessous sont créés dans `artifacts/` et ne sont pas versionnés dans Git :

- `model.joblib` : pipeline entraîné (prétraitement et modèle)
- `metrics.json` : accuracy et F1 macro sur le jeu de test
- `confusion_matrix.png` : matrice de confusion du jeu de test
- `report.json` : rapport de classification détaillé produit par le script d'évaluation

Pour reproduire les résultats, utilisez la même configuration et les mêmes versions de dépendances. Les données Iris sont fournies par scikit-learn ; une source CSV peut être configurée dans `config/train.yaml` en réglant `data.kind` sur `csv` et en indiquant le chemin et la colonne cible.
