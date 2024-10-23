import streamlit as st
import pandas as pd


# ページのレイアウトを設定
st.set_page_config(
    page_title="リーダーボード",
    layout="wide", # wideにすると横長なレイアウトに
    initial_sidebar_state="expanded"
)

# タイトルの設定
st.title("リーダーボード")

# サイドバーにアップロードファイルのウィジェットを表示
st.sidebar.markdown("TEST")
uploaded_file = st.sidebar.file_uploader("計算結果をCSVファイルでアップロードしてください", type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
