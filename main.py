# main.py
from entities.User import User
from adapters.SeleniumAdapter import SeleniumAdapter


def main():

    print("*"*45)
    print("*"*10, "BOT FACEBOOK AUTO LIKER", "*"*10)
    print("*"*45)

   # Créez une instance de l'utilisateur
    user = User(username='my_username', password='my_password')

    target_user = User(username='target_username')

    # Créez une instance de l'adaptateur Selenium
    web_driver = SeleniumAdapter()

    # Connectez-vous à Facebook
    web_driver.login(user)

    # Créez une instance du cas d'utilisation
    web_driver.recherche(target_user)
    web_driver.facebook_auto_liker(100, 0.3)

    # Fermez le navigateur à la fin
    web_driver.quit()


if __name__ == "__main__":
    main()
