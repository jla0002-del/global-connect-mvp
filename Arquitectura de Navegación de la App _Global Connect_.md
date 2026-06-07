# Arquitectura de Navegación de la App "Global Connect"

## Estructura de Archivos Propuesta

```
global_connect_mvp/
├── docs/
│   ├── architecture/
│   │   ├── navigation_architecture.md
│   │   └── technical_scheme.md
│   ├── user_flows/
│   │   └── phase1_user_flow.md
│   └── viability_simulator/
│       └── economic_viability_simulator.md
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── catalog_api.py
│   │   ├── orders_api.py
│   │   ├── tracking_api.py
│   │   └── smart_curator_api.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── ui/
│   │   │   ├── __init__.py
│   │   │   ├── catalog_screen.py
│   │   │   ├── orders_screen.py
│   │   │   ├── tracking_screen.py
│   │   │   └── smart_curator_screen.py
│   │   └── components/
│   │       ├── __init__.py
│   │       └── common_ui_elements.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── services.py
│   └── tests/
│       ├── __init__.py
│       ├── test_api.py
│       └── test_app.py
├── data/
│   ├── mock_data/
│   │   ├── catalog_data.json
│   │   └── orders_data.json
│   └── raw_data/
├── config/
│   ├── settings.py
│   └── database.py
├── scripts/
│   ├── setup.sh
│   └── run_tests.sh
├── .gitignore
├── README.md
├── requirements.txt
```

## Arquitectura de Navegación de la App (Pestañas)

La aplicación "Global Connect" se estructurará en torno a un sistema de navegación basado en pestañas, lo que permitirá un acceso intuitivo y rápido a las funcionalidades principales. Las pestañas principales serán:

1.  **Catálogo (Catalog):** Esta pestaña será el punto de entrada al catálogo digital interactivo de productos artesanales. Permitirá a los minoristas explorar, filtrar y visualizar los productos de manera eficiente.
2.  **Pedidos (Orders):** Dedicada a la gestión de pedidos, esta sección facilitará la realización de compras mediante la función "One-Tap" y proporcionará un historial detallado de todas las transacciones.
3.  **Tracking:** Un módulo esencial para el seguimiento de pedidos internacionales. Los minoristas podrán consultar el estado de sus envíos con actualizaciones sobre Aduanas, En tránsito y Entregado.
4.  **IA Smart Curator:** Esta pestaña albergará el motor de recomendaciones impulsado por inteligencia artificial, que sugerirá stock a los minoristas basándose en tendencias de mercado y el perfil de su negocio.

Cada una de estas pestañas actuará como un punto de acceso principal a su respectivo módulo, asegurando una experiencia de usuario fluida y organizada.

## Preguntas para el Árbol de Decisiones Inicial

Para avanzar con el diseño detallado y la implementación de la Fase 1, necesito su validación y algunas definiciones clave. Por favor, responda a las siguientes preguntas:

## Decisiones Técnicas Clave

Basado en las definiciones proporcionadas, las decisiones técnicas clave para el MVP "Global Connect" son las siguientes:

*   **Plataforma de Desarrollo:** Enfoque multiplataforma utilizando **React Native o Flutter** para cubrir iOS y Android simultáneamente.
*   **Tecnología de Backend:** **Python (Django o FastAPI)** para asegurar la integración nativa con los modelos de IA.
*   **Base de Datos:** **PostgreSQL** para garantizar la integridad transaccional del catálogo B2B.
*   **Autenticación de Usuarios:** Sistema **híbrido** que incluirá Email/Contraseña y Social Login (Google/Apple) para minimizar la fricción en el registro.
*   **Diseño de UI/UX:** Uso de componentes estándar (Material Design/Human Interface Guidelines) con una guía de estilo personalizada que refleje el rebranding de Global Imports hacia lo digital.

Estas decisiones guiarán el diseño y la implementación de las funcionalidades críticas.
