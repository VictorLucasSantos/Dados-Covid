import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
)
# print(df.columns.tolist())
df = df.rename(
    columns={
        "epi_week": "Semana Epidemiológica",
        "date": "Data",
        "country": "País",
        "state": "Estado",
        "city": "Cidade",
        "newDeaths": "Novas Mortes",
        "deaths": "Mortes Acumuladas",
        "newCases": "Novos Casos",
        "totalCases": "Casos Acumulados",
        "deathsMS": "Mortes (Ministério da Saúde)",
        "totalCasesMS": "Casos Acumulados (Ministério da Saúde)",
        "deaths_per_100k_inhabitants": "Mortes por 100 mil Habitantes",
        "totalCases_per_100k_inhabitants": "Casos por 100 mil Habitantes",
        "deaths_by_totalCases": "Proporção de Mortes por Casos",
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
