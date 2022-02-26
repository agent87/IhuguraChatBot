from requests.api import request
import streamlit as st
import time
from lib.translate import translator
from lib.s2t import convert



SIDEBAR_OPTION_PROJECT_INFO = "Project Info"
SIDEBAR_OPTION_TEXT_QA = "Type your inquiry"
SIDEBAR_OPTION_SPEECH_QA = "Upload a recording"
SIDEBAR_OPTION_MEET_TEAM = "Meet the Team"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_INFO, SIDEBAR_OPTION_TEXT_QA, SIDEBAR_OPTION_SPEECH_QA, SIDEBAR_OPTION_MEET_TEAM]





#st.cache()
def startup_load():
    one = st.title('Ewawe Parking Managment System V.2.1')
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)
        # Update status text.
        status_text.text(
        'Starting up the system :{}%'.format(i) )
        # Pretend we're doing some computation that takes time.
        time.sleep(0.1)
    one.empty()
    progress_bar.empty() 
    status_text.empty()


def main():
    st.sidebar.title("Navigation Bar")
    AppMode = st.sidebar.selectbox('Please select from the following',SIDEBAR_OPTIONS)
    trans = translator()

    if AppMode == SIDEBAR_OPTION_PROJECT_INFO:
        st.title("Ihugure Chatbot")
        st.text("Ihugure Chatbot is legal .")
    elif AppMode == SIDEBAR_OPTION_TEXT_QA:
        st.title("Text based Q&A Inquiry")
        st.text("This is a text based Q&A inquiry")
        question = st.text_area("Type your question here", value="", height=None, max_chars=250, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
        if st.button("Submit Inquiry", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False):
            if len(question) > 0:
                response = trans.to_english(text=question)
                st.text_area("Response",value=response, disabled=True)
            else:
                pass
    elif AppMode == SIDEBAR_OPTION_SPEECH_QA:
        st.title("Speech enabled Q&A Inquiry")
        st.info('PRIVACY POLICY: uploaded audio files are never saved or stored. They are held entirely within memory for prediction and discarded after the final results are displayed. ')
        audio_file = st.file_uploader("Upload your audio files here", type=['wav', 'mp3' ])
        if audio_file is not None:
            st.write('Audio File')
            st.audio(audio_file)
            s2t = convert()
            text = s2t.to_text(audio=audio_file)
            s2t_header = st.subheader("Speech 2 Text")
            s2t_text_area = st.text_area("",value=text+"?", disabled=True)
            response_header = st.subheader("Response")
            response_text_area = st.text_area("",value="Response", disabled=True)

    elif AppMode == SIDEBAR_OPTION_MEET_TEAM:
        st.title("Meet the team behind the system")
        first_column, second_column, third_column= st.beta_columns(3)
        st.success('Hope you had a great time :)')
        st.write('Please feel free to connect with us on Linkedin!')
        expandar_linkedin = st.beta_expander('Contact Information')
        expandar_linkedin.write('Arnaud: https://www.linkedin.com/in/arnaud-kayonga-5910a813a/')




main()