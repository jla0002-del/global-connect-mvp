import streamlit as st
import pandas as pd
import numpy as np
from core.monetization_logic import MonetizationCalculator
from core.scenario_simulator import ScenarioSimulator

st.set_page_config(layout="wide", page_title="Global Connect: Simulador de Sostenibilidad Financiera")

st.title("Global Connect: Simulador de Sostenibilidad Financiera")
st.subheader("Proyección a 36 meses para el MVP")

# --- Parámetros Base --- #
st.sidebar.header("Parámetros Base")
initial_clients = st.sidebar.slider("Clientes Iniciales del Piloto", 15, 100, 15)
commission_rate = st.sidebar.slider("Tasa de Comisión por Transacción (%)", 0.05, 0.20, 0.10, 0.01)
pro_subscription_fee = st.sidebar.slider("Cuota Mensual Suscripción Pro ($)", 20.0, 100.0, 49.99, 5.0)

monetization_calc = MonetizationCalculator(commission_rate, pro_subscription_fee)
simulator = ScenarioSimulator(initial_clients, commission_rate, pro_subscription_fee)

# --- Definición de Escenarios --- #
st.sidebar.header("Parámetros por Escenario")

scenario_options = ["Conservador", "Realista", "Optimista"]
selected_scenario = st.sidebar.selectbox("Seleccionar Escenario", scenario_options)

scenario_params = {
    "Conservador": {
        "new_clients_per_month": st.sidebar.slider("Nuevos Clientes/Mes (Conservador)", 0, 5, 1),
        "churn_rate": st.sidebar.slider("Tasa de Abandono Mensual (Conservador, %)", 0.01, 0.10, 0.05, 0.01),
        "avg_order_value": st.sidebar.slider("Valor Promedio Pedido ($) (Conservador)", 100, 1000, 400),
        "num_orders_per_client": st.sidebar.slider("Pedidos/Cliente/Mes (Conservador)", 0.5, 3.0, 1.5, 0.1),
        "pro_adoption_rate": st.sidebar.slider("Adopción Suscripción Pro (%) (Conservador)", 0.05, 0.50, 0.10, 0.05)
    },
    "Realista": {
        "new_clients_per_month": st.sidebar.slider("Nuevos Clientes/Mes (Realista)", 1, 10, 3),
        "churn_rate": st.sidebar.slider("Tasa de Abandono Mensual (Realista, %)", 0.01, 0.07, 0.03, 0.01),
        "avg_order_value": st.sidebar.slider("Valor Promedio Pedido ($) (Realista)", 200, 1500, 500),
        "num_orders_per_client": st.sidebar.slider("Pedidos/Cliente/Mes (Realista)", 1.0, 4.0, 2.0, 0.1),
        "pro_adoption_rate": st.sidebar.slider("Adopción Suscripción Pro (%) (Realista)", 0.10, 0.70, 0.20, 0.05)
    },
    "Optimista": {
        "new_clients_per_month": st.sidebar.slider("Nuevos Clientes/Mes (Optimista)", 5, 20, 7),
        "churn_rate": st.sidebar.slider("Tasa de Abandono Mensual (Optimista, %)", 0.005, 0.05, 0.01, 0.005),
        "avg_order_value": st.sidebar.slider("Valor Promedio Pedido ($) (Optimista)", 300, 2000, 600),
        "num_orders_per_client": st.sidebar.slider("Pedidos/Cliente/Mes (Optimista)", 1.5, 5.0, 2.5, 0.1),
        "pro_adoption_rate": st.sidebar.slider("Adopción Suscripción Pro (%) (Optimista)", 0.20, 0.90, 0.35, 0.05)
    }
}

# --- Ejecutar Simulación --- #
st.header(f"Resultados de la Simulación: Escenario {selected_scenario}")

current_scenario_params = scenario_params[selected_scenario]
simulation_results = simulator.simulate_scenario(current_scenario_params, months=36)

st.dataframe(simulation_results.style.format({
    "transaction_revenue": "${:,.2f}",
    "subscription_revenue": "${:,.2f}",
    "total_revenue": "${:,.2f}"
}), use_container_width=True)

st.line_chart(simulation_results.set_index("month")[[ "clients", "total_revenue"]])

st.markdown("--- ")

# --- Análisis de Sensibilidad LTV --- #
st.header("Análisis de Sensibilidad del LTV")

avg_arpu_monthly = st.slider("ARPU Mensual Promedio ($)", 50, 500, 110)
churn_rates_for_analysis = st.multiselect("Tasas de Abandono a Analizar (%)", 
                                        [0.01, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20],
                                        default=[0.01, 0.03, 0.05])

ltv_sensitivity = simulator.analyze_ltv_sensitivity(avg_arpu_monthly, churn_rates_for_analysis)
ltv_df = pd.DataFrame(ltv_sensitivity.items(), columns=["Tasa de Abandono", "LTV Proyectado"])
ltv_df["LTV Proyectado"] = ltv_df["LTV Proyectado"].map("${:,.2f}".format)
st.table(ltv_df)

st.markdown("**Nota:** LTV = ARPU Mensual / Tasa de Abandono Mensual. Un ARPU de $110 se basa en el piloto de 15 clientes y $1650 de ingresos mensuales.")

# --- Conclusiones --- #
st.header("Conclusiones Clave")
st.write(
    "Este simulador interactivo permite explorar la sostenibilidad financiera de 'Global Connect' bajo diferentes supuestos. "
    "Es crucial monitorear de cerca la tasa de adquisición de nuevos clientes y, especialmente, la tasa de abandono (churn rate), "
    "ya que tiene un impacto significativo en el Lifetime Value (LTV) de nuestros clientes B2B."
)
