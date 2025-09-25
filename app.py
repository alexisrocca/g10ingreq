
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sistema de Laboratorio - Secciones", layout="wide")

st.title("Presentacion de Propuesta de Requisitos")
st.subheader("Sistema de Gestión de Laboratorio")

st.caption("**Grupo 10:** \nSantiago Vigo, Santiago Passafiume, Débora Bucci, Alexis Barbero, Alexis Rocca")



@st.cache_data
def load_data():
    import os
    rf_data = [
        ["RF-01", "Funcional", "El sistema debe permitir agendar, modificar y cancelar turnos para estudios médicos", "Alta"],
        ["RF-02", "Funcional", "El sistema debe registrar y almacenar los datos personales de los pacientes", "Alta"],
        ["RF-03", "Funcional", "El sistema debe permitir cargar y validar resultados de análisis clínicos", "Alta"],
        ["RF-04", "Funcional", "El sistema debe generar reportes de resultados en formato PDF para impresión y envío digital", "Alta"],
        ["RF-05", "Funcional", "El sistema debe mantener un historial completo de estudios por paciente", "Media"],
        ["RF-06", "Funcional", "El sistema debe enviar notificaciones automáticas cuando los resultados estén disponibles", "Media"],
        ["RF-07", "Funcional", "El sistema debe permitir la búsqueda de pacientes por DNI, nombre o apellido", "Media"],
        ["RF-08", "Funcional", "El sistema debe controlar que no se asignen turnos duplicados en el mismo horario", "Alta"],
        ["RF-09", "Funcional", "El sistema debe permitir consultar la disponibilidad de horarios en tiempo real", "Media"],
        ["RF-10", "Funcional", "El sistema debe generar reportes estadísticos de productividad del laboratorio", "Baja"],
    ]
    rnf_data = [
        ["RNF-01", "No Funcional", "El sistema debe garantizar la confidencialidad de los datos médicos cumpliendo con la Ley de Protección de Datos Personales", "Alta"],
        ["RNF-02", "No Funcional", "El sistema debe tener un tiempo de respuesta menor a 3 segundos para consultas básicas", "Media"],
        ["RNF-03", "No Funcional", "El sistema debe estar disponible 24/7 con un uptime mínimo del 99%", "Alta"],
        ["RNF-04", "No Funcional", "El sistema debe ser intuitivo y fácil de usar, requiriendo máximo 2 horas de capacitación para usuarios básicos", "Media"],
        ["RNF-05", "No Funcional", "El sistema debe soportar al menos 100 usuarios concurrentes sin degradación del rendimiento", "Media"],
        ["RNF-06", "No Funcional", "El sistema debe realizar respaldos automáticos diarios de toda la información", "Alta"],
        ["RNF-07", "No Funcional", "El sistema debe funcionar correctamente en navegadores web modernos (Chrome, Firefox, Safari, Edge)", "Media"],
    ]
    extra_info = [
        ["CTX-01", "Contexto", "Un laboratorio de Rosario necesita un Sistema de Gestión de Laboratorio para turnos, resultados y comunicación", "—"],
        ["PROB-01", "Problema", "Retrasos en la entrega de resultados", "El proceso manual con planillas de Excel genera demoras en el procesamiento y entrega de estudios", "Alta"],
        ["PROB-02", "Problema", "Errores de carga de datos por entrada manual", "La entrada manual de datos genera errores frecuentes en la información de pacientes y resultados", "Alta"],
        ["PROB-03", "Problema", "Duplicidad de turnos", "Sin un sistema centralizado, se pueden asignar múltiples turnos en el mismo horario", "Alta"],
        ["PROB-04", "Problema", "Falta de historial digital", "No existe un sistema digitalizado que mantenga el historial completo de estudios por paciente", "Alta"],
        ["PROB-05", "Problema", "Comunicación ineficiente", "La comunicación telefónica entre el laboratorio y pacientes/médicos es lenta e ineficaz", "Media"],
        ["PROB-06", "Problema", "Gestión de turnos deficiente", "El sistema actual de gestión de turnos es manual, lento y propenso a errores", "Alta"],
        ["ACT-01", "Actor", "Paciente", "Persona que solicita estudios médicos y recibe resultados", "—"],
        ["ACT-02", "Actor", "Recepcionista/Administrativo", "Gestiona turnos, atiende pacientes, recibe muestras y entrega resultados", "—"],
        ["ACT-03", "Actor", "Técnico de laboratorio", "Realiza análisis clínicos y carga resultados al sistema", "—"],
        ["ACT-04", "Actor", "Bioquímico responsable", "Valida  y firma los resultados de análisis", "—"],
        ["ACT-05", "Actor", "Médico", "Solicita estudios para pacientes y consulta resultados", "—"],
        ["ACT-06", "Actor", "Administrador del sistema", "Gestiona usuarios, permisos y configuraciones del sistema", "—"],
        ["ACT-07", "Actor", "Director del laboratorio", "Supervisa operaciones generales y accede a reportes estadísticos", "—"]
    ]
    df_rf = pd.DataFrame(rf_data, columns=["ID", "TIPO", "DESCRIPCIÓN", "PRIORIDAD"])
    df_rnf = pd.DataFrame(rnf_data, columns=["ID", "TIPO", "DESCRIPCIÓN", "PRIORIDAD"])
    df_extra = pd.DataFrame(extra_info, columns=["ID", "TIPO", "TÍTULO", "DESCRIPCIÓN", "PRIORIDAD"])
    
    return df_extra, df_rf, df_rnf

df_extra, df_rf, df_rnf = load_data()

# Separar por secciones
df_actores = df_extra[df_extra["TIPO"] == "Actor"].copy()
df_problemas = df_extra[df_extra["TIPO"] == "Problema"].copy()

tab1, tab2, tab3, tab4 = st.tabs(["Problemas", "Actores", "Requerimientos", "Gráfico útil"])

with tab1:
    st.subheader("Problemas Identificados")
    st.write("Problemas del escenario actual con su descripción detallada y prioridad.")
    
    # Crear tabla con título y descripción de problemáticas
    problemas_tabla = df_problemas[["TÍTULO", "DESCRIPCIÓN"]].copy()
    problemas_tabla.columns = ["Problemática", "Descripción"]
    st.dataframe(
        problemas_tabla.reset_index(drop=True), 
        use_container_width=True,
        column_config={
            "Problemática": st.column_config.Column(width="medium"),
            "Descripción": st.column_config.Column(width="large")
        }
    )

with tab2:
    st.subheader("Actores del Sistema")
    st.write("Listado de actores con su nombre y descripción de su rol.")
    
    # Crear tabla con nombre y descripción de actores
    actores_tabla = df_actores[["TÍTULO", "DESCRIPCIÓN"]].copy()
    actores_tabla.columns = ["Actor", "Descripción"]
    st.dataframe(
        actores_tabla.reset_index(drop=True), 
        use_container_width=True,
        column_config={
            "Actor": st.column_config.Column(width="medium"),
            "Descripción": st.column_config.Column(width="large")
        }
    )

with tab3:
    st.subheader("Requerimientos")
    st.markdown("**Primero: Requerimientos Funcionales (RF)**")
    st.dataframe(
        df_rf.sort_values(["PRIORIDAD", "ID"]).reset_index(drop=True), 
        use_container_width=True,
        column_config={
            "ID": st.column_config.Column(width="small"),
            "TIPO": st.column_config.Column(width="medium"),
            "DESCRIPCIÓN": st.column_config.Column(width="large"),
            "PRIORIDAD": st.column_config.Column(width="small")
        }
    )
    st.markdown("---")
    st.markdown("**Luego: Requerimientos No Funcionales (RNF)**")
    st.dataframe(
        df_rnf.sort_values(["PRIORIDAD", "ID"]).reset_index(drop=True), 
        use_container_width=True,
        column_config={
            "ID": st.column_config.Column(width="small"),
            "TIPO": st.column_config.Column(width="medium"),
            "DESCRIPCIÓN": st.column_config.Column(width="large"),
            "PRIORIDAD": st.column_config.Column(width="small")
        }
    )

with tab4:
    st.subheader("Gráfico de utilidad — Prioridades por tipo de requerimiento")
    # Construir un gráfico comparando RF vs RNF por prioridad
    prios = ["Alta", "Media", "Baja"]
    rf_counts = df_rf["PRIORIDAD"].value_counts()
    rnf_counts = df_rnf["PRIORIDAD"].value_counts()
    rf_vals = [int(rf_counts.get(p, 0)) for p in prios]
    rnf_vals = [int(rnf_counts.get(p, 0)) for p in prios]

    import numpy as np
    x = np.arange(len(prios))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, rf_vals, width, label="RF")
    ax.bar(x + width/2, rnf_vals, width, label="RNF")
    ax.set_xticks(x)
    ax.set_xticklabels(prios)
    ax.set_xlabel("Prioridad")
    ax.set_ylabel("Cantidad")
    ax.set_title("Comparación de prioridades entre RF y RNF")
    ax.legend()
    st.pyplot(fig)

