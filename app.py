import streamlit as st
import pandas as pd

# 讀取資料
csv_path = "fee_data_2024_ready_clean_address.csv"
df = pd.read_csv(csv_path, dtype=str)

st.set_page_config(page_title="繳費紀錄查詢", layout="centered")
st.title("📋 繳費紀錄查詢系統（手機版）")

# 棟別篩選
blocks = sorted(df['棟別'].dropna().unique().tolist())
selected_block = st.selectbox("請選擇棟別：", blocks)

# 地址篩選
filtered_df = df[df['棟別'] == selected_block]
units = sorted(filtered_df['address'].dropna().unique().tolist())
selected_unit = st.selectbox("請選擇地址（樓號）：", units)

# 顯示結果
result = df[df['address'] == selected_unit]

if not result.empty:
    st.subheader("🔍 查詢結果")
    rename_dict = {
        'id': '住戶代號',
        'address': '地址',
        'owner': '區權人',
        '棟別': '棟別',
        'manage': '管理費',
        '車位清潔費': '車位清潔費',
        'elevator': '電梯費',
        'discount': '折扣',
        'total': '總金額'
    }
    st.dataframe(result.rename(columns=rename_dict), use_container_width=True)
else:
    st.info("尚無資料")
