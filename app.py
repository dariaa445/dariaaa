import streamlit as st
import random

st.set_page_config(page_title="German Word Quiz", page_icon="📚")
st.markdown(
    """
    <h1 style="text-align:center; font-size: 50px; font-family: 'Baloo 2', cursive ;
               background: linear-gradient(to right, #F48FB1, #CE93D8, #81D4FA);
               -webkit-background-clip: text;
               color: transparent;
               padding: 10px;">
       🌸German Word Quiz🌸
    </h1>
    """,
    unsafe_allow_html=True
)

# Corrected the line below
st.markdown("<p style='font-size:17px;'>Learn German words in a fun way!</p>", unsafe_allow_html=True)

# Fixed color syntax + updated to black for contrast
st.markdown(
    """
    <div style="text-align:left;">
        <h1 style="color: #ADD8E6;"> Let's Learn German Words! 📚✨</h1>
        <p style="font-size:18px; color: #d2b4de ;">Click the button to guess the meaning of a German word!</p>
    </div>
    """,
    unsafe_allow_html=True
)
# 🌈 Style the Submit button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50 !important;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 24px;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Word list (removed the duplicate 'brauche' key)
words = {
    'Arbute': 'angajati',
    'Kunden': 'client',
    'Kundendienst': 'serviciu de client',
    'Der Auftrag': 'solicitare',
    'Zielgrupper': 'grup tinta',
    'Diensleistung': 'serviciu',
    'Geschäftsbereiche': 'domenii de activitate',
    'schiftlich': 'in scris',
    'beschreiben': 'a descrie',
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
    'Weiterterbildung': 'cursuri profesionale',
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
    'beruflich ': 'profesional',
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
    'Einladung': 'invitatie',
}

# Setup session state
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_number = 0
    st.session_state.word_list = list(words.items())
    random.shuffle(st.session_state.word_list)

# Quiz logic
if st.session_state.q_number < len(st.session_state.word_list):
    german, english = st.session_state.word_list[st.session_state.q_number]
    st.markdown(
    f"""
    <h3 style="font-family: Arial; font-size: 24px;">
        What does <span style="color: #E91E63; font-weight: bold;">{german}</span> mean in Romanian?
    </h3>
    """,
    unsafe_allow_html=True
)


    answer = st.text_input("Your answer:")

    if st.button("Submit"):
        if answer.lower() == english.lower():
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Nope! It was **{english}**.")

        st.session_state.q_number += 1
        st.experimental_rerun()
else:
    st.balloons()
    st.subheader("🎉 Quiz Complete!")
    st.write(f"Your final score: **{st.session_state.score}/{len(words)}**")

    if st.button("Restart"):
        st.session_state.clear()
        st.experimental_rerun()
