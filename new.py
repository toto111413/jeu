import pygame
import random
import sys

# Initialisation
pygame.init()

# Dimensions
largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("🎯 Attrape le carré - Contre la montre")

# Couleurs
NOIR = (0, 0, 0)
BLEU = (0, 128, 255)
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)

# Joueur
joueur = pygame.Rect(50, 50, 50, 50)
vitesse = 5

# Cible
cible = pygame.Rect(random.randint(0, largeur - 30),
                    random.randint(0, hauteur - 30), 30, 30)

# Score et police
score = 0
font = pygame.font.Font(None, 36)
grosse_font = pygame.font.Font(None, 72)

# Timer
temps_max = 30  # secondes

# Charger le son
try:
    son_pop = pygame.mixer.Sound("pop.wav")
except:
    son_pop = None
    print("⚠️ Fichier 'pop.wav' introuvable ! Le son sera désactivé.")

# Rejouer : bouton
bouton_rejouer = pygame.Rect(largeur // 2 - 80, hauteur // 2 + 80, 160, 50)


def initialiser_jeu():
    global joueur, cible, score, temps_debut, jeu_termine
    joueur.x, joueur.y = 50, 50
    cible.x = random.randint(0, largeur - cible.width)
    cible.y = random.randint(0, hauteur - cible.height)
    score = 0
    temps_debut = pygame.time.get_ticks()
    jeu_termine = False


initialiser_jeu()

# Boucle
clock = pygame.time.Clock()
running = True

while running:
    fenetre.fill(NOIR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if jeu_termine and event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rejouer.collidepoint(event.pos):
                initialiser_jeu()

    if not jeu_termine:
        # Timer
        temps_actuel = (pygame.time.get_ticks() - temps_debut) / 1000
        temps_restant = max(0, int(temps_max - temps_actuel))

        if temps_restant <= 0:
            jeu_termine = True

        # Contrôles
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            joueur.x -= vitesse
        if touches[pygame.K_RIGHT]:
            joueur.x += vitesse
        if touches[pygame.K_UP]:
            joueur.y -= vitesse
        if touches[pygame.K_DOWN]:
            joueur.y += vitesse

        # Collision
        if joueur.colliderect(cible):
            score += 1
            cible.x = random.randint(0, largeur - cible.width)
            cible.y = random.randint(0, hauteur - cible.height)
            if son_pop:
                son_pop.play()

        # Dessin
        pygame.draw.rect(fenetre, BLEU, joueur)
        pygame.draw.rect(fenetre, ROUGE, cible)

        # Score et temps
        texte_score = font.render(f"Score : {score}", True, BLANC)
        texte_temps = font.render(f"Temps restant : {temps_restant}s", True,
                                  BLANC)
        fenetre.blit(texte_score, (10, 10))
        fenetre.blit(texte_temps, (10, 50))
    else:
        # Fin du jeu
        message = grosse_font.render("⏰ Fin du jeu !", True, BLANC)
        score_final = font.render(f"Ton score : {score}", True, BLANC)
        texte_bouton = font.render("Rejouer", True, NOIR)

        fenetre.blit(
            message,
            (largeur // 2 - message.get_width() // 2, hauteur // 2 - 80))
        fenetre.blit(
            score_final,
            (largeur // 2 - score_final.get_width() // 2, hauteur // 2 - 20))

        pygame.draw.rect(fenetre, VERT, bouton_rejouer)
        fenetre.blit(texte_bouton,
                     (bouton_rejouer.x + 30, bouton_rejouer.y + 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
