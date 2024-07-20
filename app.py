import random
import pandas as pd
import streamlit as st

from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Superhuman Utilities", page_icon="🚀")
words_df = pd.read_csv("words.csv")
word = ""


def refresh():
    streamlit_js_eval(js_expressions="parent.window.location.reload()")


def submit_callback():
    st.session_state.submit_clicked = True


def get_word():
    with open("seen.txt") as file:
        seen_words = [line.rstrip() for line in file]
    print(seen_words)

    category = st.session_state.category
    word_list = words_df[category].to_list()
    while True:
        x = random.randint(0, 249)
        new_word = word_list[x]
        if new_word not in seen_words:
            file = open("seen.txt", "a")  # append mode
            file.write(f"{new_word} \n")
            file.close()
            break

    st.session_state.word = new_word


def start_callback():
    if not st.session_state.start:
        st.session_state.start = True
        st.session_state.score = 0
        st.session_state.skip = False
        get_word()
    else:
        pass


def correct_callback():
    get_word()
    st.session_state.score += 1


def skip_callback():
    if st.session_state.skip:
        st.error(f'You have already skipped! Your skipped word was {st.session_state.skipped_word}', icon="🚨")
    else:
        st.session_state.skipped_word = st.session_state.word
        st.session_state.skip = True
        get_word()


def main() -> None:

    user_input = st.empty()
    with user_input.container():
        st.title("Articulate! (Imevbore Edition) 🫂")
        st.markdown(":green[Version 0.0.1: Word Generator]")
        st.markdown(":gray[*Version 0.0.2: Score tracker*]")
        st.markdown(":gray[*Version 0.0.3: Built in timer*]")
        st.divider()
        st.header(body="What category are you on?")
        category = st.selectbox(label=" ", options=["People", "World", "Objects", "Nature", "Random", "Actions", "Spade"])
        go_button = st.button(label="Start Round!", on_click=submit_callback)

    if "submit_clicked" not in st.session_state:
        st.session_state.submit_clicked = False

    if go_button or st.session_state.submit_clicked:
        user_input.empty()
        st.session_state.category = category
        st.header(body=f"Your word is: {st.sesssion_state.word}", divider="rainbow")
        correct_button = st.button(label="Correct", on_click=correct_callback)
        skip_button = st.button(label="Skip", on_click=skip_callback)
        st.subheader(body=f"Score this round: {st.session_state.score}")
        reset_button = st.button(label="Reset Round", on_click=refresh)


if __name__ == "__main__":
    main()
    