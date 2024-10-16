import tkinter as tk

class Grid:
    def __init__(self):
        self.root = tk.Tk() #Permet de définir la fenêtre
        self.cells = [] #Les listes pour géré les coordonée
        self.list_x = []
        self.list_o = []

        #Pour géré l'affichage des Label dans le jeu
        self.erreur_place = None
        self.current_player = "Joueur 1 X"
        #================================

        self.create_grid() #Appelle la création d'une grille la premier fois pour lancer le jeu
        self.game(self.current_player, "")

    def create_grid(self): #On créé la grille de jeu
        for row in range(3):
            row_cells = []
            for col in range(3):
                #On défini et ajoute toutes les cases
                cell = tk.Label(self.root, width=5, height=2, borderwidth=1, relief="solid", bg="white", font=('Helvetica', 40))
                cell.grid(row=row, column=col)
                #On créé un bouton qui va ajouter à l'endroits cliquer
                cell.bind("<Button>", lambda e, r=row, c=col: self.add_player_on_grid(r, c))
                row_cells.append(cell)
            self.cells.append(row_cells)

    def add_player_on_grid(self, row, col): #On ajoute les points sur la grille
        #Si une case est occuper on renvoie que c'est le cas et on ne va pas plus loin
        if [row, col] in self.list_x or [row, col] in self.list_o:
            self.game(self.current_player, "Cette case est prise")
            return
        #Si le c'est le joueur 1 qui joue on effectue cette partie
        if self.current_player == "Joueur 1 X":
            self.list_x.append([row, col]) #On ajoute les coo à la liste du joueur
            self.cells[row][col].config(text="X") #on écrit X dans la case
            if self.check_victory("X"): #Si la fonction renvoie vrai fin du jeu
                self.game("Fin du jeu", "Joueur 1 gagne !")
                self.disable_cells()  #On empêche d'ajouter des choses
                return
            self.current_player = "Joueur 2 O"
        #Sinon pareil mais pour le joueur 2 /même chose que le joueur 1\
        else:
            self.list_o.append([row, col])
            self.cells[row][col].config(text="O")
            if self.check_victory("O"):
                self.game("Fin du jeu", "Joueur 2 gagne !")
                self.disable_cells()
                return
            self.current_player = "Joueur 1 X"

        if len(self.list_x) + len(self.list_o) == 9: #Si la somme de la longeur des deux liste vaut 9 c'est draw
            self.game("Fin du jeu", "Match nul !")
            self.disable_cells() #On empêche d'ajouter des choses
            return

        self.game(self.current_player, "") #On retourne au jeu et on vide le paramètre erreur

    def check_victory(self, symbol):
        player_list = self.list_x if symbol == "X" else self.list_o #On défini de quelle joueur on veut vérifier la victoire
        win_conditions = [
            [[0, 0], [0, 1], [0, 2]],  # Ligne 0
            [[1, 0], [1, 1], [1, 2]],  # Ligne 1
            [[2, 0], [2, 1], [2, 2]],  # Ligne 2
            [[0, 0], [1, 0], [2, 0]],  # Colonne 0
            [[0, 1], [1, 1], [2, 1]],  # Colonne 1
            [[0, 2], [1, 2], [2, 2]],  # Colonne 2
            [[0, 0], [1, 1], [2, 2]],  # Diagonale 1
            [[0, 2], [1, 1], [2, 0]]   # Diagonale 2
        ]

        for condition in win_conditions:#On vérifie si le joueur rempli une condition.
            if all([c in player_list for c in condition]):
                return True #Si oui la fonction est vrai
        return False #Sinon elle est fausse

    def disable_cells(self):
        for row in self.cells:
            for cell in row:
                cell.unbind("<Button>")  #Enlève l'évennement clique dans toutes les cellules du tableau

    def game(self, player, erreur):
        if self.erreur_place is not None: #Si la variable n'est pas vide,
            self.erreur_place.grid_forget() #On l'oublie, elle disparais

        self.current_title = tk.Label(self.root, text=player) #On écrit c'est au tour de qui en fonction du paramètre joueur
        self.current_title.grid(row=4, column=0, padx=5, pady=5) #On met en forme

        self.erreur_place = tk.Label(self.root, text=erreur) #On gère l'erreur si il y en a une
        self.erreur_place.grid(row=4, column=1, padx=5, pady=5) #Mise en forme

    def mainloop(self):
        self.root.mainloop() #Sert à définir la boucle pour afficher les information

app = Grid()
app.mainloop()#Lancement du programme


