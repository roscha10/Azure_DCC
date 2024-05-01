
![WhatsApp Image 2024-04-29 at 11 02 07 AM](https://github.com/roscha10/Azure_DCC/assets/130667173/d624ba20-ac2a-49ec-be9d-6fd5e4457470)

# Servicios de Azure para análisis de datos, enfocado en las empresas de NASDAQ-100 y un estudio detallado sobre sus 10 principales empresas por capitalización de mercado

<div style="overflow: auto;">
  <img src="image/MicrosoftAzure.png" alt="Azure" style="float: left; margin-right: 10px; width: 200px;">
  ¡Hola a todos, miembro de la comunidad de Data Cloud Club de Henry y entusiastas de Azure! Prepárense para explorar el emocionante mundo del análisis de datos usando Azure, abordando el conjunto completo de empresas listadas en el NASDAQ-100 Con un especial énfasis en las 10 principales compañías por capitalización de mercado. Esta presentación está diseñada tanto para principiantes como para estudiantes que están dando sus primeros pasos en la nube de Azure y la ciencia de datos; exploraremos cómo iniciar con Azure aprovechando el crédito inicial de $200 ofrecido en el primer mes de la suscripción. Este crédito es una excelente oportunidad para aprender y aplicar las herramientas de Azure sin costo inicial, permitiéndonos explorar, experimentar y ejecutar proyectos de análisis de datos de manera efectiva.
</div>

# Estos son los temas y contenidos que vamos a profundizar y tratar de explicar detalladamente:

•	Fundamentos de Azure
•	Automatización de Procesos con Azure Functions
•	Programación en Python para el Análisis de Datos
•	Gestión de Datos en Azure Blob Storage

# Descripción General del Proyecto:

Este proyecto se centra en el análisis detallado de las empresas con mayor capitalización de mercado del NASDAQ-100, utilizando para ello los avanzados servicios de Azure. El objetivo es proporcionar a estudiantes y principiantes una comprensión profunda de cómo se pueden aplicar las soluciones de Azure en el ámbito del análisis de datos financieros.
Al comenzar, los participantes aprenderán a configurar su entorno Azure, aprovechando un crédito inicial de $200 ofrecido por Azure para explorar y utilizar sus diversos servicios sin coste inicial. Esta oportunidad permite a los usuarios familiarizarse con la plataforma, practicar la configuración de recursos y gestionar datos de manera efectiva sin preocupaciones económicas durante el primer mes, algunos siempre seran gratis.

Aquí está el diagrama que muestra el flujo de trabajo del proyecto que vamos a construir:

<img src="image/WhatsApp Image 2024-04-29 at 11.02.07 AM.jpeg" width="300">


# El proyecto abarca varios componentes clave:

1.	Configuración de Azure: Los participantes aprenderán a crear y gestionar grupos de recursos, configurar cuentas de almacenamiento y organizar datos utilizando contenedores en Azure Blob Storage.
2.	Automatización con Azure Functions Se introducirán los fundamentos de Azure Functions para automatizar la ingestión y el flujo de datos, para manejar grandes volúmenes de información.
3.	Programación en Python para análisis de datos: A través de ejercicios prácticos, los estudiantes utilizarán Python para extraer datos de fuentes en línea como Wikipedia y APIs financieras, y aprenderán a manipular y preparar estos datos con la biblioteca Pandas.
4.	Integración de Python con Azure Blob Storage: Se explicará cómo subir y descargar datos de manera eficiente, facilitando la interacción entre scripts locales y la nube.
5.	Análisis y visualización avanzada: Utilizando Azure Synapse Analytics para análisis profundos y Power BI para visualizar y presentar los resultados, los participantes podrán convertir datos crudos en insights accionables y visualmente atractivos.

Este proyecto mejorará las habilidades técnicas de los participantes en el uso de Azure y Python y también proporcionará una gran experiencia en el análisis de datos reales del mercado financiero, preparando a los estudiantes para futuras carreras en la ciencia de datos y la ingeniería de datos. Al final del proyecto, los participantes habrán completado un análisis de datos de principio a fin, utilizando algunas de las herramientas más potentes disponibles en la tecnología de la nube.


*Antes de profundizar en cómo estructurar nuestro proyecto de análisis de datos en Azure, es importante mencionar que esta guía es solo una de las muchas maneras en que se puede aprovechar la nube para nuestros fines. Cada participante del proyecto tiene la libertad y es alentado a aportar sus propias ideas y sugerencias. Valoramos enormemente la diversidad de enfoques y consideramos que cada propuesta diferente ya que enriquece nuestro proyecto, y contribuye significativamente a nuestra comunidad. Con esto en mente, les presentamos nuestra sugerencia para desarrollar este proyecto, esperando que sirva como punto de partida para futuras innovaciones y personalizaciones.*

# Sugerencia  para desarrollar este proyecto:

## 1. Acceso a Azure y Utilización del Crédito Inicial:

**Desbloqueo de Azure con el Crédito Inicial de $200:**

•	Dirígete a la página oficial de Microsoft Azure ([Azure Free Account](https://azure.microsoft.com/en-us/free/)). Aquí encontrarás información sobre la cuenta gratuita que incluye $200 de crédito para usar durante los primeros 30 días.

•	**Crear una cuenta de Microsoft:** Si aún no tienes una, deberás crear una cuenta de Microsoft. Puedes hacerlo desde el mismo portal de Azure.


•	**Iniciar el proceso de registro para Azure**: Haz clic en "Start free", y serás guiado a través del proceso de registro.

•	**Proporcionar detalles personales:** Durante el proceso de registro, se te pedirá que ingreses información personal básica.


•	**Verificación de teléfono:** Azure requiere una verificación de teléfono para ayudar a proteger tu identidad. Deberás ingresar tu número de teléfono para recibir un código de verificación.

•	**Información de la tarjeta de crédito:** Aunque no se te cobrará durante el periodo de prueba gratuito, Azure requiere una tarjeta de crédito para configurar la cuenta. Esto es para asegurarse de que puedas continuar usando los servicios sin interrupción después de que el crédito inicial o el periodo gratuito termine, Es importante saber que Azure no realizará cargos en tu tarjeta de crédito durante el período de prueba, ni después de este, a menos que decidas cambiar de plan y autorices explícitamente esos cargos. Esto te da control completo sobre tu plan de gastos y asegura que no habrá costos inesperados.


•	**Confirmación de la cuenta:** Una vez que ingreses todos los detalles necesarios y completes la verificación, tu cuenta será activada.

•	**Recepción del crédito de $200:** El crédito de $200 estará automáticamente disponible en tu cuenta una vez que la activación sea exitosa.


  <img src="image/azure00.jpeg" alt="" width="600">



•	**Iniciar sesión en Azure Portal:**  Con tus credenciales de Microsoft, inicia sesión en Azure Portal.

## 2. Configuración de Azure:

**Creación del Grupo de Recursos:**
1.	Inicia sesión en el Portal de Azure.
2.	En el panel de navegación izquierdo, haz clic en "Crear un recurso".
3.	Busca "Grupo de recursos" y selecciona la opción correspondiente.
4.	En el formulario, proporciona un nombre para el grupo de recursos, en este caso, **DataFactoryResources.**
5.	Selecciona la región más adecuada para tu proyecto.
6.	Haz clic en "Revisar y crear", y luego en "Crear".

![image](https://github.com/roscha10/Azure_DCC/assets/130667173/226c1220-d708-4fd9-8695-9c1e59334f98)

![image](https://github.com/roscha10/Azure_DCC/assets/130667173/300bb078-cfd3-42f1-bc3c-39eab21ff418)

## 3. Creación de la Cuenta de Almacenamiento:

1.	Dentro del grupo de recursos DataFactoryResources, haz clic en "Agregar" o "Crear recurso".
   ![image](https://github.com/roscha10/Azure_DCC/assets/130667173/f1b71e7f-78c5-47a7-b542-16f817e0fe2a)
	
2.	En la barra de búsqueda, busca "Cuenta de almacenamiento" y selecciona la opción correspondiente.
3.	En la configuración básica, asigna el nombre.
4.	Asegúrate de que el grupo de recursos seleccionado sea le grupo de recursos creado, en este caso DataFactoryResources.  
5.	Configura los detalles específicos como el rendimiento (estándar/premium), el tipo de cuenta y la replicación según las necesidades del proyecto.  
6.	Selecciona la misma región o la más cercana a la de tu grupo de recursos para optimizar la latencia.  
7.	Haz clic en "Revisar y crear" y, una vez validados los detalles, en "Crear".


<img src="image/azure8.jpg" alt="" width="600">

<img src="image/azure9.jpg" alt="" width="600">

## 4. Creación de un contenedor, dentro de la cuenta de almacenamiento:

El siguiente paso es crear un contenedor. Dentro de la cuenta ADLS, ubique y seleccione la sección "Contenedores", haga clic en  "+ Contenedor" e ingrese el nombre deseado para el contenedor, por ejemplo, "marketdata", luego haga clic en crear.

<img src="image/azure13.jpg" alt="" width="600">

El siguiente paso es crear dos directorios dentro de este contenedor. Navegue hasta el contenedor específico, haga clic en "Cargar". Ingrese el nombre del directorio como "datos sin procesar" y confirme la creación. Haga clic en "Agregar directorio" nuevamente e ingrese el nombre del directorio como "datos transformados" y confirme la creación. Esta es una forma común de organizar datos.

<img src="image/azure15.jpg" alt="" width="600">

## 5. Automatización con Azure Functions: 

### Paso 1: Crear una Aplicación de Funciones

1.	**Accede al Portal de Azure:**
	•	Ingresa a ([Azure Portal](https://portal.azure.com)) usando tus credenciales.    
2.	**Navega a Aplicaciones de Funciones:**  
	•	Puedes encontrarlo buscando "Aplicaciones de funciones" en la barra de búsqueda del portal o dentro del menú de servicios.    
3.	**Crear una Nueva Aplicación de Funciones:**  
	•	Haz clic en "Agregar" o "Crear" para iniciar la configuración de una nueva Aplicación de Funciones.      
	•	Se te presentará un formulario para configurar la nueva aplicación.    
4.	**Configura los Detalles de la Aplicación:**    
	•	Suscripción: Selecciona la suscripción de Azure que usarás.  
	•	Grupo de recursos: Elige el grupo de recursos que ya creaste.  
	•	Nombre de la aplicación de funciones: Asigna un nombre único.  
	•	Publicar: Elige "Código" para subir código directamente.  
	•	Pila de ejecución: Selecciona "Python".  
	•	Versión: Elige la versión de Python que tu script necesita.  
	•	Región: Escoge la región más conveniente para minimizar la latencia.  
5.	**Revisión y Creación:**
	•	Haz clic en "Revisar y crear" para verificar tu configuración.
	•	Finaliza haciendo clic en "Crear" para desplegar la Aplicación de Funciones.

<img src="image/azurefunction.jpg" alt="" width="600">

### Paso 2: Desarrollar y Desplegar el Script de Python
1.	**Desarrolla tu Script Localmente:**  
	•	Asegúrate de que tu script de Python realiza las tareas deseadas (ej., acceder a datos, procesarlos, y prepararlos para la carga).    
	•	Incluye las bibliotecas necesarias para interactuar con Azure Blob Storage, como azure-storage-blob.    
2.	**Prueba tu Script Localmente:**  
	•	Ejecuta el script en tu entorno local para asegurarte de que funciona correctamente antes de subirlo a Azure.    
3.	**Prepara tu Entorno de Desarrollo:**  
	•	Instala la extensión de Azure Functions en VS Code si aún no lo has hecho. Esto se puede hacer desde la barra lateral de extensiones buscando "Azure Functions" y haciendo clic en instalar.    
	•	Desde la paleta de comandos, Escribe y selecciona "Azure Functions: Create New Project...".    

<img src="image/azuref1.png" alt="Descripción de la imagen" width="660">  

•	Asegúrate de que la carpeta del proyecto esté seleccionada, es recomendable crear una carpeta exclusiva para Azure Function.  
•	Elige "Python" como lenguaje de programación para tu proyecto de Azure Functions.  
•	Selecciona el entorno de Python que quieras usar (deberías tener Python ya instalado).  
•	Pasos para crear el "TimerTrigger" como tipo de disparador para ejecutar cada tiempo determinado.
1.	En VS Code, asegúrate de tener instalada la extensión de Azure Functions.
2.	Abre la paleta de comandos con Ctrl+Shift+P.
3.	Escribe y selecciona "Azure Functions: Create Function...".
4.	Sigue los pasos y elige "TimerTrigger" como tipo de disparador.
   
<img src="image/azuref2.png" alt="Descripción de la imagen" width="660">

5.	Proporciona un nombre a la función, como DailyDataUpdater.
6.	Establece el cronograma con una expresión CRON que represente tu necesidad (por ejemplo, 0 0 0 * * * para ejecutar a medianoche todos los días).
7.	Selecciona "Create New Blueprint File" cuando se te pregunte dónde colocar la función.  


<img src="image/azuretrigger.jpg" alt="Descripción de la imagen" width="660">

## 6. Sube tu Script a Azure:
Después de haber desarrollado y probado tu script localmente, es el momento de llevarlo a la nube de Azure para su ejecución automatizada. Sigue estos pasos para subir tu script a Azure Functions:
Accede al Portal de Azure utilizando tus credenciales de Microsoft.  
 
• Navega a la sección de Aplicaciones de Funciones dentro del menú de servicios.  
• Haz clic en "Agregar" o "Crear" para iniciar la configuración de una nueva Aplicación de Funciones.  
• Rellena los detalles de la aplicación, asegurándote de seleccionar la suscripción correcta y el grupo de recursos apropiado.  
• Asigna un nombre único a tu aplicación de funciones y elige la pila de ejecución Python con la versión adecuada.   
• Sube tu script de Python y cualquier otro archivo necesario a través del portal de Azure o mediante herramientas como Visual Studio Code.  
• Verifica que tu función se haya desplegado correctamente y realiza pruebas adicionales para asegurarte de que funcione como se espera en el entorno de Azure.  

**Al completar este paso, tu script estará listo para ejecutarse automáticamente en Azure, proporcionándote un análisis de datos continuo y escalable basado en la nube.**
