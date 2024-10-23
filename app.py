import streamlit as st
import pandas as pd
from sklearn.metrics import roc_auc_score


# ページのレイアウトを設定
st.set_page_config(
    page_title="リーダーボード",
    layout="wide", # wideにすると横長なレイアウトに
    initial_sidebar_state="expanded"
)

# タイトルの設定
st.title("リーダーボード")

df_ref = pd.read_csv("正解_bin.csv")
st.write(df_ref)

# サイドバーにアップロードファイルのウィジェットを表示
st.sidebar.markdown("TEST")
uploaded_file = st.sidebar.file_uploader("計算結果をCSVファイルでアップロードしてください", type='csv')
if uploaded_file is not None:
    df_res = pd.read_csv(uploaded_file)
    auc = roc_auc_score(df_ref["値"], df_res["値"])
    st.write(auc)
