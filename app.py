import streamlit as st

import random

st.set_page_config(page_title="German Word Quiz", page_icon="📚")
st.title(" German Word Quiz")
st.write("Learn German words in a fun way!", size=17)
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: E0F2F1;"> Let's Learn German Words! 📚✨</h1>
        <p style="font-size:18px;">Click the button to guess the meaning of a German word!</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    body {
        background-color: #FFF3E0; /* Light peach */
    }
    </style>
    """,
    unsafe_allow_html=True
)

import time

placeholder = st.empty()
for i in range(5):
    placeholder.markdown(f"🎉 Loading... {i+1}")
    time.sleep(0.5)
placeholder.success("Done! ✅")


# Word list
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

start = time.time()

if user_input:
    elapsed = time.time() - start
    if elapsed > 5:
        st.error("⏰ Too late!")
    elif user_input.lower() == correct_answer.lower():
        st.success("✅ Correct!")
    else:
        st.warning("❌ Try again.")
# Setup session state
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_number = 0
    st.session_state.word_list = list(words.items())
    random.shuffle(st.session_state.word_list)

# Quiz logic
if st.session_state.q_number < len(st.session_state.word_list):
    german, english = st.session_state.word_list[st.session_state.q_number]
    st.subheader(f"What does _{german}_ mean in Romanian?")

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
