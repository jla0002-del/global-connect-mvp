# Esquema Técnico Detallado del MVP "Global Connect"

Este documento detalla el diseño de las funcionalidades críticas para el MVP de la aplicación "Global Connect", basándose en las decisiones técnicas previamente definidas.

## 1. Catálogo Digital Interactivo

### Descripción
Sustitución de catálogos físicos por una interfaz móvil de alta velocidad que permite a los minoristas explorar, filtrar y visualizar productos artesanales de manera eficiente.

### Diseño de UI/UX
*   **Navegación:** Accesible desde la pestaña principal "Catálogo".
*   **Visualización:** Grid view o list view con imágenes de alta resolución, nombre del producto, precio y disponibilidad.
*   **Filtros y Búsqueda:** Opciones de filtrado por categoría, región de origen, tipo de artesanía, precio, etc. Barra de búsqueda con autocompletado.
*   **Detalle del Producto:** Al seleccionar un producto, se mostrará una pantalla con múltiples imágenes, descripción detallada, información del artesano, stock disponible y opciones de compra.
*   **Interacción:** Posibilidad de añadir productos a una lista de deseos o a un carrito de compras temporal.

### Componentes Técnicos (Frontend)
*   **React Native/Flutter:** Implementación de componentes de UI para grids, listas, carruseles de imágenes, barras de búsqueda y filtros.
*   **Gestión de Estado:** Uso de Redux, Context API o Provider para manejar el estado del catálogo y el carrito.
*   **Consumo de API:** Interacción con el `catalog_api.py` del backend para obtener datos de productos.

### Componentes Técnicos (Backend)
*   **Python (Django/FastAPI):** Endpoint `/api/v1/catalog` para listar productos, `/api/v1/catalog/{id}` para detalles de producto.
*   **Base de Datos (PostgreSQL):** Tablas `products`, `categories`, `artisans` con relaciones adecuadas para almacenar la información del catálogo.
*   **Optimización:** Implementación de paginación, caching y compresión de imágenes para asegurar alta velocidad.

## 2. Gestión de Pedidos "One-Tap"

### Descripción
Funcionalidad que permite la compra directa de productos con un solo toque, eliminando la fricción analógica y las llamadas telefónicas.

### Diseño de UI/UX
*   **Navegación:** Accesible desde la pestaña principal "Pedidos" y desde la pantalla de detalle del producto.
*   **Botón "One-Tap":** Un botón prominente en la pantalla de detalle del producto que inicia el proceso de compra rápida.
*   **Confirmación:** Una pantalla de confirmación concisa que muestra el resumen del pedido (producto, cantidad, precio total, dirección de envío) antes de la compra final.
*   **Historial de Pedidos:** Dentro de la pestaña "Pedidos", un listado de todos los pedidos realizados con su estado actual.

### Componentes Técnicos (Frontend)
*   **React Native/Flutter:** Implementación de la lógica del botón "One-Tap" y la interfaz de confirmación.
*   **Formularios:** Manejo de la dirección de envío y métodos de pago preestablecidos.
*   **Consumo de API:** Interacción con el `orders_api.py` del backend para crear y gestionar pedidos.

### Componentes Técnicos (Backend)
*   **Python (Django/FastAPI):** Endpoint `/api/v1/orders` para crear nuevos pedidos, `/api/v1/orders/{id}` para ver detalles de un pedido.
*   **Base de Datos (PostgreSQL):** Tablas `orders`, `order_items`, `addresses`, `payments` para gestionar la información de los pedidos.
*   **Transacciones:** Asegurar la atomicidad de las transacciones para evitar inconsistencias en el stock y los pagos.

## 3. Módulo de Seguimiento Básico

### Descripción
Panel de trazabilidad para pedidos internacionales que permite a los minoristas consultar el estado de sus envíos (Aduanas, En tránsito, Entregado).

### Diseño de UI/UX
*   **Navegación:** Accesible desde la pestaña principal "Tracking".
*   **Listado de Envíos:** Una lista de todos los pedidos con información de seguimiento, incluyendo número de pedido, producto principal y estado actual.
*   **Detalle de Seguimiento:** Al seleccionar un envío, se mostrará una línea de tiempo o una serie de hitos con la fecha y descripción de cada estado (e.g., "En Aduanas - 2026-06-10", "En Tránsito - 2026-06-12", "Entregado - 2026-06-15").
*   **Notificaciones:** Opcional: notificaciones push para cambios de estado importantes.

### Componentes Técnicos (Frontend)
*   **React Native/Flutter:** Implementación de la interfaz de seguimiento con listas y vistas de detalle.
*   **Consumo de API:** Interacción con el `tracking_api.py` del backend para obtener datos de seguimiento.

### Componentes Técnicos (Backend)
*   **Python (Django/FastAPI):** Endpoint `/api/v1/tracking/{order_id}` para obtener el estado de un pedido.
*   **Base de Datos (PostgreSQL):** Tabla `shipments` con campos como `order_id`, `status`, `last_update`, `location`.
*   **Integración Externa:** Posible integración con APIs de transportistas o sistemas de aduanas (para el MVP, se puede simular o usar datos estáticos).

## 4. Smart Curator (IA)

### Descripción
Motor de recomendaciones impulsado por inteligencia artificial que sugiere stock al minorista basado en tendencias de mercado y el perfil de su negocio.

### Diseño de UI/UX
*   **Navegación:** Accesible desde la pestaña principal "IA Smart Curator".
*   **Panel de Recomendaciones:** Una sección que muestra productos recomendados, quizás categorizados por "Tendencias Actuales", "Para Tu Tienda" o "Novedades Exclusivas".
*   **Justificación:** Breve explicación de por qué se recomienda un producto (e.g., "Alta demanda en tu región", "Complementa tu inventario actual").
*   **Interacción:** Posibilidad de "Me gusta" o "No me gusta" para refinar las recomendaciones, o añadir directamente al carrito.

### Componentes Técnicos (Frontend)
*   **React Native/Flutter:** Implementación de la interfaz de usuario para mostrar las recomendaciones de forma atractiva.
*   **Consumo de API:** Interacción con el `smart_curator_api.py` del backend para obtener las recomendaciones.

### Componentes Técnicos (Backend)
*   **Python (Django/FastAPI):** Endpoint `/api/v1/smart_curator/recommendations` que recibe el ID del minorista y devuelve una lista de productos recomendados.
*   **Modelos de IA:** Implementación de un modelo de recomendación (e.g., filtrado colaborativo, basado en contenido, o híbrido) utilizando librerías de Python (TensorFlow, PyTorch, Scikit-learn).
*   **Base de Datos (PostgreSQL):** Almacenamiento de datos de comportamiento del usuario, historial de compras, interacciones con productos para alimentar el modelo de IA.
*   **Procesamiento de Datos:** Un pipeline de datos para preprocesar la información y entrenar/actualizar el modelo de IA periódicamente.

## Próximos Pasos

Con este esquema técnico detallado, el siguiente paso es la validación de esta Fase 1 antes de proceder con la implementación o la Fase 2.
