import streamlit as st
import pandas as pd

st.title("Datos Educativos")

uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.sidebar.header("Filtros")

    if "Nivel educativo" in df.columns:
        nivel_educativo = st.sidebar.multiselect(
            "Nivel educativo", df["Nivel educativo"].unique()
        )
    else:
        nivel_educativo = []

    if "Carrera" in df.columns:
        carrera = st.sidebar.multiselect(
            "Carrera", df["Carrera"].unique()
        )
    else:
        carrera = []

    if "Institución" in df.columns:
        institucion = st.sidebar.multiselect(
            "Institución", df["Institución"].unique()
        )
    else:
        institucion = []

    df_filtrado = df.copy()

    if nivel_educativo:
        df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]

    if carrera:
        df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]

    if institucion:
        df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

    st.dataframe(df_filtrado)

    st.subheader("Estadísticas Descriptivas")
    if not df_filtrado.empty:
        st.write(df_filtrado.describe())
    else:
        st.write("No hay datos disponibles para mostrar estadísticas.")

    st.subheader("Conteo de Estudiantes por Nivel Educativo")
    if "Nivel educativo" in df.columns:
        if not df_filtrado.empty and "Nivel educativo" in df_filtrado.columns:
            conteo_niveles = df_filtrado["Nivel educativo"].value_counts()
            if not conteo_niveles.empty:
                st.bar_chart(conteo_niveles)
            else:
                st.write("No hay datos para mostrar el conteo de estudiantes por nivel educativo.")
        else:
            st.write("No hay datos disponibles para los filtros seleccionados.")
    else:
        st.write("La columna 'Nivel educativo' no existe en el DataFrame original.")

    st.subheader("Distribución de la Edad")
    if "Edad" in df.columns and not df_filtrado.empty:
        st.bar_chart(df_filtrado["Edad"].value_counts(bins=10))
    else:
        st.write("No hay datos para mostrar el histograma de edad o la columna 'Edad' no existe.")
else:
    st.write("Por favor, sube un archivo CSV.")
