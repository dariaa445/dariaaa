import streamlit as st
import random
import time

# Page setup
st.set_page_config(page_title="German Word Quiz", page_icon="📚")

# Apply custom styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E0F7FA; /* light blue */
        color: black;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: black;
    }
    .stTextInput > div > div > input {
        background-color: #F8BBD0; /* pink */
        color: black;
    }
    .stButton button {
        background-color: #F48FB1 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App header
st.title("📚 German Word Quiz")
st.write("Learn German words in a fun way!")

st.markdown(
    """
    <div style="text-align: center;">
        <h1> Let's Learn German Words! 📚✨</h1>
        <p style="font-size:18px;">Click the button to guess the meaning of a German word!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Loading animation
placeholder = st.empty()
for i in range(3):
    placeholder.markdown(f"🎉 Loading... {i+1}")
    time.sleep(0.3)
placeholder.success("Done! ✅")

# Word list
words = {
    'Arbute': 'angajati',
    'Kunden': 'client',
    'Kundendienst': 'serviciu de client',
    'Der Auftrag': 'solicitare',
    'Zielgrupper': 'grup tinta',
    'Diensleistung': 'serviciu',
    'Geschäftsbereiche': 'domenii de activitate',
    'schiftlich': 'in scris',
    'beschreiben': 'descrie',
    'genügt': 'de ajuns',
    'brauche': 'a avea nevoie',
    'vielleicht': 'probabil',
    'Fehler': 'eroare',
    'bestelle': 'a comanda',
    'bekomme': 'a primi',
    'schlau': 'perspicace',
    'Arbeitsplatze': 'loc de munca',
    'das Unternehmen': 'compania',
    'Grosserunternehmen': 'companie mare',
    'Grundungjahr': 'anul inaugurarii',
    'Mitarbeiterzahl': 'nr. de angajati',
    'Die Tätigkeit': 'activitate',
    'Geschäft': 'afacere',
    'Termine': 'intalnire',
    'Waterbildung': 'cursuri profesionale',
    'Eine Termin fetlegen': 'to make an appointment',
    'Die Messe': 'targ',
    'besuchen': 'a vizita',
    'schenken': 'a darui',
    'schinken': 'a trimite',
    'mitnehmen': 'a lua cu tine',
    'Das Werk': 'opera, munca',
    'drucken': 'a printa',
    'zeigen': 'a arata',
    'vorstellen': 'a prezenta',
    'der Standort': 'locatia',
    'der Geschäftsbereich': 'zona de afaceri',
    'die Menge': 'suma',
    'dringent': 'urgent',
    'praktisch': 'practic',
    'zufrieden': 'multumit',
    'beruflich': 'profesional',
    'die Entwicklung': 'dezvoltare, proiectare',
    'Aussendienst': 'serviciu extern',
    'Die Werbung': 'reclama',
    'entwickeln': 'a dezvolta',
    'Buchaltung': 'contabilitate',
    'Einkauf': 'achizitii',
    'Der Führerschein': 'permis',
    'Bereichte': 'domeniu',
    'Vertrieb': 'transport',
    'Geschäftsleute': 'oameni de afaceri',
    'einladen': 'a invita',
    'die Zeit': 'timp',
    'Zusage': 'confirmare',
    'Absage': 'refuz',
    'Einladung': 'invitatie'
}

# Setup session state
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_number = 0
    st.session_state.word_list = list(words.items())
    random.shuffle(st.session_state.word_list)
    st.session_state.start_time = time.time()

# Quiz logic
if st.session_state.q_number < len(st.session_state.word_list):
    german, english = st.session_state.word_list[st.session_state.q_number]
    st.subheader(f"What does *{german}* mean in Romanian?")

    # Timer logic
    elapsed = time.time() - st.session_state.start_time
    remaining = 10 - int(elapsed)
    if remaining > 0:
        st.warning(f"⏳ You have {remaining} seconds left!")
        answer = st.text_input("Your answer:")
        if st.button("Submit"):
            if answer.lower() == english.lower():
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Nope! It was **{english}**.")
            st.session_state.q_number +=

