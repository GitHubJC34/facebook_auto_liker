# Cas d'utilisation

Ce dépôt contient le code pour différents cas d'utilisation d'automatisation avec Selenium.

## FacebookAutoLiker

Le cas d'utilisation FacebookAutoLiker permet de :

- Se connecter à Facebook
- Rechercher un profil utilisateur cible
- Liker automatiquement les publications du profil cible

### Utilisation

```python
from selenium import webdriver
from use_cases.FacebookAutoLiker import FacebookAutoLiker

driver = webdriver.Chrome()
use_case = FacebookAutoLiker(driver)

use_case.login('mon_email', 'mon_mdp')
use_case.search_profile('profil_cible')
use_case.auto_like(100, 0.5) # 100 likes avec 0.5 sec entre chaque
```

### Fonctionnalités

```python 
login(email, password) #se connecte à Facebook

search_profile(profile_name) #recherche le profil cible

auto_like(max_likes, delay) #like automatiquement les publications
``` 