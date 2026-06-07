import pandas as pd
import numpy as np
from monetization_logic import MonetizationCalculator

class ScenarioSimulator:
    def __init__(self, initial_clients=15, commission_rate=0.10, pro_subscription_fee=49.99):
        self.monetization_calc = MonetizationCalculator(commission_rate, pro_subscription_fee)
        self.initial_clients = initial_clients

    def simulate_scenario(self, scenario_params, months=12):
        """Simula un escenario a 12 meses."""
        results = []
        current_clients = self.initial_clients
        
        for month in range(1, months + 1):
            # Crecimiento de clientes
            new_clients = scenario_params["new_clients_per_month"]
            churned_clients = current_clients * scenario_params["churn_rate"]
            current_clients = current_clients + new_clients - churned_clients
            current_clients = max(0, round(current_clients)) # Asegurar que no haya clientes negativos

            # Simulación de ingresos
            monthly_revenue = self.monetization_calc.simulate_monetization_scenarios(
                avg_order_value=scenario_params["avg_order_value"],
                num_orders_per_client=scenario_params["num_orders_per_client"],
                num_clients=current_clients,
                pro_adoption_rate=scenario_params["pro_adoption_rate"]
            )
            
            results.append({
                "month": month,
                "clients": current_clients,
                "transaction_revenue": monthly_revenue["transaction_revenue"],
                "subscription_revenue": monthly_revenue["subscription_revenue"],
                "total_revenue": monthly_revenue["total_revenue"]
            })
        
        return pd.DataFrame(results)

    def analyze_ltv_sensitivity(self, avg_revenue_per_client, churn_rates):
        """Analiza la sensibilidad del LTV a diferentes tasas de retención (1 - churn_rate)."""
        ltv_results = {}
        for churn_rate in churn_rates:
            # LTV = ARPU / Churn Rate (simplificado para este análisis)
            # ARPU (Average Revenue Per User) mensual
            ltv = avg_revenue_per_client / churn_rate if churn_rate > 0 else float("inf")
            ltv_results[f"Churn Rate {churn_rate*100:.1f}%"] = ltv
        return ltv_results

if __name__ == "__main__":
    simulator = ScenarioSimulator()

    # Definición de parámetros para cada escenario
    scenario_params = {
        "conservador": {
            "new_clients_per_month": 1,
            "churn_rate": 0.05, # 5% churn mensual
            "avg_order_value": 400,
            "num_orders_per_client": 1.5,
            "pro_adoption_rate": 0.10
        },
        "realista": {
            "new_clients_per_month": 3,
            "churn_rate": 0.03, # 3% churn mensual
            "avg_order_value": 500,
            "num_orders_per_client": 2,
            "pro_adoption_rate": 0.20
        },
        "optimista": {
            "new_clients_per_month": 7,
            "churn_rate": 0.01, # 1% churn mensual
            "avg_order_value": 600,
            "num_orders_per_client": 2.5,
            "pro_adoption_rate": 0.35
        }
    }

    print("\n--- Simulación Escenario Conservador ---")
    conservative_results = simulator.simulate_scenario(scenario_params["conservador"])
    print(conservative_results.tail(1))

    print("\n--- Simulación Escenario Realista ---")
    realistic_results = simulator.simulate_scenario(scenario_params["realista"])
    print(realistic_results.tail(1))

    print("\n--- Simulación Escenario Optimista ---")
    optimistic_results = simulator.simulate_scenario(scenario_params["optimista"])
    print(optimistic_results.tail(1))

    # Análisis de Sensibilidad LTV
    # Asumimos un ARPU mensual promedio de $110 (basado en el piloto, $1650/15 clientes)
    avg_arpu_monthly = 110
    churn_rates_for_analysis = [0.01, 0.03, 0.05, 0.07, 0.10]
    ltv_sensitivity = simulator.analyze_ltv_sensitivity(avg_arpu_monthly, churn_rates_for_analysis)
    print("\n--- Análisis de Sensibilidad del LTV ---")
    for rate, ltv_val in ltv_sensitivity.items():
        print(f"{rate}: ${ltv_val:.2f}")
