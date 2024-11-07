import streamlit as st

# Webアプリのタイトル
st.title("日本語文字の文字コード表示アプリ")

# 入力フォーム
input_text = st.text_input("日本語の文字を入力してください（1文字のみ）:")

# 入力がある場合に文字コードを表示
if input_text:
    if len(input_text) == 1:
        char_code = ord(input_text)
        st.write(f"文字 '{input_text}' の文字コードは: {char_code}")
    else:
        st.error("1文字のみ入力してください。")