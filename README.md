# 🚗 Sistema de Gestión de Estacionamiento



![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

API REST para la gestión integral de un sistema de estacionamiento, desarrollada con FastAPI y arquitectura moderna.

---

## 📋 Descripción

Sistema backend que permite administrar espacios de estacionamiento, registrar vehículos, controlar entradas/salidas y calcular tarifas. Ideal para estacionamientos comerciales, centros comerciales o edificios corporativos.

---

## ✨ Características

- 🚗 **Gestión de Vehículos**: CRUD completo de vehículos
- 📍 **Control de Espacios**: Administración de plazas disponibles
- ⏱️ **Registro de Entradas/Salidas**: Control de tiempo en tiempo real
- 💰 **Cálculo de Tarifas**: Cálculo automático según tiempo de permanencia
- 📊 **Reportes**: Estadísticas de ocupación y ganancias
- 🔒 **Validación de Datos**: Validación con Pydantic
- 📚 **Documentación Automática**: Swagger UI y ReDoc integrados

---

## 🛠️ Tecnologías

- **FastAPI** - Framework web moderno y rápido
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI
- **Python 3.8+** - Lenguaje de programación

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/smarinx15/estacionamiento.git
   cd estacionamiento
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor**
   ```bash
   uvicorn main:app --reload
   ```

5. **Abrir en el navegador**
   - API: `http://localhost:8000`
   - Documentación: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

---

## 📡 API Endpoints

### Vehículos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/vehiculos` | Listar todos los vehículos |
| `GET` | `/vehiculos/{id}` | Obtener vehículo por ID |
| `POST` | `/vehiculos` | Registrar nuevo vehículo |
| `PUT` | `/vehiculos/{id}` | Actualizar vehículo |
| `DELETE` | `/vehiculos/{id}` | Eliminar vehículo |

### Espacios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/espacios` | Listar espacios disponibles |
| `GET` | `/espacios/{id}` | Obtener espacio específico |
| `POST` | `/espacios/{id}/ocupar` | Marcar espacio como ocupado |
| `POST` | `/espacios/{id}/liberar` | Liberar espacio |

### Tickets

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/tickets/entrada` | Registrar entrada de vehículo |
| `POST` | `/tickets/salida` | Registrar salida y calcular tarifa |
| `GET` | `/tickets/{id}` | Consultar ticket |

---

## 💡 Ejemplos de Uso

### Registrar Entrada de Vehículo

```bash
curl -X POST "http://localhost:8000/tickets/entrada" \
  -H "Content-Type: application/json" \
  -d '{
    "placa": "ABC123",
    "tipo": "auto",
    "espacio_id": 1
  }'
```

**Respuesta:**
```json
{
  "ticket_id": 1,
  "placa": "ABC123",
  "hora_entrada": "2025-01-15T10:30:00",
  "espacio": 1,
  "mensaje": "Vehículo registrado exitosamente"
}
```

### Registrar Salida y Calcular Tarifa

```bash
curl -X POST "http://localhost:8000/tickets/salida" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket_id": 1
  }'
```

**Respuesta:**
```json
{
  "ticket_id": 1,
  "placa": "ABC123",
  "hora_entrada": "2025-01-15T10:30:00",
  "hora_salida": "2025-01-15T14:45:00",
  "tiempo_total": "4h 15min",
  "tarifa": 25000,
  "mensaje": "Total a pagar: $25,000 COP"
}
```

---

## 📸 Capturas de Pantalla

### Documentación Swagger
![Swagger UI](screenshots/swagger.png)

### Endpoints Disponibles
![Endpoints](screenshots/endpoints.png)

---

## 🗂️ Estructura del Proyecto

```
estacionamiento/
│
├── main.py              # Punto de entrada de la aplicación
├── models.py            # Modelos Pydantic
├── database.py          # Configuración de base de datos
├── routers/             # Endpoints organizados
│   ├── vehiculos.py
│   ├── espacios.py
│   └── tickets.py
├── requirements.txt     # Dependencias
└── README.md           # Este archivo
```

---

## ⚙️ Configuración

### Tarifas

Puedes configurar las tarifas en `config.py`:

```python
TARIFA_HORA = 5000  # COP por hora
TARIFA_MINIMA = 3000  # COP mínimo
TIEMPO_GRACIA = 15  # minutos sin cobro
```

---

## 🧪 Testing

Para ejecutar las pruebas:

```bash
pytest tests/
```

---

## 🚀 Despliegue

### Usando Docker

```bash
docker build -t estacionamiento-api .
docker run -p 8000:8000 estacionamiento-api
```

### En Render/Railway

1. Conecta tu repositorio
2. Configura el comando: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Deploy automático

---

## 🛣️ Roadmap

- [ ] Integración con base de datos (PostgreSQL/MongoDB)
- [ ] Sistema de autenticación (JWT)
- [ ] Pasarela de pagos
- [ ] Dashboard de administración
- [ ] Notificaciones por email/SMS
- [ ] App móvil para clientes
- [ ] Sistema de reservas
- [ ] Reportes en PDF

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Push (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

---

## 👤 Autor

**Santiago Marín**
- GitHub: [@smarinx15](https://github.com/smarinx15)

---

## 🙏 Agradecimientos

- FastAPI por su increíble framework
- La comunidad de Python

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella ⭐**



