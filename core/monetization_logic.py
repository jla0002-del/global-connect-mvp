import pandas as pd

class MonetizationCalculator:
    def __init__(self, commission_rate=0.10, pro_subscription_fee=49.99):
        """
        Inicializa el calculador de monetización.
        
        :param commission_rate: % de comisión sobre transacciones (default 10%)
        :param pro_subscription_fee: Cuota mensual de suscripción "Curaduría Pro"
        """
        self.commission_rate = commission_rate
        self.pro_subscription_fee = pro_subscription_fee

    def calculate_transaction_revenue(self, total_transaction_volume):
        """Calcula los ingresos por comisiones de intermediación."""
        return total_transaction_volume * self.commission_rate

    def calculate_subscription_revenue(self, num_pro_subscribers, months=1):
        """Calcula los ingresos por suscripciones 'Curaduría Pro'."""
        return num_pro_subscribers * self.pro_subscription_fee * months

    def calculate_total_revenue(self, total_transaction_volume, num_pro_subscribers, months=1):
        """Calcula los ingresos totales combinando ambas fuentes."""
        transaction_rev = self.calculate_transaction_revenue(total_transaction_volume)
        subscription_rev = self.calculate_subscription_revenue(num_pro_subscribers, months)
        return {
            'transaction_revenue': transaction_rev,
            'subscription_revenue': subscription_rev,
            'total_revenue': transaction_rev + subscription_rev
        }

    def simulate_monetization_scenarios(self, avg_order_value, num_orders_per_client, num_clients, pro_adoption_rate):
        """
        Simula ingresos basados en el comportamiento del cliente.
        
        :param avg_order_value: Valor promedio de cada pedido
        :param num_orders_per_client: Número de pedidos por cliente al mes
        :param num_clients: Número total de clientes
        :param pro_adoption_rate: % de clientes que se suscriben a "Curaduría Pro"
        """
        total_volume = avg_order_value * num_orders_per_client * num_clients
        num_pro_subscribers = num_clients * pro_adoption_rate
        
        return self.calculate_total_revenue(total_volume, num_pro_subscribers)

if __name__ == "__main__":
    calc = MonetizationCalculator()
    
    # Ejemplo de simulación para el piloto (15 clientes)
    # Asumiendo: Pedido promedio $500, 2 pedidos/mes, 20% adopción Pro
    simulation = calc.simulate_monetization_scenarios(
        avg_order_value=500,
        num_orders_per_client=2,
        num_clients=15,
        pro_adoption_rate=0.20
    )
    
    print("Simulación de Monetización Mensual (Piloto 15 clientes):")
    print(f"Ingresos por Comisiones (10%): ${simulation['transaction_revenue']:.2f}")
    print(f"Ingresos por Suscripción Pro: ${simulation['subscription_revenue']:.2f}")
    print(f"Ingresos Totales: ${simulation['total_revenue']:.2f}")
