# Système de gestion des employés Python (English version below) 

Petit projet de cours : gestion d'employés avec un menu.
Les employés sont stockés dans un dictionnaire Python (clé = `id`).

# Fonctionnalités
- Rechercher un employé
- Ajouter un nouvel employé
- Modifier nom / département / titre
- Supprimer un employé
- Quitter le programme


# Concepts couverts
- Classe `Employé` (attributs, méthode `afficher_informations()`)
- Dictionnaire Python pour stocker les objets
- Saisie utilisateur (`input`), conditions, boucles
- Organisation avec des fonctions (ajouter, rechercher, etc.)

# Exécuter
```bash
python3 main.py
```
# Exemple

=== Menu ===
1. Rechercher un employé (47899, 39119, 81774)
2. Ajouter un nouvel employé
3. Modifier un employé
4. Supprimer un employé
5. Quitter
Choisissez une option (1-5): 2
Nom de l'employé: Alice
Numéro d'identification: 12345
Département: IT
Titre du poste: Développeuse
Employé ajouté.

<details>
  <summary>English (summary)</summary>

# Employee Management System — Python

Small course project: a menu-driven CLI to manage employees stored in a Python dictionary (`id` → `Employee` object).

## Key features
- Search an employee
- Add a new employee
- Edit name / department / title
- Delete an employee
- Quit

## Covered concepts
- `Employee` class (attributes, `display_information()` method)
- Python dictionary for storing objects
- User input (`input()`), conditionals, loops
- Organization with functions (add, search, edit, delete)

## Run
```bash
python3 main.py
Sample session
pgsql
Copier le code
=== Menu ===
1) Search an employee
2) Add a new employee
3) Edit an employee
4) Delete an employee
5) Quit

Choose an option (1-5): 2
Employee name: Alice
Employee ID: 12345
Department: IT
Job title: Developer
Employee added.

Choose an option (1-5): 1
Enter employee ID to search: 12345
[12345] Alice — IT — Developer







