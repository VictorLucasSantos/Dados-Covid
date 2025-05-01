import pandas as pd
import plotly.express as px
import os
import streamlit as st

url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
filename = "cases-brazil-states.csv"

if not os.path.exists(filename):
    print("Baixando arquivo...")
    df = pd.read_csv(url)
    df.to_csv(filename, index=False)
else:
    print("Usando arquivo local...")
    df = pd.read_csv(filename)


df = df.rename(
    columns={
        "epi_week": "Semana Epidemiológica",
        "date": "Data",
        "country": "País",
        "state": "Estado",
        "city": "Cidade",
        "newDeaths": "Novos Óbitos",
        "deaths": "Óbitos Acumuladas",
        "newCases": "Novos Casos",
        "totalCases": "Casos Acumulados",
        "deathsMS": "Óbitos (Ministério da Saúde)",
        "totalCasesMS": "Casos Acumulados (Ministério da Saúde)",
        "deaths_per_100k_inhabitants": "Óbitos por 100 mil Habitantes",
        "totalCases_per_100k_inhabitants": "Casos por 100 mil Habitantes",
        "deaths_by_totalCases": "Proporção de Óbitos por Casos",
        "recovered": "Recuperados",
        "suspects": "Suspeitos",
        "tests": "Testes Realizados",
        "tests_per_100k_inhabitants": "Testes por 100 mil Habitantes",
        "vaccinated": "Vacinados (1ª Dose)",
        "vaccinated_per_100_inhabitants": "Vacinados (1ª Dose) por 100 Habitantes",
        "vaccinated_second": "Vacinados (2ª Dose)",
        "vaccinated_second_per_100_inhabitants": "Vacinados (2ª Dose) por 100 Habitantes",
        "vaccinated_single": "Vacinados (Dose Única)",
        "vaccinated_single_per_100_inhabitants": "Vacinados (Dose Única) por 100 Habitantes",
        "vaccinated_third": "Vacinados (3ª Dose ou Reforço)",
        "vaccinated_third_per_100_inhabitants": "Vacinados (3ª Dose) por 100 Habitantes",
    }
)

states = list(df["Estado"].unique())

state = st.sidebar.selectbox("Escolha o Estado", states, key="Estados")

column = "Casos por 100 mil Habitantes"
colunas = [
    "Novos Óbitos",
    "Novos Casos",
    "Óbitos por 100 mil Habitantes",
    "Casos por 100 mil Habitantes",
]

column = st.sidebar.selectbox(
    "Escolha o Tipo de Informação", colunas, key="Tipo Informação"
)

# Filtrando estado
df = df[df["Estado"] == state]

fig = px.line(df, x="Data", y=column, title=column + " - " + state)
fig.update_layout(xaxis_title="Data", yaxis_title=column.upper(), title={"x": 0.5})

st.title("DADOS COVID - BRASIL")
st.write(
    "Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utiloze o menu lateral"
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br"
)
