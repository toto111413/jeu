import turtle
import random
import time
import os

# === Variables === #
score = 0
temps_restant = 30
jeu_termine = False
highscore = 0
vitesse_cible = 500  # en ms (diminue avec score)
niveau = 1

# === Charger high score === #
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0

# === Fenêtre === #
fenetre = turtle.Screen()
fenetre.title("🎯 Clic Mania X")
fenetre.bgcolor("#222222")
fenetre.setup(width=700, height=700)

# === Stylo général === #
stylo = turtle.Turtle()
stylo.hideturtle()
stylo.penup()

# === Cible === #
cible = turtle.Turtle()
cible.shape("circle")
cible.color("red")
cible.penup()
cible.speed(0)
cible.shapesize(2)

# === Score === #
score_affiche = turtle.Turtle()
score_affiche.hideturtle()
score_affiche.penup()
score_affiche.goto(0, 300)

# === Chronomètre === #
chrono = turtle.Turtle()
chrono.hideturtle()
chrono.penup()
chrono.goto(0, 260)

# === Déplacement automatique === #
def auto_move():
    if not jeu_termine:
        deplacer_cible()
        fenetre.ontimer(auto_move, max(200, vitesse_cible - score * 10))

# === Score update === #
def mettre_a_jour_score():
    score_affiche.clear()
    score_affiche.write(f"Score : {score}   |   High Score : {highscore}   |   Niveau : {niveau}", align="center", font=("Arial", 16, "bold"))

# === Chrono update === #
def mise_a_jour_temps():
    global temps_restant, jeu_termine
    if temps_restant > 0:
        temps_restant -= 1
        chrono.clear()
        chrono.write(f"Temps restant : {temps_restant}s", align="center", font=("Arial", 14, "normal"))
        fenetre.ontimer(mise_a_jour_temps, 1000)
    else:
        fin_jeu()

# === Clic sur la cible === #
def clique(x, y):
    global score, niveau, vitesse_cible
    if not jeu_termine:
        if cible.distance(x, y) < 30:
            score += 1
            if score % 5 == 0:
                niveau += 1
                vitesse_cible = max(200, vitesse_cible - 50)
            effet_visuel()
            mettre_a_jour_score()

# === Déplacer cible === #
def deplacer_cible():
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    cible.goto(x, y)

# === Effet visuel rapide === #
def effet_visuel():
    couleur = random.choice(["yellow", "cyan", "lime", "magenta", "orange", "white"])
    cible.color(couleur)
    cible.shapesize(random.uniform(1.5, 3.5))

# === Fin de jeu === #
def fin_jeu():
    global jeu_termine, highscore
    jeu_termine = True
    cible.hideturtle()
    chrono.clear()
    score_affiche.clear()

    if score > highscore:
        highscore = score
        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

    stylo.goto(0, 30)
    stylo.write(f"🎉 Temps écoulé ! Score final : {score}", align="center", font=("Arial", 18, "bold"))
    stylo.goto(0, -10)
    stylo.write(f"🏆 High Score : {highscore}", align="center", font=("Arial", 14, "normal"))
    stylo.goto(0, -50)
    stylo.write("Clique ici pour rejouer", align="center", font=("Arial", 14, "italic"))
    fenetre.onclick(rejouer)

# === Rejouer === #
def rejouer(x, y):
    if -150 < x < 150 and -70 < y < -30:
        initialiser_jeu()

# === Initialiser jeu === #
def initialiser_jeu():
    global score, temps_restant, jeu_termine, niveau, vitesse_cible
    score = 0
    temps_restant = 30
    jeu_termine = False
    niveau = 1
    vitesse_cible = 500
    stylo.clear()
    chrono.clear()
    cible.color("red")
    cible.shapesize(2)
    cible.showturtle()
    mettre_a_jour_score()
    deplacer_cible()
    mise_a_jour_temps()
    auto_move()

# === Menu d'accueil === #
def menu_accueil():
    stylo.clear()
    stylo.goto(0, 50)
    stylo.write("🎯 Bienvenue dans Clic Mania X 🎯", align="center", font=("Arial", 22, "bold"))
    stylo.goto(0, 10)
    stylo.write("Clique n'importe où pour démarrer", align="center", font=("Arial", 14, "normal"))
    fenetre.onclick(start_game)

# === Démarrer jeu === #
def start_game(x=None, y=None):
    fenetre.onclick(None)
    initialiser_jeu()
    cible.onclick(clique)

# === Lancement === #
menu_accueil()
turtle.mainloop()


