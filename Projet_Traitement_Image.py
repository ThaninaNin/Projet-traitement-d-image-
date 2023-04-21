import streamlit as st
from PIL import Image

# Titre de l'application
st.title("Sélectionner une image")

# Bouton pour sélectionner une image
uploaded_file = st.file_uploader("Sélectionner une image", type=["jpg", "jpeg", "png"])

# Si un fichier a été sélectionné
if uploaded_file is not None:
    # Ouvrir l'image avec PIL
    image = Image.open(uploaded_file)

    # Afficher l'image dans la page Streamlit
    st.image(image, caption='Image sélectionnée')
else:
    # Si aucun fichier n'a été sélectionné
    st.warning("Veuillez sélectionner une image.")
