import pandas as pd
import numpy as np

class ValidationMetricsCalculator:
    def __init__(self, num_clients=15, duration_weeks=4):
        self.num_clients = num_clients
        self.duration_weeks = duration_weeks
        self.data = None

    def generate_mock_data(self):
        """Genera datos simulados para el piloto de 4 semanas con 15 clientes."""
        np.random.seed(42)
        dates = pd.date_range(start='2026-06-01', periods=self.duration_weeks * 7, freq='D')
        
        client_data = []
        for client_id in range(1, self.num_clients + 1):
            for date in dates:
                # Simular actividad del cliente
                activated = np.random.choice([0, 1], p=[0.2, 0.8]) if date == dates[0] else 1
                explored_catalog = np.random.choice([0, 1], p=[0.3, 0.7])
                visits = np.random.randint(0, 5)
                order_cycle_time = np.random.uniform(1, 5) # Días
                cac = np.random.uniform(50, 150) # Coste de adquisición
                ltv = np.random.uniform(200, 1000) # Lifetime Value proyectado
                
                client_data.append({
                    'client_id': client_id,
                    'date': date,
                    'activated': activated,
                    'explored_catalog': explored_catalog,
                    'visits': visits,
                    'order_cycle_time': order_cycle_time,
                    'cac': cac,
                    'ltv': ltv
                })
        
        self.data = pd.DataFrame(client_data)

    def calculate_activation_rate(self):
        """Calcula el % de minoristas que completan el registro y exploran el catálogo."""
        if self.data is None: return 0
        total_clients = self.num_clients
        activated_clients = self.data[self.data['activated'] == 1]['client_id'].nunique()
        explored_clients = self.data[self.data['explored_catalog'] == 1]['client_id'].nunique()
        
        activation_rate = (explored_clients / total_clients) * 100
        return activation_rate

    def calculate_sticky_rate(self):
        """Calcula el % de usuarios que regresan >3 veces por semana sin visita comercial."""
        if self.data is None: return 0
        
        # Agrupar por cliente y semana
        self.data['week'] = self.data['date'].dt.isocalendar().week
        weekly_visits = self.data.groupby(['client_id', 'week'])['visits'].sum().reset_index()
        
        sticky_users = weekly_visits[weekly_visits['visits'] > 3]['client_id'].nunique()
        sticky_rate = (sticky_users / self.num_clients) * 100
        return sticky_rate

    def calculate_operational_efficiency(self, traditional_cycle_time=7):
        """Calcula la reducción de tiempo en el ciclo de pedido vs. método tradicional."""
        if self.data is None: return 0
        avg_digital_cycle_time = self.data['order_cycle_time'].mean()
        reduction = ((traditional_cycle_time - avg_digital_cycle_time) / traditional_cycle_time) * 100
        return reduction

    def project_ltv_vs_cac(self):
        """Proyecta cuándo el valor del cliente supera el coste de adquisición digital."""
        if self.data is None: return None
        avg_cac = self.data['cac'].mean()
        avg_ltv = self.data['ltv'].mean()
        
        # Simulación de recuperación de CAC (meses)
        # Asumiendo un margen mensual del 10% del LTV
        monthly_margin = (avg_ltv / 12) * 0.1
        months_to_recover = avg_cac / monthly_margin if monthly_margin > 0 else float('inf')
        
        return {
            'avg_cac': avg_cac,
            'avg_ltv': avg_ltv,
            'months_to_recover': months_to_recover
        }

    def get_summary_report(self):
        """Genera un informe resumen de las métricas de validación."""
        if self.data is None: self.generate_mock_data()
        
        report = {
            'Tasa de Activación (%)': self.calculate_activation_rate(),
            'Recurrencia (Sticky Rate) (%)': self.calculate_sticky_rate(),
            'Eficiencia Operativa (% reducción)': self.calculate_operational_efficiency(),
            'LTV vs CAC Projection': self.project_ltv_vs_cac()
        }
        return report

if __name__ == "__main__":
    calculator = ValidationMetricsCalculator()
    report = calculator.get_summary_report()
    print("Informe de Métricas de Validación del Piloto (4 semanas, 15 clientes):")
    for metric, value in report.items():
        print(f"{metric}: {value}")
