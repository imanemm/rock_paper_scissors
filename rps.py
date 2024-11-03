#Projet de roche, papier, ciseaux
#19 septembre 2024

import random

def play_round():
    #Définition des options possibles
    options = [ "rock", "paper", "scissors"]

    #Choix du joueur
    op_joueur = input("Please choose between rock, paper and scissors: ").lower()

    while op_joueur not in options:
        print("This is not an option, please choose between rock, paper and scissors: ")
        op_joueur = input("Please choose between rock, paper and scissors: ").lower()

    #Génération du choix de l'ordinateur
    op_ordi = random.choice(options)
    print(f"The computer chose: {op_ordi}.", '\n')


    #Détermination du gagnant
    if op_joueur == op_ordi:
        print("It's a tie")
        return 

    elif op_joueur == "rock":
        if op_ordi == "scissors":
            print("You win ;) Rock beats Scissors.", '\n')
            return "joueur"

        else:
            print("You lose :/ Paper beats rock", '\n')
            return "ordinateur"
            
            
    elif op_joueur == "paper":
        if op_ordi == "rock":
            print("You win ;) Paper beats rock.", '\n')
            return "joueur"
        
        else:
            print("You lose :/ Scissors beats paper", '\n')
            return "ordinateur"

    elif op_joueur == "scissors":
        if op_ordi == "paper":
            print("You win ;) Scissors beats paper.", '\n')
            return "joueur"
        else:
            print("You lose :/ Rock beats Scissors", '\n')
            return "ordinateur"
        
def best_of_five():
    #Compteur des scores des joeurs
    score_joueur = 0
    score_ordi = 0
    max_wins = 3
    
    #Le but est de jouer jusqu'à ce qu'un joueur obtienne 3 wins
    while score_joueur < max_wins and score_ordi < max_wins:
        gagnant = play_round()

        if gagnant == "joueur":
            score_joueur += 1
        elif gagnant == "ordinateur":
            score_ordi += 1

        #Annoncer le score présent
        print(f"Score: {score_joueur} for you and {score_ordi} for the computer!")
    #Annoncer le gagnant final:
    if score_joueur == max_wins:
        print("Congrats! You've won against the big bad machine!")
    else:
        print("The machine defeated you... It is a shame :(")

#Option de jouer à nouveau
def main():
    while True:
        #Annonce du jeu
        print("Welcome to a game of rock, paper, scissors! In this game, you will play a best-of-five against a machine. Can you handle it?")
       
        #Jouer le jeu
        best_of_five()
        
        #Propose une autre partie
        play_again = input("Do you want to play again? (yes/no): " ).lower()

        #Arrête la boucle si le joueur opte pour "no"
        if play_again != "yes":
            print("Thanks for playing! See you again!")
            break

if __name__ == "__main__":
    main()
