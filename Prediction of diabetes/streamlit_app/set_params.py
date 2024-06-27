import streamlit as st


def load_page_setting():
    # Функция для добавления локального CSS файла
    file_name = "./streamlit_app/data/styles.css"

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Подключаем CSS файл
    local_css(file_name)