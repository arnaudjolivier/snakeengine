
# Le terrain de jeu est un terrain de 20 x 16 cases, la position [0, 0] se situe en haut à gauche.
# Les variables du jeu sont stockées dans le dictionnaire gameState qui est fourni en paramètre de vos fonctions. Ce dictionnaire comporte 4 clés :
# -> gameState['direction'] représente la direction actuelle du serpent. C'est une chaîne de caractères égale à "UP", "DOWN", "LEFT" ou "RIGHT".
# -> gameState['snake'] est une liste. Chaque élément est une liste de 2 nombres entiers [x, y] représentant une position du corps du serpent. Le premier élément est la position de la tête du serpent, et le dernier correspond au bout de sa queue.
# -> gameState['grid'] est une liste composée de 20 autres listes qui représente les obstacles du terrain de jeu. gameState['grid'][x][y] est True si un obstacle se situe à cet endroit, et False sinon.
# -> gameState['apple'] est une liste de deux entiers [x, y] représentant les coordonnées de la pomme sur le terrain.


# Lire la carte de jeu dans un fichier dont le nom est donné dans la variable filename
# Le fichier contient 16 lignes de 20 caractères chacune qui représente la grille de jeu. Un exemple est donné dans grid.txt.
# Sur chaque ligne, un caractère X correspond à un obstacle et un . correspond à une case vide.
#
# readGrid modifie la valeur correspondant à la clé 'grid' dans le dictionnaire gameState.
# N'oubliez pas de return gameState à la fin !
import random


def readGrid(gameState, filename):
    gameState['grid'] = []
    for i in range(20):
        gameState['grid'] += [[False] * 16]
    with open (filename,'r') as mongrid:
        line = []
        stockage = []
        for x in range(16):
            line = mongrid.readline()
            line = line.replace('\n','')
            stockage += [line]
        for i in range(20):
            for y in range(16):
                if stockage[y][i] == 'X':
                    gameState['grid'][i][y] = True
    return gameState


# Réinitialiser le serpent. Initialement, le serpent fait une seule case de long et il a une position aléatoire sur la grille.
# La direction est aussi aléatoire.
# Attention, la case aléatoire ne doit pas être un obstacle !

def resetSnake(gameState):
    gameState['snake'] = [[random.randrange(20),random.randrange(16)]]
   # while gameState['snake'] in gameState['grid']:
    #    gameState['snake'] = [[random.randrange(20),random.randrange(16)]]
    keybind = ['RIGHT', 'LEFT', 'UP', 'DOWN']
    gameState['direction'] = random.sample(keybind,1)[0]
    return gameState

# Faire apparaître une nouvelle pomme sur le plateau à un endroit aléatoire
# Attention, la pomme ne doit pas apparaître sur le serpent ou sur un obstacle !
def resetApple(gameState):
    gameState['apple'] = [random.randrange(19),random.randrange(15)]
    pom = gameState['apple']
    while  gameState['apple'] in gameState['snake'] or (gameState['grid'][pom[0]][pom[1]] == True):        
        gameState ['apple'] = [random.randrange(19),random.randrange(15)]
    return gameState

# Calcule la nouvelle liste de positions du serpent, la tête toujours à l'index 0.
# Si la variable eating est True, alors le serpent vient de manger une pomme et il faut augmenter sa longueur d'une unité.
def moveSnake(gameState, eating):
    # 1. Calculer nouvelle position de la tête
    xtete = gameState['snake'][0][0]
    ytete = gameState['snake'][0][1]

    if gameState['direction'] == 'UP':
        newpos = [xtete, ytete - 1]
    if gameState['direction'] == 'DOWN':
        newpos = [xtete, ytete + 1]
    if gameState['direction'] == 'LEFT':
        newpos = [xtete - 1, ytete]
    if gameState['direction'] == 'RIGHT':
        newpos = [xtete + 1, ytete]
    # 2. Insérer la nouvelle position en début de liste
    gameState['snake'] = [newpos] + gameState['snake']
    # 3. Supprimer la queue si besoin
    if eating:
        return gameState
    else:
        gameState['snake'] = gameState['snake'][:-1]
    return gameState

# Vérifie si le serpent est en train de manger une pomme (si la position de sa tête coïncide avec celle de la pomme)
# Renvoie True si le serpent est en train de manger, False sinon
# Attention, il faut return un boolean et non gameState
def checkEating(gameState):
    pomme = gameState['apple']
    serp = gameState['snake']
    if serp[0] == pomme:
        return True
    else:
        return False

# Vérifie si le serpent est mort (en se mordant la queue, en entrant sur un obstacle, ou en sortant du plateau)
# Renvoie True si le serpent est mort, False sinon
# Attention, il faut return un boolean et non gameState
def checkDead(gameState):
    return False