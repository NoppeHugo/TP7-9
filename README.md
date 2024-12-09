# Classe Fraction et Tests Unitaires

Ce projet contient une classe `Fraction` permettant de représenter et manipuler des fractions, ainsi qu'une suite de tests unitaires pour garantir son bon fonctionnement.

## Aperçu des fichiers

### `fractions.py`
Ce fichier définit la classe `Fraction`, qui propose :
- L'initialisation et la réduction des fractions à leur forme simplifiée.
- Des méthodes pour l'addition, la soustraction, la multiplication et la division de fractions.
- Des méthodes utilitaires comme `is_zero`, `is_integer`, `is_proper`, `is_unit`, et `is_adjacent_to`.
- Le support pour la représentation des fractions en nombres mixtes, les comparaisons d'égalité, et la conversion en nombre décimal.

### `test_fractions.py`
Ce fichier contient des tests unitaires pour la classe `Fraction`, écrits avec le module `unittest`. Ces tests valident :
- La bonne initialisation et simplification des fractions.
- La gestion des entrées incorrectes (par exemple, un dénominateur nul).
- Les opérations mathématiques sur les fractions.
- Les méthodes et propriétés utilitaires.

## Comment utiliser

### Prérequis
- Assurez-vous que Python 3.x est installé sur votre système.
- Aucune dépendance supplémentaire n'est nécessaire en dehors des bibliothèques standard de Python.

### Exécution du code
1. Sauvegardez les fichiers `fractions.py` et `test_fractions.py` dans le même dossier.
2. Pour utiliser la classe `Fraction` :
   ```python
   from fractions import Fraction
   
   f1 = Fraction(3, 4)
   f2 = Fraction(2, 3)
   resultat = f1 + f2
   print(resultat)  # Exemple d'addition de fractions

3. Pour executer les tests :

python -m unittest test_fractions.py

