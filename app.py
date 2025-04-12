import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="German Word Quiz", page_icon="📚")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #E0F7FA;
        color: black;
    }
    .stTextInput > div > input {
        background-color: #F8BBD0;
        color: black;
    }
    .stButton>button {
        background-color: #F48FB1;
        color: black;
        font-weight: bold;
    }
    .stAlert {
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📚 German Word Quiz")
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: black;"> Let's Learn German Words! 📚✨</h1>
        <p style="font-size:18px; color: black;">Click the button to guess the meaning of a German word!</p>
    </div>
""", unsafe_allow_html=True)

# Fun little loading animation
placeholder = st.empty()
for i in range(3):
    placeholder.markdown(f"🎉 Loading... {i+1}")
    time.sleep(0.3)
placeholder.success("Done! ✅")

# German word dictionary
words = {
   'Arbute': 'angajati' ,
'Kunden' : 'client' ,
'Kundendienst' : 'serviciu de client' ,
'Der Auftrag' : 'solicitare' ,
'Zielgrupper' : 'grup tinta' ,
'Diensleistung' : 'serviciu' ,
'Geschäftsbereiche' :  'domenii de activitate' ,
'schiftlich' : 'in scris' ,
'beschreiben' : 'descrie' ,
'genügt' : 'de ajuns' ,
'brauche' : 'a avea nevoie' ,
'vielleicht' : 'probabil' ,
'Fehler' : 'eroare' ,
'bestelle' : 'a comanda' ,
'bekomme' : 'a primi' ,
'schlau' : 'perspicace' ,
'Arbeitsplatze' : 'loc de munca' ,
'das Unternehmen' : 'compania' ,
'Grosserunternehmen' : 'companie mare' ,
'Grundungjahr' : 'anul inaugurarii' ,
'Mitarbeiterzahl' : 'nr. de angajati' ,
'Die Tätigkeit' : 'activitate' ,
'Geschäft': 'afacere' ,
'Termine' : 'intalnire' ,
'Waterbildung' : 'cursuri profesionale' ,
'Eine Termin fetlegen' : 'to make an appointment' ,
'Die Messe' : 'targ' ,
'besuchen' : 'a vizita' ,
'brauchen' : 'a avea nevoie' ,
'schenken' : 'a darui' ,
'schinken' : 'a trimite' ,
'mitnehmen' : 'a lua cu tine' ,
'Das Werk' : 'opera, munca' ,
'drucken' : 'a printa' ,
'zeigen' : 'a arata' ,
'vorstellen' : 'a prezenta' ,
'der Standort' : 'locatia' ,
'der Geschäftsbereich' : 'zona de afaceri' ,
'die Menge' : 'suma' ,
'dringent' : 'urgent' ,
'praktisch' : 'practic' ,
'zufrieden' : 'multumit' ,
'beruflich ': 'profesional' ,
'die Entwicklung' : 'dezvoltare, proiectare' ,
'Aussendienst' : 'serviciu extern' ,
'Die Werbung' : 'reclama' ,
'entwickeln' : 'a dezvolta' ,
'Buchaltung' : 'contabilitate' ,
'Einkauf' : 'achizitii' ,
'Der Führerschein' : 'permis' ,
'Bereichte' : 'domeniu' ,
'Vertrieb' : 'transport' ,
'Geschäftsleute': 'oameni de afaceri' ,
'einladen' : 'a invita' ,
'die Zeit' : 'timp' ,
'Zusage': 'confirmare',
'Absage': 'refuz' ,
'Einladung':'invitatie' ,
'brauche':'a avea nevoie',
}

# --- SESSION STATE SETUP ---
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_number = 0
    st.session_state.word_list = list(words.items())
    random.shuffle(st.session_state.word_list)
    st.session_state.start_time = time.time()

# Make sure start_time is always present
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# --- QUIZ LOGIC ---
if st.session_state.q_number < len(st.session_state.word_list):
    german, english = st.session_state.word_list[st.session_state.q_number]
    st.subheader(f"What does *{german}* mean in Romanian?")

    # Timer
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
                st.error(f"❌ Nope! The correct answer was **{english}**.")

            st.session_state.q_number += 1
            st.session_state.start_time = time.time()
            st.experimental_rerun()
    else:
        st.error("⏰ Time's up!")
        st.info(f"The correct answer was **{english}**.")
        st.session_state.q_number += 1
        st.session_state.start_time = time.time()
        st.experimental_rerun()
else:
    st.balloons()
    st.success("🎊 Quiz Complete!")
    st.write(f"Your final score: **{st.session_state.score} / {len(words)}**")

    if st.button("🔄 Restart"):
        st.session_state.clear()
        st.session_state.score = 0
        st.session_state.q_number = 0
        st.session_state.word_list = list(words.items())
        random.shuffle(st.session_state.word_list)
        st.session_state.start_time = time.time()
        st.experimental_rerun()
