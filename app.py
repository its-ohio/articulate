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

    return new_word


def start_callback():
    if not st.session_state.start:
        st.session_state.start = True
        st.session_state.score = 0
        st.session_state.skip = False
    else:
        pass


def correct_callback():
    pass


def skip_callback():
    if st.session_state.skip:
        return None
    else:
        x = random.randint(0, 499)
        return x


def main() -> None:

    user_input = st.empty()
    with user_input.container():
        st.title("Articulate! (Imevbore Edition) 🫂")
        st.markdown(":green[Version 0.0.1: Word Generator]")
        st.markdown(":gray[*Version 0.0.2: Score tracker*]")
        st.markdown(":gray[*Version 0.0.3: Built in timer*]")
        st.divider()
        st.header(body="What category are you on?")
        category = st.selectbox(label=" ", options=["People", "Places", "Objects", "Actions", "World", "Random"])
        go_button = st.button(label="Start Round!", on_click=submit_callback)

    if "submit_clicked" not in st.session_state:
        st.session_state.submit_clicked = False

    if go_button or st.session_state.submit_clicked:
        user_input.empty()
        st.session_state.category = category
        st.header(body=f"Your word is: {get_word()}", divider="rainbow")
        correct_button = st.button(label="Next", on_click=correct_callback)
        reset_button = st.button(label="Reset", on_click=refresh)


if __name__ == "__main__":
    main()
