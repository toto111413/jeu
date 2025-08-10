import streamlit as st
import random

st.title("⚔️ Combat RPG")

# Initialisation des variables
if "player_hp" not in st.session_state:
    st.session_state.player_hp = 50
if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 40

st.write(f"❤️ Ton énergie : {st.session_state.player_hp}")
st.write(f"👹 Énergie du monstre : {st.session_state.enemy_hp}")

# Actions possibles
action = st.radio("Choisis ton action :", ["Attaquer", "Soigner", "Rien faire"])

if st.button("Valider l'action"):
    if action == "Attaquer":
        degats = random.randint(5, 15)
        st.session_state.enemy_hp -= degats
        st.write(f"💥 Tu infliges {degats} dégâts au monstre !")
    elif action == "Soigner":
        soin = random.randint(5, 10)
        st.session_state.player_hp += soin
        st.write(f"💊 Tu récupères {soin} points de vie.")
    else:
        st.write("⏳ Tu attends...")

    # Attaque du monstre si toujours vivant
    if st.session_state.enemy_hp > 0:
        degats_monstre = random.randint(3, 12)
        st.session_state.player_hp -= degats_monstre
        st.write(f"👹 Le monstre t'attaque et inflige {degats_monstre} dégâts.")

    # Vérification victoire/défaite
    if st.session_state.enemy_hp <= 0:
        st.success("🎉 Tu as vaincu le monstre !")
        st.session_state.player_hp = 50
        st.session_state.enemy_hp = 40
    elif st.session_state.player_hp <= 0:
        st.error("💀 Tu es mort...")
        st.session_state.player_hp = 50
        st.session_state.enemy_hp = 40
