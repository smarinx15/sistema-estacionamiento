# \# 🅿️ Sistema de Estacionamiento

# 

# Sistema de gestión de estacionamiento desarrollado en Python que permite administrar el ingreso, salida y cobro de vehículos (automóviles, motocicletas y bicicletas), así como la gestión de mensualidades.

# 

# \## 📋 Características

# 

# \- \*\*Gestión de Tarifas\*\*: Configuración flexible de tarifas por minuto para cada tipo de vehículo

# \- \*\*Registro de Vehículos\*\*: 

# &nbsp; - Automóviles (formato: ABC123)

# &nbsp; - Motocicletas (formato: ABC12D)

# &nbsp; - Bicicletas (sistema de consecutivo automático)

# \- \*\*Sistema de Mensualidades\*\*: Control de mensualidades con vigencia de 30 días

# \- \*\*Cálculo Automático\*\*: Calcula tiempo de estadía y monto a cobrar

# \- \*\*Sistema de Facturación\*\*: Generación de facturas con número único

# \- \*\*Búsqueda Avanzada\*\*: Búsqueda por placa, consecutivo o número de factura

# \- \*\*Reportes\*\*: Visualización de registros por tipo de vehículo

# \- \*\*Cuadre de Caja\*\*: Reporte consolidado de ingresos

# 

# \## 🚀 Requisitos

# 

# \- Python 3.6 o superior

# \- No requiere librerías externas

# 

# \## 💻 Instalación y Uso

# 

# 1\. Clona este repositorio:

# ```bash

# git clone https://github.com/smarinx15/sistema-estacionamiento.git

# ```

# 

# 2\. Navega a la carpeta del proyecto:

# ```bash

# cd sistema-estacionamiento

# ```

# 

# 3\. Ejecuta el programa:

# ```bash

# python ESTACIONAMIENTO-VERSIONFINAL.py

# ```

# 

# \## 📖 Guía de Uso

# 

# \### Menú Principal

# 

# 1\. \*\*Tarifas\*\* - Configurar precios

# 2\. \*\*Registrar mensualidad\*\* - Registro de planes mensuales

# 3\. \*\*Ingresar vehículo\*\* - Registrar entrada

# 4\. \*\*Buscar vehículo\*\* - Búsqueda individual

# 5\. \*\*Mostrar registros\*\* - Ver todos los registros

# 6\. \*\*Mostrar Mensualidades\*\* - Ver mensualidades activas

# 7\. \*\*Salida vehículo\*\* - Registrar salida y cobrar

# 8\. \*\*Buscar Factura\*\* - Consultar factura

# 9\. \*\*Cuadre de Caja\*\* - Reporte de ingresos

# 10\. \*\*Salir\*\* - Cerrar sistema

# 

# \### Formatos Requeridos

# 

# \- \*\*Placas de Automóvil\*\*: 3 letras + 3 números (Ejemplo: `ABC123`)

# \- \*\*Placas de Motocicleta\*\*: 3 letras + 2 números + 1 letra (Ejemplo: `ABC12D`)

# \- \*\*Fecha\*\*: `ddmmyyyy` (Ejemplo: `17102025`)

# \- \*\*Hora\*\*: `hhmm` formato 24 horas (Ejemplo: `1430` para 2:30 PM)

# 

# \## 🎯 Ejemplo de Uso

# 

# ```

# 1\. Configure las tarifas en el menú Tarifas

# &nbsp;  - Automóvil: $50 por minuto

# &nbsp;  - Moto: $30 por minuto

# &nbsp;  - Bicicleta: $20 por minuto

# &nbsp;  - Mensualidad: $100,000

# 

# 2\. Ingrese un vehículo

# &nbsp;  - Tipo: Automóvil

# &nbsp;  - Placa: ABC123

# &nbsp;  - Hora: 0900

# &nbsp;  - Fecha: 17102025

# 

# 3\. Registre la salida

# &nbsp;  - Placa: ABC123

# &nbsp;  - Hora salida: 1030

# &nbsp;  - Tiempo: 90 minutos

# &nbsp;  - Total a pagar: $4,500

# ```

# 

# \## 🛠️ Funcionalidades Principales

# 

# \### Sistema de Mensualidades

# \- Vigencia de 30 días desde la fecha de registro

# \- Exención automática de cobro para vehículos con mensualidad vigente

# \- Control de fechas de vencimiento

# 

# \### Cálculo de Cobro

# \- Cálculo automático de minutos transcurridos

# \- Aplicación de tarifa según tipo de vehículo

# \- Generación de factura detallada

# 

# \### Validaciones

# \- Formato de placas según tipo de vehículo

# \- Validación de fechas (día, mes, año)

# \- Validación de horas (formato 24h)

# \- Detección de placas duplicadas

# \- Validación de hora de salida mayor a hora de entrada

# 

# \## 📊 Estructura de Datos

# 

# El sistema almacena:

# \- Registro de vehículos con entrada/salida

# \- Mensualidades activas

# \- Facturas generadas

# \- Tarifas configuradas

# 

# \## 👤 Autor

# 

# \*\*Santiago Marín\*\*

# \- GitHub: \[@smarinx15](https://github.com/smarinx15)

# 

# \## 📄 Licencia

# 

# Este proyecto está bajo la Licencia MIT.

# 

# \## 🤝 Contribuciones

# 

# Las contribuciones son bienvenidas. Si deseas mejorar el proyecto:

# 

# 1\. Haz fork del repositorio

# 2\. Crea una rama para tu mejora (`git checkout -b feature/mejora`)

# 3\. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)

# 4\. Haz push a la rama (`git push origin feature/mejora`)

# 5\. Abre un Pull Request

# 

# \## 📞 Soporte

# 

# Si tienes preguntas o encuentras algún problema, abre un \[Issue](https://github.com/smarinx15/sistema-estacionamiento/issues) en GitHub.

# 

# ---

# 

# ⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub

