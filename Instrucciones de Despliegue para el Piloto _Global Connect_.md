# Instrucciones de Despliegue para el Piloto "Global Connect"

Este documento proporciona las instrucciones esenciales para el equipo de operaciones para el despliegue y monitoreo del piloto del MVP "Global Connect" con los 15 clientes minoristas.

## 1. Pre-requisitos

*   **Entorno Cloud:** Acceso a una cuenta de Google Cloud Platform (GCP) o Amazon Web Services (AWS) con permisos de administrador.
*   **Contenedores:** Docker y Kubernetes (GKE/EKS) configurados para el despliegue de microservicios.
*   **Base de Datos:** Instancia de PostgreSQL gestionada (Cloud SQL en GCP o RDS en AWS) con credenciales de acceso.
*   **Dominio:** Un subdominio configurado para la API de backend (ej. `api.globalconnect.com`) y para la aplicación Streamlit (ej. `simulator.globalconnect.com`).
*   **Certificados SSL:** Certificados SSL/TLS configurados para ambos dominios.

## 2. Despliegue del Backend (Python FastAPI/Django)

El backend se desplegará como un microservicio en un clúster de Kubernetes.

### Pasos:

1.  **Clonar Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_BACKEND>
    cd global_connect_mvp/src/api
    ```
2.  **Configurar Variables de Entorno:**
    Crear un archivo `.env` con las siguientes variables:
    ```
    DATABASE_URL="postgresql://user:password@host:port/dbname"
    SECRET_KEY="your_super_secret_key"
    # Otras variables de configuración para IA, autenticación, etc.
    ```
3.  **Construir Imagen Docker:**
    ```bash
    docker build -t global-connect-backend:latest .
    ```
4.  **Subir Imagen a Registro de Contenedores:**
    ```bash
    docker tag global-connect-backend:latest gcr.io/<PROJECT_ID>/global-connect-backend:latest # Para GCP
    docker push gcr.io/<PROJECT_ID>/global-connect-backend:latest
    # O para AWS ECR: aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
    # docker tag global-connect-backend:latest <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/global-connect-backend:latest
    # docker push <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/global-connect-backend:latest
    ```
5.  **Desplegar en Kubernetes:**
    Aplicar los manifiestos de Kubernetes (Deployment, Service, Ingress) para el backend. Asegurarse de que el Ingress apunte al subdominio `api.globalconnect.com` y utilice los certificados SSL.
    ```bash
    kubectl apply -f k8s/backend-deployment.yaml
    kubectl apply -f k8s/backend-service.yaml
    kubectl apply -f k8s/backend-ingress.yaml
    ```

## 3. Despliegue del Microservicio IA Smart Curator

El microservicio de IA se desplegará de manera similar al backend.

### Pasos:

1.  **Clonar Repositorio:** (Si es un repositorio separado, de lo contrario, usar el mismo)
    ```bash
    git clone <URL_DEL_REPOSITORIO_IA>
    cd global_connect_mvp/src/api # O la ruta del microservicio IA
    ```
2.  **Configurar Variables de Entorno:** (Si aplica)
3.  **Construir Imagen Docker:**
    ```bash
    docker build -t global-connect-ai-curator:latest .
    ```
4.  **Subir Imagen a Registro de Contenedores:**
    ```bash
    docker tag global-connect-ai-curator:latest gcr.io/<PROJECT_ID>/global-connect-ai-curator:latest
    docker push gcr.io/<PROJECT_ID>/global-connect-ai-curator:latest
    ```
5.  **Desplegar en Kubernetes:**
    Aplicar los manifiestos de Kubernetes (Deployment, Service) para el microservicio de IA.
    ```bash
    kubectl apply -f k8s/ai-curator-deployment.yaml
    kubectl apply -f k8s/ai-curator-service.yaml
    ```

## 4. Despliegue del Simulador Financiero (Streamlit)

El simulador de Streamlit se puede desplegar en un entorno de servidor web o como una aplicación de Streamlit Cloud.

### Opción A: Despliegue en Servidor Web (Docker/Kubernetes)

1.  **Clonar Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_FRONTEND>
    cd global_connect_mvp/src/app
    ```
2.  **Construir Imagen Docker:**
    Crear un `Dockerfile` para la aplicación Streamlit:
    ```dockerfile
    FROM python:3.9-slim-buster
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    EXPOSE 8501
    CMD ["streamlit", "run", "financial_simulator_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
    ```
    ```bash
    docker build -t global-connect-simulator:latest .
    ```
3.  **Subir Imagen a Registro de Contenedores:**
    ```bash
    docker tag global-connect-simulator:latest gcr.io/<PROJECT_ID>/global-connect-simulator:latest
    docker push gcr.io/<PROJECT_ID>/global-connect-simulator:latest
    ```
4.  **Desplegar en Kubernetes:**
    Aplicar los manifiestos de Kubernetes (Deployment, Service, Ingress) para el simulador. Asegurarse de que el Ingress apunte al subdominio `simulator.globalconnect.com` y utilice los certificados SSL.
    ```bash
    kubectl apply -f k8s/simulator-deployment.yaml
    kubectl apply -f k8s/simulator-service.yaml
    kubectl apply -f k8s/simulator-ingress.yaml
    ```

### Opción B: Despliegue en Streamlit Cloud

1.  **Crear Repositorio Git:** Asegurarse de que el código del simulador (`financial_simulator_app.py` y `requirements.txt`) esté en un repositorio Git público (GitHub, GitLab, Bitbucket).
2.  **Conectar a Streamlit Cloud:** Acceder a [Streamlit Cloud](https://share.streamlit.io/) y conectar el repositorio.
3.  **Configurar Despliegue:** Seleccionar el archivo principal (`financial_simulator_app.py`) y la rama. Streamlit Cloud se encargará automáticamente del despliegue y la gestión de la URL.

## 5. Monitoreo y Observabilidad

*   **Logs:** Configurar la ingesta de logs de Kubernetes a una herramienta centralizada (Stackdriver Logging, CloudWatch Logs, ELK Stack).
*   **Métricas:** Implementar monitoreo de métricas (Prometheus/Grafana) para CPU, memoria, latencia de API y errores.
*   **Alertas:** Configurar alertas para umbrales críticos (ej. alta tasa de error, baja disponibilidad).

## 6. Gestión de Clientes del Piloto

*   **Onboarding:** Proporcionar a los 15 clientes minoristas las credenciales de acceso a la aplicación móvil y una guía de usuario rápida.
*   **Soporte:** Establecer un canal de soporte dedicado para resolver dudas y recoger feedback.
*   **Recolección de Datos:** Asegurar que los sistemas de analítica (ej. Google Analytics, Mixpanel) estén configurados para recolectar datos de uso y comportamiento de los usuarios del piloto.

Este plan de despliegue asegura una puesta en marcha controlada y monitoreada del MVP, permitiendo la recolección de datos cruciales para la validación y futuras iteraciones.
