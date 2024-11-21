import streamlit as st
import pandas as pd
from data import turmas_fundamental, turmas_medio

with st.sidebar:
    add_select = None

    add_radio = st.radio(
        "Composição",
        ('Ensino Fundamental', "Ensino Médio")
    )

    if add_radio == 'Ensino Fundamental':
        add_select = st.selectbox('Escolha uma turma:', turmas_fundamental)
    if add_radio == 'Ensino Médio':
        add_select = st.selectbox('Escolha uma turma:', turmas_medio)

chart_path = {
    'Ensino Fundamental': f'./data/fundamental/{add_select}.csv',
    'Ensino Médio': f'./data/medio/{add_select}.csv'
}
chart = None
for key, path in chart_path.items():
    if key == add_radio:
        chart = path
print(chart)

df = pd.read_csv(chart)
df.set_index('Matérias', inplace=True)
st.bar_chart(data=df['Notas >= 6'])

st.dataframe(df, width=1000)
