# Lógica de Monetización Renovada (Fase 3)

La transformación de Global Imports hacia "Global Connect" implica una evolución desde un modelo de importación tradicional hacia un Marketplace B2B híbrido con dos fuentes principales de ingresos digitales.

## 1. Comisiones por Intermediación

Este flujo de ingresos capitaliza el volumen de transacciones que ocurren dentro de la plataforma entre los artesanos y los minoristas.

*   **Mecánica:** Se aplica un porcentaje fijo sobre el valor total de cada transacción "One-Tap".
*   **Tasa de Comisión (MVP):** 10%. Esta tasa es competitiva frente a los márgenes tradicionales de importación y cubre los costes operativos de la plataforma.
*   **Valor Agregado:** El minorista accede a precios directos de origen, compensando la comisión con la eliminación de intermediarios analógicos ineficientes.

## 2. Suscripción "Curaduría Pro"

Un modelo de ingresos recurrentes (SaaS) que ofrece servicios de valor añadido impulsados por el motor de IA Smart Curator.

*   **Cuota Mensual (MVP):** $49.99 / mes.
*   **Beneficios Exclusivos:**
    *   **Acceso Prioritario:** Notificaciones anticipadas sobre nuevas piezas exclusivas y colecciones limitadas.
    *   **Insights de Tendencia:** Reportes detallados generados por la IA sobre qué productos están ganando tracción en el mercado global.
    *   **Sugerencias de Stock Optimizadas:** Recomendaciones personalizadas de inventario basadas en el perfil de ventas histórico del minorista.

## 3. Simulación de Ingresos (Modelo Piloto)

Utilizando la lógica programada en `src/core/monetization_logic.py`, presentamos una proyección mensual para los 15 clientes del piloto:

| Variable | Valor Simulado |
| :--- | :--- |
| **Clientes Totales** | 15 |
| **Pedido Promedio (AOV)** | $500.00 |
| **Pedidos por Mes/Cliente** | 2 |
| **Volumen Total Transaccionado (GMV)** | $15,000.00 |
| **Adopción Suscripción Pro** | 20% (3 clientes) |

### Desglose de Ingresos Mensuales

| Fuente de Ingreso | Cálculo | Total Mensual |
| :--- | :--- | :--- |
| **Comisiones (10%)** | $15,000 * 0.10 | $1,500.00 |
| **Suscripción Pro** | 3 clientes * $49.99 | $149.97 |
| **Ingreso Total Estimado** | | **$1,649.97** |

## 4. Conclusión de la Fase 3

El modelo de monetización híbrido permite capturar valor tanto de la actividad transaccional como del servicio de datos/curaduría. Esto diversifica el riesgo y crea un flujo de ingresos recurrente que mejora la previsibilidad financiera de Global Connect.

**Próximos Pasos:** Una vez validada esta lógica de monetización, procederemos a la **Fase 4: Escenarios Dinámicos y Roadmap de Escalabilidad**, donde proyectaremos estos resultados a un año y definiremos la hoja de ruta hacia la Versión 3.0.
