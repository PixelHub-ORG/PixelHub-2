# TODO: 
- Hablar del cambio propuesto en Visión global del proceso de desarrollo. (ISMAEL)
- Revisar todo lo escrito en ese punto, hay cosas que no tienen mucho sentido como hablar de Rosemary que no lo hemos implementado nosotros. (no lo veo del todo mal hablar un poco de rosemary) (ISMAEL)
- Guía de instalación HECHO, falta vagrant (HECHO: DIEGO)
- Ejercicio de propuesta de cambio
- Cambiar la visión global, se nota demasiado que es IA  (ISMAEL)
- Rellenar las horas, una vez que esté completo el Clockify, y adjuntar el report (HECHO: DIEGO)

(si hay alguna duda del TODO preguntar a Diego)


El documento del proyecto debe ser un documento que sintetice los aspectos del proyecto elegido para su desarrollo con respecto a los temas vistos en clases. 

Debe tener claramente identificados los nombres y apellidos de cada componente, grupo al que pertenecen (1, 2, o 3 mañana o tarde), curso académico, nombre del proyecto (seguir la política de nombres). Use este [[modelo de portada]] para el documento del proyecto y alójelo en su repositorio o en otro sitio accesible y que tenga posibilidad de verse el último momento de edicación. Puede usar el repositorio del proyecto usando para ello el lenguaje de [markdown](https://guides.github.com/features/mastering-markdown/) que ofrece github. En todo caso, debe ser un documento elaborado en formato [wiki]. 

Será un documento presentado de manera profesional guardando la forma en los estilos y contenidos y con el máximo nivel de rigor académico y profesional.

Tenga en cuenta los siguientes aspectos: 

* Siempre diferencie claramente las secciones y subsecciones y para ello use etiquetas de encabezado como las que se disponen en los lenguajes tipo _markdown_

# Apartados del documento 

El documento del proyecto tendrá (al menos) que sintetizar los siguientes apartados:

## Indicadores del proyecto

(_debe dejar enlaces a evidencias que permitan de una forma sencilla analizar estos indicadores, con gráficas y/o con enlaces_)

Miembro del equipo  | Horas | Commits | LoC | Test | Issues | Work Item| Dificultad
------------- | ------------- | ------------- | ------------- | ------------- | ------------- |  ------------- |  ------------- | 
[Ángel Postigo, Estrella del Carmen](https://github.com/nombredeusuariodegithub) | 59:07 | 12 | 987 | 17 | 4 | Build my own dataset | M |
[Carrasco Mkhazni, Ismael](https://github.com/nombredeusuariodegithub) | 50:26 | 8 | 468 | 3 | 6 | Download own dataset | M |
[Cerdá Morales, Carlos](https://github.com/nombredeusuariodegithub) | 57:25 | 64 | 16.632 | 47 | 9 | Differences between versions | H |
[Founoun El Aoud, Loubna](https://github.com/nombredeusuariodegithub) | 53:42 | 48 | 1.163| 4 | 5 | View user profile | L |
[Moraza Vergara, José Luis](https://github.com/nombredeusuariodegithub) | 51:54 | 23 | 2.930 | 57 | 9 | Upload from Github/Zip | H |
[Terrón Hernández, Diego](https://github.com/nombredeusuariodegithub) | 51:33 | 10 | 698 | 4 | 3 | Auth with ORCID | L |
**TOTAL** | 324:08 | 165  | 22878 | 132 | 36 |  | H(2)/M(2)/L(2) |

[Clockify Report](clockify_report.pdf)

## Integración con otros equipos

* [PixelHub-1](https://github.com/PixelHub-ORG/PixelHub-1): Hemos hecho integración con este grupo para tener un alcance más amplio para nuestro proyecto y optar a la nota máxima.
- [Repositorio conjunto - PixelHub-X](https://github.com/PixelHub-ORG/PixelHub-X): Este es el repositorio en el que se muestra el proyecto final una vez realizada la integración.

## Resumen ejecutivo 

El presente documento detalla la evolución y las optimizaciones aplicadas al proyecto UVLHub, un repositorio especializado en modelos de características (feature models) en formato UVL. Nuestro enfoque principal ha sido elevar la calidad del software mejorando su funcionalidad, eficiencia y la experiencia general del usuario, apoyándonos en metodologías de desarrollo robustas y herramientas modernas.

### Desarrollo y Nuevas Funcionalidades

Durante el ciclo de vida del proyecto, hemos priorizado tanto la corrección de errores críticos como la implementación de nuevas características de alto valor técnico y funcional:

1. **Gestión de Identidad con ORCID:**
   Hemos unificado el acceso a la plataforma mediante la integración con ORCID. Esto facilita el inicio de sesión institucional (por ejemplo, con credenciales de la Universidad de Sevilla) y vincula la actividad del usuario a su perfil académico, el cual puede gestionar desde la nueva sección "Mi Perfil".

2. **Sistema de Carrito y Composición de Datasets:**
   Implementamos una funcionalidad de "Carrito" que transforma la manera de interactuar con los datos. Los usuarios ahora pueden seleccionar modelos específicos (*filemodels*) de diferentes datasets para dos propósitos clave: descargarlos conjuntamente o utilizarlos como base para generar y publicar nuevos datasets derivados directamente desde la plataforma.

3. **Integración con Repositorios Externos (GitHub):**
   Se ha flexibilizado significativamente el formulario de subida de modelos. Además de la carga tradicional mediante archivos ZIP, ahora es posible importar modelos conectando directamente con repositorios de GitHub, agilizando el flujo de trabajo para los desarrolladores.

4. **Control de Versiones y Diferencias:**
   Para mejorar la trazabilidad de los datos, hemos integrado una herramienta de visualización de diferencias (*diffs*). Esto permite a los usuarios comparar y rastrear los cambios específicos entre distintas versiones de un mismo modelo de manera gráfica y sencilla.

5. **Infraestructura de Pruebas: Fakenodo:**
   Para validar la integración con repositorios externos sin depender del entorno de producción de Zenodo, hemos desarrollado e implementado Fakenodo. Su principal aporte técnico es que ha sido construido como un **microservicio independiente**, contando con su propio despliegue en **Render**, al igual que la aplicación principal, garantizando un entorno desacoplado.

### Stack Tecnológico

Para garantizar un desarrollo ágil y pruebas rigurosas, hemos empleado un conjunto de herramientas estándar que incluye **Visual Studio Code**, **MariaDB**, **Selenium** y **Locust** (para pruebas de carga y funcionales). El despliegue de la aplicación y la base de datos se gestiona en **Render**, aunque el proyecto mantiene compatibilidad total con Docker y Vagrant para entornos virtualizados.

La Integración Continua (CI) se gestiona a través de **GitHub Actions**, asegurando que cada modificación en el código sea testeada y notificada automáticamente antes de su fusión, reduciendo drásticamente la introducción de regresiones o fallos.

### Metodología y Flujo de Trabajo

Nuestra estrategia de control de versiones sigue el modelo **EGC-flow**, estructurado en torno a *feature-tasks*. Este enfoque nos permite trabajar en ramas aisladas para cada funcionalidad, las cuales se fusionan frecuentemente con la rama de desarrollo principal (**trunk**). Paralelamente, mantenemos una rama **main** persistente que refleja únicamente las versiones estables y liberadas del producto.

Para agilizar el desarrollo interno, hemos optado por prescindir de las Pull Requests (PR) dentro del equipo, reservando este mecanismo únicamente para integraciones con equipos externos.

### Cultura de Buenas Prácticas

La disciplina ha sido un pilar fundamental en este trabajo. Nos hemos adherido estrictamente a buenas prácticas de ingeniería de software, tales como el mantenimiento de un código limpio, una estructura de ramas coherente y el uso intensivo de integración continua. Esta filosofía de mejora constante nos ha permitido adaptar nuestros procesos ante nuevos desafíos, garantizando entregas de software consistentes y de alta calidad.

### Conclusión

En definitiva, este proyecto ha supuesto una iteración significativa en la mejora de la plataforma UVLHub. Gracias a la combinación de herramientas avanzadas de testing, un flujo de trabajo ágil y una gestión rigurosa del código, hemos logrado optimizar el sistema y ofrecer una experiencia de usuario superior.

## Descripción del sistema

El sistema desarrollado es una plataforma para la gestión, visualización y distribución de **modelos y pixdatasets**. Su objetivo principal es proporcionar a los usuarios una forma eficiente de descubrir, compartir y reutilizar modelos, facilitando la colaboración en diferentes áreas de investigación. Además, permite a los autores disponer de herramientas avanzadas para el control de versiones, la importación de código y la gestión personalizada de sus archivos, optimizando tanto el descubrimiento como la creación de nuevos conjuntos de datos.

La plataforma se basa en un conjunto de subsistemas que interactúan entre sí para proporcionar una experiencia fluida. Entre estos subsistemas se incluyen la gestión unificada de identidad, la manipulación dinámica de *filemodels* a través de un sistema de carrito, y herramientas de integración con repositorios externos.

### **Arquitectura del Sistema**

El sistema está diseñado bajo una arquitectura modular, lo que facilita su mantenimiento, escalabilidad y la incorporación de nuevos estándares como el formato `.pix`. Los componentes principales incluyen:

1. **Autenticación y Gestión de Usuarios**
   - Este subsistema centraliza la identidad del usuario y su información personal, priorizando la accesibilidad institucional y la gestión del perfil.
   - **Inicio de Sesión con ORCID:** Para facilitar el acceso al entorno académico y de investigación, se ha implementado el login mediante **ORCID**. Esto permite a los usuarios (por ejemplo, con cuentas institucionales como la de la Universidad de Sevilla) autenticarse de forma segura sin necesidad de crear credenciales específicas para la plataforma, vinculando su identidad investigadora automáticamente.
   - **Pestaña "Mi Perfil":** Se ha desarrollado un espacio dedicado donde el usuario puede visualizar y editar su información personal, gestionar sus vinculaciones institucionales y revisar su historial de actividad dentro de la plataforma.

2. **Gestión, Creación y Visualización de Datasets**
   - Este módulo es el núcleo funcional de la plataforma, encargado de la manipulación de los modelos `.pix`, la gestión de versiones y la creación de nuevos datasets.
   - **Sistema de Carrito y Filemodels:** Se ha introducido una funcionalidad de **Carrito** transversal a la navegación. Los usuarios pueden seleccionar y añadir archivos individuales (*filemodels*) de diferentes datasets a su carrito. Desde esta interfaz, se habilitan dos acciones clave: descargar el paquete de modelos seleccionados o utilizarlos como base para **crear y publicar un nuevo dataset** propio.
   - **Importación desde GitHub y ZIP:** El formulario de creación y subida de modelos se ha flexibilizado para adaptarse a flujos de trabajo modernos. Ahora permite añadir modelos no solo mediante la carga tradicional de archivos **ZIP**, sino también conectando directamente con repositorios de **GitHub**, facilitando la sincronización con el código fuente del investigador.
   - **Control y Diferencias entre Versiones:** Para mejorar la trazabilidad, el sistema permite visualizar las diferencias entre distintas versiones de un mismo modelo o dataset. Esto ayuda a los usuarios a identificar cambios evolutivos en los archivos `.pix` a lo largo del tiempo.

3. **Servicios de Almacenamiento y Distribución**
   - Los datasets se almacenan garantizando la integridad de los nuevos formatos soportados y su disponibilidad a largo plazo, contando con una infraestructura robusta tanto para producción como para pruebas.
   - **Soporte para Modelos `.pix`:** El sistema de almacenamiento ha sido optimizado para gestionar nativamente el formato `.pix` (reemplazando al estándar anterior `.uvl`), asegurando su correcta indexación y visualización.
   - **Integración con Zenodo:** Se mantiene la integración con Zenodo para la preservación digital. Cuando un usuario publica un dataset finalizado, el sistema puede depositarlo automáticamente en Zenodo para asignarle un DOI, garantizando que los conjuntos de datos sean citables académicamente.
   - **Microservicio de Pruebas (Fakenodo):** Para validar la distribución sin depender del entorno de producción, se ha implementado **Fakenodo**, un simulador de la API de Zenodo. Arquitectónicamente, se ha diseñado como un **servicio independiente con su propio despliegue en Render**, al igual que la aplicación principal. Esto añade valor al sistema al desacoplar el entorno de pruebas y permitir la validación segura de la publicación de datasets.

### **Flujo de Trabajo de la Plataforma**

El flujo de trabajo en la plataforma se organiza en torno a las actividades principales de los usuarios: la autenticación unificada, la creación flexible de datasets y la interacción dinámica con los modelos. El siguiente es un resumen del flujo general actualizado:

1. **Registro y Autenticación:**
   - Los usuarios pueden acceder a la plataforma mediante el registro tradicional o, alternativamente, utilizando su **identificador ORCID**.
   - Esta integración simplifica el acceso institucional (por ejemplo, vinculando la cuenta de la Universidad de Sevilla) y permite gestionar la identidad del investigador de forma centralizada, eliminando barreras de entrada.

2. **Creación y Gestión de Datasets:**
   - La creación de datasets ofrece ahora múltiples vías: los usuarios pueden subir archivos locales (`.zip`, `.pix`), importar el contenido directamente desde un **repositorio de GitHub**, o generar un dataset derivado a partir de modelos recopilados en su **Carrito**.
   - Al publicar el dataset, el sistema gestiona su preservación, comunicándose con la API de **Fakenodo** (nuestro servicio de simulación independiente).

3. **Visualización y Descubrimiento de Datasets:**
   - Los usuarios pueden explorar datasets mediante filtros por etiquetas, autor o comunidad. Además, se ha integrado una herramienta de **visualización de diferencias (Diffs)**, que permite comparar versiones de un modelo para entender su evolución.

4. **Descarga y Sistema de Carrito:**
   - La interacción con los archivos es más granular gracias al **Carrito**. Los usuarios no están limitados a descargar un dataset entero; pueden seleccionar *filemodels* específicos de distintos orígenes y añadirlos a su carrito.
   - Desde ahí, pueden realizar una descarga conjunta de los elementos seleccionados. El sistema registra estas acciones para actualizar los contadores de popularidad, asegurando que las estadísticas reflejen el interés real de la comunidad.

### **Cambios Desarrollados en el Proyecto**

A lo largo del desarrollo de la plataforma, se han implementado y mejorado varias funcionalidades clave. Los cambios más relevantes son los siguientes:

1. **Integración con ORCID y Gestión de Perfil:**
   - Se ha sustituido el registro tradicional por un sistema de inicio de sesión mediante **ORCID**. Esto facilita el acceso institucional (por ejemplo, con cuentas de la Universidad de Sevilla) y permite a los usuarios gestionar su información académica y personal desde la nueva pestaña "Mi Perfil".

2. **Sistema de Carrito y Reutilización de Modelos:**
   - Hemos desarrollado un **Carrito** que transforma la interacción con los datos. Ahora es posible seleccionar *filemodels* individuales de distintos datasets para descargarlos conjuntamente o, lo que es más importante, utilizarlos como base para componer y publicar nuevos datasets derivados directamente desde la plataforma.

3. **Migración a Formato .pix y Visualización de Diferencias:**
   - Se ha realizado una migración completa del estándar de modelos, pasando de `.uvl` a **.pix**. Acompañando este cambio, se ha integrado una herramienta de visualización de diferencias (**Diffs**) que permite a los usuarios comparar gráficamente los cambios entre distintas versiones de un modelo.

4. **Importación Flexible desde GitHub:**
   - Se ha mejorado el formulario de creación de datasets para soportar flujos de trabajo de desarrollo modernos. Además de la subida de archivos ZIP, ahora se permite la importación directa de modelos conectando con repositorios de **GitHub**.

5. **Infraestructura de Pruebas (Fakenodo):**
   - Para mejorar la integración con Zenodo sin comprometer el entorno de producción, hemos desarrollado **Fakenodo**. Este es un microservicio independiente que simula las respuestas de la API de Zenodo para validar la publicación y asignación de DOIs en un entorno seguro.

6. **Despliegue Contenerizado con Docker:**
   - Se ha implementado la contenerización completa del sistema utilizando **Docker**. Esto asegura la portabilidad del proyecto, facilitando un despliegue estandarizado y reproducible de todos los servicios (aplicación principal y servicios auxiliares) tanto en entornos locales como en servidores de producción.

7. **Interfaz de Usuario y Navegación:**
   - Se han realizado mejoras generales en la interfaz para integrar estas nuevas herramientas, facilitando la navegación entre la vista de detalles del dataset, el carrito de compra y el panel de administración del usuario.

## Visión global del proceso de desarrollo

El proceso de desarrollo del sistema **PixelHub-2** se ha estructurado bajo los principios de la **Ingeniería de Software Moderna**, priorizando la reproducibilidad, la automatización y la calidad continua. Dado que el sistema integra gestión de datos complejos, interfaces web y comunicación con repositorios externos (Zenodo), el ciclo de vida del desarrollo (SDLC) se aleja de métodos rígidos para adoptar un enfoque ágil, apoyado firmemente en prácticas de **DevOps** y **Containerización**.

El flujo de trabajo diseñado no es una simple secuencia de pasos, sino un ecosistema integrado donde el código, la infraestructura y las pruebas conviven de manera sincronizada. A continuación, se detalla cómo se orquesta este proceso y las herramientas específicas que conforman el esqueleto tecnológico del proyecto.

### Los Pilares del Proceso: Infraestructura como Código y Virtualización

La base fundamental sobre la que se cimienta todo el proceso de desarrollo es la eliminación de la discrepancia entre entornos. En el desarrollo de software distribuido, el problema de "funciona en mi máquina" es un obstáculo crítico. Para mitigar esto, **PixelHub-2** ha adoptado una estrategia dual de virtualización y contenerización.

Por un lado, utilizamos **Docker** como estándar principal para la definición de servicios. El archivo `docker-compose.dev.yml` define la "verdad única" del entorno, levantando simultáneamente la aplicación web (Flask), la base de datos MariaDB y el servidor Nginx.

Por otro lado, hemos implementado **Vagrant** para gestionar entornos de desarrollo virtualizados completos. Esto nos permite desplegar una máquina virtual con una configuración de sistema operativo idéntica a la de producción, garantizando que las dependencias del sistema y las configuraciones de red sean consistentes para todos los desarrolladores, independientemente de su sistema operativo anfitrión.

Un componente distintivo de esta arquitectura es el servicio **Fakenodo**. Dado que PixelHub-2 interactúa con la API de Zenodo, depender de la API real para el desarrollo diario sería ineficiente. El equipo utiliza este microservicio simulado, dockerizado independientemente, permitiendo que el ciclo de desarrollo sea autosuficiente y desconectado.

### Estandarización y Gestión de la Configuración

El control de versiones se gestiona mediante **Git**, utilizando una estrategia de ramas (*Branching Strategy*) que protege la rama principal. La estandarización se refuerza mediante el uso de **Commitlint**.

El sistema impone una disciplina estricta en los mensajes de confirmación (commits) utilizando la especificación de *Conventional Commits* (ej. `feat:`, `fix:`, `chore:`). Esto facilita la trazabilidad semántica de la evolución del proyecto y permite la generación automática de registros de cambios. La configuración del entorno se gestiona a través de variables de entorno, asegurando que las credenciales sensibles nunca se filtren al repositorio.

### Automatización de Tareas (DX): Uso de Rosemary

Para optimizar la experiencia de desarrollo y reducir la carga cognitiva del equipo, el proyecto hace uso de la herramienta de línea de comandos (CLI) **Rosemary**.

Esta utilidad abstrae la complejidad de los comandos subyacentes de Docker, Flask y la base de datos. En lugar de ejecutar instrucciones manuales y propensas a errores, el equipo utiliza esta interfaz para tareas rutinarias como la inicialización y sembrado de la base de datos (`db:seed`), la ejecución de tests o la limpieza de cachés. Su integración en el flujo de trabajo acelera significativamente la incorporación de nuevos miembros y el mantenimiento diario.

### Estrategia de Aseguramiento de la Calidad (QA)

La calidad no es una fase final, sino una actividad continua integrada en el desarrollo. La arquitectura de pruebas es piramidal y exhaustiva:

* **Pruebas Unitarias:** Primera línea de defensa utilizando **Pytest**. Cada módulo (como `auth` o `dataset`) cuenta con su propia suite que valida la lógica de negocio aislada.
* **Pruebas de Integración y End-to-End (E2E):** Para validar la interacción de los componentes y la interfaz de usuario, se utiliza **Selenium WebDriver**. El sistema lanza navegadores *headless* dentro de contenedores Docker, simulando interacciones humanas reales.
* **Pruebas de Carga:** Antes de considerar un cambio listo para producción, verificamos su impacto en el rendimiento utilizando **Locust**, lo que permite detectar cuellos de botella bajo estrés.

### Integración Continua (CI) y Despliegue Continuo (CD)

El "pegamento" que une este proceso es **GitHub Actions**. El repositorio cuenta con flujos de trabajo robustos que automatizan la validación y entrega:

* **CI (Continuous Integration):** Cada subida de código dispara validaciones automáticas. Se verifica el estilo del código (Linting), se ejecutan las baterías de pruebas unitarias y se valida la semántica de los commits. Si algún paso falla, el cambio es rechazado automáticamente.
* **CD (Continuous Deployment):** Una vez que el código se fusiona en la rama principal (`trunk`), se activa el despliegue automático. Se construyen imágenes de Docker optimizadas para producción y se despliegan en la plataforma Render, actualizando la aplicación en vivo sin intervención manual.

### Ejemplo Ilustrativo: Ciclo de Vida de un Cambio

Para visualizar cómo encajan estas piezas, analizamos el ciclo de vida completo de una corrección real: **"Corrección del contenido del pie de página (Footer)"**.

**Escenario:** Se detectó que el pie de página mostraba una lista de universidades en lugar de los nombres del equipo de desarrollo, tal como se requería para la versión actual.

1. **Identificación y Asignación:** La Issue es reportada por Estrella Ángel Postigo (Autor/Asignante). Se documenta el comportamiento actual y el esperado. La tarea se asigna al desarrollador José Luis Moraza Vergara.
2. **Ramificación:** El desarrollador crea una rama específica para esta corrección, siguiendo la nomenclatura del proyecto, por ejemplo: `fix/footer-content-update`.
3. **Desarrollo Local:** José Luis modifica las plantillas del frontend (UI) para reemplazar "University of Seville..." por la lista de integrantes: "Estrella Ángel Postigo · Ismael Carrasco Mkhazni · Carlos Cerdá Morales...". Utiliza el entorno local levantado con Docker/Vagrant para verificar visualmente que el cambio se refleja correctamente en el navegador.
4. **Verificación y Commit:** Antes de subir el cambio, el desarrollador ejecuta los tests locales para asegurar que no ha roto la maquetación. Realiza un commit semántico describiendo la corrección: `fix(ui): update footer with dev team names`.
5. **Integración Continua:** Al subir la rama al repositorio, GitHub Actions ejecuta automáticamente los linters y pruebas.
6. **Revisión y Cierre:** Ismael Carrasco Mkhazni actúa como Revisor Técnico. Tras verificar el código y comprobar que cumple con los requisitos de la issue, Ismael procede a ejecutar las tareas finales de integración:
    * **Fusión (Merge):** Integra los cambios de la rama de trabajo de José Luis en la rama principal `trunk`.
    * **Cierre de Rama:** Elimina la rama `fix/footer-content-update` para mantener la limpieza del repositorio.
    * **Actualización de Estado:** Mueve la issue correspondiente a la columna Done (Hecho) en el tablero de gestión del proyecto.
7. **Despliegue Automático:** La fusión en `trunk` dispara el pipeline de despliegue (`CD_render.yml`). En cuestión de minutos, la nueva versión con los nombres correctos en el pie de página está disponible en producción para todos los usuarios.

## Entorno de desarrollo (800 palabras aproximadamente)
Debe explicar cuál es el entorno de desarrollo que ha usado, cuáles son las versiones usadas y qué pasos hay que seguir para instalar tanto su sistema como los subsistemas relacionados para hacer funcionar el sistema al completo. Si se han usado distintos entornos de desarrollo por parte de distintos miembros del grupo, también debe referenciarlo aquí.

A continuación, se detallan los requisitos, las herramientas seleccionadas y los pasos necesarios para desplegar el sistema completo.# Entorno de Desarrollo de UVLHub

### 1. Requisitos del Sistema y Stack Tecnológico

Para el correcto funcionamiento del sistema, se han establecido las siguientes versiones y herramientas base, las cuales son mandatorias para garantizar la compatibilidad del código:

- **Sistema Operativo Base:** Se utiliza **Ubuntu 22.04 LTS ** como el sistema de referencia para producción y para las máquinas virtuales de desarrollo.
- **Lenguaje de Programación:** El núcleo de la aplicación está construido sobre **Python 3.12**. Esta versión es estricta, tal como se especifica en la configuración del proyecto, para aprovechar las últimas mejoras de rendimiento y tipado del lenguaje.
- **Orquestación de Contenedores:** **Docker** y **Docker Compose** son las piezas centrales que permiten levantar la aplicación web junto con sus servicios satélites (bases de datos, simuladores de API, etc.) de manera aislada.
- **Virtualización (Opcional):** Para entornos que requieren una simulación completa de la infraestructura de red, se emplean **VirtualBox** y **Vagrant**.

### 2. Entorno de Desarrollo Integrado (IDE)

El equipo ha utilizado de **Visual Studio Code (VS Code)**

#### Configuración y Extensiones

Extensiones instaladas en VS Codes:

1. **Docker:** Permite gestionar contenedores, imágenes, volúmenes y redes de Docker directamente desde Visual Studio Code
2. **Python:** Proporciona soporte completo para el desarrollo en Python, incluyendo resaltado de sintaxis, autocompletado inteligente (IntelliSense), ejecución de scripts y gestión de entornos virtuales.
3. **Debugpy:** Habilita la depuración avanzada de aplicaciones Python, permitiendo establecer puntos de interrupción, inspeccionar variables y ejecutar el código paso a paso, tanto en entornos locales como dentro de contenedores.
4. **Python indent:** Mejora el manejo automático de la indentación en Python, evitando errores comunes relacionados con espacios y tabulaciones, especialmente en bloques de control y funciones.
5. **Flake8:** Integra el analizador estático Flake8 en el editor para detectar errores de sintaxis, problemas de estilo y posibles fallos lógicos, ayudando a mantener un código limpio y consistente.
6. **ESLint:** Proporciona análisis estático para código JavaScript, detectando errores, malas prácticas y problemas de estilo en tiempo real, especialmente útil en el desarrollo del frontend.
7. **PyPi Assistant:** Facilita la gestión de dependencias de Python, mostrando información sobre versiones disponibles, compatibilidad y posibles actualizaciones de los paquetes instalados desde PyPI.
8. **Flask Snippets:** Ofrece fragmentos de código predefinidos para aplicaciones Flask, acelerando el desarrollo al generar estructuras comunes como rutas, vistas y configuraciones básicas.

### 3. Gestión de Calidad, Estilo y Dependencias

Antes de realizar cualquier commit en el repositorio, es recomendable ejecutar localmente las herramientas de análisis y formateo de código del proyecto. En concreto, se debe ejecutar **flake8** para detectar errores de sintaxis y estilo, así como **black .** e **isort .** para aplicar automáticamente el formato y la ordenación de importaciones. Aunque el proyecto cuenta con hooks de pre-commit que ejecutan estas comprobaciones de forma automática y bloquean el commit en caso de incumplimiento, ejecutar estas herramientas manualmente previamente permite detectar y corregir problemas de manera anticipada.

Se aplican reglas estrictas mediante herramientas de análisis estático y formateo automático definidas en el archivo `pyproject.toml` y gestionadas por `pre-commit`.

- **Gestión de Dependencias:** Se utiliza un archivo `pyproject.toml`  para definir las dependencias del proyecto (`click`, `python-dotenv`) y las herramientas de desarrollo (`black`, `isort`, `flake8`, `autoflake`). También se mantiene un `requirements.txt` para compatibilidad.
- **Formato de Código (Black):** Se utiliza Black con una longitud de línea configurada a **120 caracteres**.
- **Pre-commit Hooks:** Antes de cada confirmación en Git, se ejecuta una serie de pruebas automatizadas:
  - **Ruff:** Configurado para corregir errores automáticamente (`--fix`).
  - **Check-added-large-files:** Impide subir archivos binarios mayores a 5MB (5120KB).
  - **Check-yaml / Check-json:** Valida la sintaxis de archivos de configuración.
  - **Commitlint:** Asegura que los mensajes de commit sigan la convención *Conventional Commits*.

### 4. Arquitectura de Subsistemas (Docker Compose)

El entorno de desarrollo local reproduce el funcionamiento del sistema en producción mediante el uso de varios servicios que se coordinan entre sí y que se configuran a través del archivo `docker-compose.dev.yml`:

1. **Web (Flask App):** Contenedor principal que monta el código fuente local (`../:/app`) como volumen y expone el servicio en el puerto **5000**.
2. **Database (MariaDB):** Base de datos relacional persistente en el puerto **3306**.
3. **Nginx:** Servidor web como proxy inverso en el puerto **80**.
5. **Fakenodo:** Simulador interno de la API de Zenodo que se ejecuta en el puerto **5001**, permitiendo pruebas sin depender del servicio real.

### 5. Guía de Instalación y Puesta en Marcha

#### Opción A: Despliegue con Docker

Para el despliegue del sistema en Docker seguiremos los siguientes pasos. Se estima que son necesarios entre **15-20 GB** de almacenamiento libre.

---

##### 1. Instalación de Docker y Docker Compose

Ejecutaremos la siguiente secuencia de comandos para instalar la versión oficial de Docker en **Ubuntu 22.04**:

```bash
# Actualizar repositorios e instalar dependencias
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl gnupg lsb-release

# Añadir la clave GPG oficial de Docker
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Configurar el repositorio de Docker
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker y Docker Compose
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Dar permisos a Docker para usarlo sin sudo
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

##### Comprobación de la instalación

Para verificar que Docker se ha instalado correctamente, ejecutamos:

```bash
docker version
```

Si el comando muestra información tanto del **Client** como del **Server**, la instalación ha sido correcta.

---

##### 2. Clonado del repositorio del proyecto

A continuación, instalamos **Git** y descargamos el código del proyecto:


```bash
sudo apt install -y git
git clone https://github.com/PixelHub-ORG/PixelHub-2.git
```
Creamos ahora el `.env` para que la aplicación funcione correctamente, estableciendo las siguientes variables de entorno:

```bash
FLASK_APP_NAME="PIXELHUB.IO(dev)"
FLASK_ENV=development
DOMAIN=localhost:5000
MARIADB_HOSTNAME=localhost
MARIADB_PORT=3306
MARIADB_DATABASE=pixelhubdb
MARIADB_TEST_DATABASE=pixelhubdb_test
MARIADB_USER=pixelhubdb_user
MARIADB_PASSWORD=pixelhubdb_password
MARIADB_ROOT_PASSWORD=pixelhubdb_root_password
WORKING_DIR=""
ORCID_CLIENT_ID="APP-QDXJOGWEQBPHZ3JR"
ORCID_CLIENT_SECRET="3d15b6fc-2d86-46e0-9522-dba049b5d477"
FAKENODO_URL="http://localhost:5001/api"
FAKENODO_BACKEND_URL="http://localhost:5001/api"
GITHUB_TOKEN="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"

```

---

##### 3. Ejecución de scripts de despliegue

Para facilitar el despliegue del sistema, se han creado dos scripts dentro de la carpeta `/scripts`.

#### 3.1. Levantar el entorno (`docker_up.sh`)

El script `docker_up.sh` realiza las siguientes acciones:

* Utiliza **MariaDB en local**.
* Inicia el archivo `docker-compose.dev.yml`.
* Despliega todos los contenedores necesarios para que el sistema funcione desde cero.

```bash
cd scripts
./docker_up.sh
```

> **Nota:** Si MariaDB no está instalada en el sistema, el script mostrará un error, pero **no afecta a la ejecución**, ya que el despliegue con Docker continuará funcionando correctamente.

---

##### 4. Acceso a los servicios

Una vez que los contenedores estén levantados:

##### Backend

Ejecutar el siguiente comando para acceder al contenedor del backend:

```bash
docker exec -it web_app_container bash
```

Una vez dentro del contenedor, ejecutar:

```bash
rosemary test
```

Para salir del contenedor:

```bash
exit
```

##### Frontend

Abrir un navegador web y acceder a para comprobar que PixelHub funciona:

```
http://localhost
```

Si queremos comprobar que el contenedor de fakenodo a funcionado correctamente abriremos en el navegador:
```
http://localhost:5001
```

---

##### 5. Detener y limpiar el entorno (`docker_down.sh`)

Para detener los contenedores, eliminarlos y volver a iniciar MariaDB en el sistema, ejecutar:

```bash
cd scripts
./docker_down.sh
```

Este script:

* Detiene los contenedores Docker.
* Elimina los contenedores creados.
* Vuelve a iniciar MariaDB en el sistema local.

---




#### Opción B: Vagrant

Esta guía detalla los pasos para desplegar el entorno utilizando Vagrant y VirtualBox (versión 7.0.16).

> **IMPORTANTE:** Asegúrese de que **Secure Boot** NO está activado en la BIOS de su sistema.

##### 1. Preparación del Sistema

Para evitar conflictos con KVM, es necesario añadir los módulos a la lista negra y reiniciar:

```bash
echo "blacklist kvm_intel" | sudo tee /etc/modprobe.d/blacklist-kvm.conf
echo "blacklist kvm_amd" | sudo tee -a /etc/modprobe.d/blacklist-kvm.conf
```

**Nota:** Es necesario **reiniciar el ordenador** después de ejecutar estos comandos.

##### 2. Instalación de Software

Instalaremos Vagrant, Ansible y VirtualBox. Asegúrese de utilizar VirtualBox 7.0.16 o compatible.

```bash
sudo apt update

# Añadir repositorio de HashiCorp para Vagrant
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Instalar paquetes
sudo apt update && sudo apt install vagrant ansible virtualbox
```

##### 3. Configuración del Proyecto

En el directorio raíz del proyecto (`PixelHub-2`), modificamos el archivo `.env`. Debemos cambiar la variable `WORKING_DIR` para que apunte al directorio de Vagrant:

```bash
# En el archivo .env cambiar WORKING_DIR="" por:
WORKING_DIR=/vagrant/
```
> **Nota:** El valor debe ser exactamente `/vagrant/`, sin comillas adicionales si no son necesarias por el formato.

##### 4. Despliegue y Ejecución

Accedemos a la carpeta `vagrant` y levantamos la máquina virtual:

```bash
cd vagrant
vagrant up
```

Una vez finalizado el proceso, la aplicación debería estar accesible en:
`http://localhost:5000`

##### 5. Solución de Problemas

Si ocurre algún error durante el despliegue (`vagrant up`), es necesario limpiar el entorno completamente antes de reintentar, ya que la máquina virtual puede quedar en un estado inconsistente.

```bash
vagrant halt
vagrant destroy -f
vagrant up
```

---


#### Opción C: Local


Esta guía detalla los pasos para instalar y poner en marcha **PixelHub2** en un entorno Ubuntu limpio.

---

##### 1. Instalación y configuración de MariaDB

Instalar MariaDB:

```bash
sudo apt install mariadb-server -y
sudo systemctl start mariadb
sudo mysql_secure_installation
```
Durante la configuración de `mysql_secure_installation` introducimos por consola las siguientes opciones:

- Enter current password for root (enter for none): (enter)
- Switch to unix_socket authentication [Y/n]: `y`
- Change the root password? [Y/n]: `y`
    - New password: `pixelhubdb_root_password`
    - Re-enter new password: `pixelhubdb_root_password`
- Remove anonymous users? [Y/n]: `y`
- Disallow root login remotely? [Y/n]: `y` 
- Remove test database and access to it? [Y/n]: `y`
- Reload privilege tables now? [Y/n] : `y`

Creamos la base de datos y el usuario `root` para la aplicación:

```bash

sudo mysql -u root -p
# Introducir: pixelhubdb_root_password
```
En la consola de mariadb introducimos los siguientes comandos y pulsamos enter:
```bash
CREATE DATABASE pixelhubdb;
CREATE DATABASE pixelhubdb_test;

CREATE USER 'pixelhubdb_user'@'localhost' IDENTIFIED BY 'pixelhubdb_password';
GRANT ALL PRIVILEGES ON pixelhubdb.* TO 'pixelhubdb_user'@'localhost';
GRANT ALL PRIVILEGES ON pixelhubdb_test.* TO 'pixelhubdb_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
##### 2. Crear el archivo de variables de entorno `.env`
Creamos ahora el `.env` para que la aplicación funcione correctamente, estableciendo las siguientes variables de entorno:

```bash
FLASK_APP_NAME="PIXELHUB.IO(dev)"
FLASK_ENV=development
DOMAIN=localhost:5000
MARIADB_HOSTNAME=localhost
MARIADB_PORT=3306
MARIADB_DATABASE=pixelhubdb
MARIADB_TEST_DATABASE=pixelhubdb_test
MARIADB_USER=pixelhubdb_user
MARIADB_PASSWORD=pixelhubdb_password
MARIADB_ROOT_PASSWORD=pixelhubdb_root_password
WORKING_DIR=""
ORCID_CLIENT_ID="APP-QDXJOGWEQBPHZ3JR"
ORCID_CLIENT_SECRET="3d15b6fc-2d86-46e0-9522-dba049b5d477"
FAKENODO_URL="http://localhost:5001/api"
FAKENODO_BACKEND_URL="http://localhost:5001/api"
GITHUB_TOKEN="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"
```

Crear el archivo `.moduleignore`:

```bash 
echo "webhook" > .moduleignore
```

##### 3. Instalación de Python3.12
Ejecutamos:
```bash 
sudo apt install python3.12-venv -y
```
Si nos devuelve un error:
```bash 
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12 python3.12-venv -y
```
Creamos y activamos el entorno virtual:
```bash
python3.12 -m venv venv
source venv/bin/activate
```

Instalamos las dependencias:
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e ./

```

Verificamos si rosemary se ha instalado ejecutando:
```bash
rosemary
```

##### 5. Aplicar las migraciones
Ejecutamos la actualización de las migraciones y la población de la base de datos:

```bash
flask db upgrade
rosemary db:seed

```

##### 6. Arrancar la aplicación
Aplicación principal:
```bash
flask run --port 5000 --host=0.0.0.0 --reload --debug

```

Fakenodo (en otra terminal con el entorno de python activado):
```bash
cd fakenodo
flask run --port 5001

```






## Ejercicio de propuesta de cambio

Para ilustrar el proceso de evolución y gestión de la configuración del proyecto **PixelHub-2**, se presenta a continuación un caso práctico real. Este ejercicio describe el ciclo de vida completo de una modificación en el sistema, desde su reporte como incidencia hasta su despliegue en producción, detallando los comandos y herramientas utilizados en cada etapa.

### Definición del Cambio (Issue #45)

El cambio se origina a partir de un reporte de error en la interfaz de usuario. Se ha documentado la incidencia en el sistema de seguimiento (GitHub Issues) con la siguiente información:

* **Título:** Corrección del contenido del pie de página (Footer).
* **Tipo:** `Bug` / `Content`
* **Descripción del error:** El contenido del pie de página es incorrecto. Actualmente muestra una lista genérica de universidades ("University of Seville · University of Malaga · University of Ulm") en lugar de los nombres de los integrantes del equipo de desarrollo, tal como se requiere para la versión actual.
* **Pasos para reproducir:**
    1.  Entrar en la página principal de la aplicación.
    2.  Hacer *scroll* hasta el final de la página.
    3.  Observar el texto actual en el *footer*.
* **Comportamiento esperado:** El pie de página debe mostrar: `PIXELHUB.IO(dev) Estrella Ángel Postigo · Ismael Carrasco Mkhazni · Carlos Cerdá Morales · Loubna Founoun El Aoud · José Luis Moraza Vergara · Diego Terrón Hernández`.

#### Asignación de Roles
Para este ejercicio, el flujo de trabajo involucra a los siguientes miembros:
* **Autor/Asignante:** Estrella Ángel Postigo.
* **Desarrollador:** José Luis Moraza Vergara.
* **Revisor Técnico:** Ismael Carrasco Mkhazni.

### Ciclo de Ejecución Paso a Paso

A continuación, se detalla el procedimiento técnico seguido para resolver la incidencia.

#### Paso 1: Gestión de la Configuración (Inicio)

El desarrollador (**José Luis**) comienza sincronizando su repositorio local con la rama principal para asegurar que trabaja sobre la última versión estable. Posteriormente, crea una rama de funcionalidad específica para aislar el cambio.

```bash

git checkout trunk
git pull origin trunk

git checkout -b fix/footer-names-45
````

#### Paso 2: Implementación (Desarrollo)

El desarrollador localiza el archivo responsable de la estructura base de la interfaz: `app/templates/base_template.html`. Utilizando **Visual Studio Code**, procede a modificar el bloque HTML correspondiente al pie de página.

**Código Modificado (Diff):**

```html
<div class="col-sm-6 text-end">
    University of Seville · University of Malaga · University of Ulm
</div>
------------------------------------------------------------
<div class="col-sm-6 text-end">
    Estrella Ángel Postigo · Ismael Carrasco Mkhazni · Carlos Cerdá Morales · Loubna Founoun El Aoud · José Luis Moraza Vergara · Diego Terrón Hernández
</div>
```

#### Paso 3: Aseguramiento de la Calidad (QA Local)

Antes de confirmar los cambios, es imperativo verificar que la modificación no ha introducido errores de sintaxis o regresiones en la interfaz. El desarrollador utiliza el entorno local (desplegado previamente con Docker o Vagrant) para validar visualmente el cambio y ejecuta las pruebas automáticas.

```bash
# 1. Validación visual: Acceder a http://localhost:5000 y verificar el footer.

# 2. Ejecución de tests unitarios y de integración para evitar regresiones
rosemary test
```

#### Paso 4: Confirmación y Envío (Git)

Una vez validado el cambio, se procede a registrarlo en el control de versiones. Se utiliza **Commitlint** para asegurar que el mensaje del commit cumpla con el estándar semántico del proyecto.

```bash

git add app/templates/base_template.html

git commit -m "fix: update footer content with team member names (Issue #45)"

git push origin fix/footer-names-45
```

#### Paso 5: Integración Continua (CI)

Al detectar la subida de la nueva rama (`push`), la plataforma **GitHub Actions** dispara automáticamente los flujos de trabajo de Integración Continua definidos en `.github/workflows/`.

  * **Linting:** Se verifica que el código HTML/Jinja2 cumple con las reglas de estilo.
  * **Testing:** Se ejecuta la batería de pruebas en un entorno aislado en la nube.

Si alguna de estas verificaciones falla, el sistema notifica al desarrollador para que corrija el error antes de continuar.

#### Paso 6: Revisión y Cierre (Gestión)

Una vez que el CI ha marcado la rama como válida (check verde), interviene el **Revisor Técnico (Ismael)**.

1.  **Code Review:** Ismael revisa el código en GitHub para asegurar que el cambio cumple estrictamente con lo solicitado en la *issue* y no incluye código innecesario.
2.  **Fusión (Merge):** Tras aprobar el cambio, Ismael procede a integrar la rama de corrección en la rama principal.
    ```bash
    git checkout trunk
    git pull origin trunk
    git merge fix/footer-names-45
    git push origin trunk
    ```
3.  **Cierre:** Se elimina la rama `fix/footer-names-45` (tanto local como remota) para mantener la limpieza del repositorio y se mueve la *Issue \#45* a la columna **Done**.

#### Paso 7: Despliegue Continuo (CD)

La actualización de la rama `trunk` activa automáticamente el flujo de despliegue (`CD_render.yml`). El sistema construye una nueva imagen Docker con los cambios y la despliega en **Render**. En cuestión de minutos, el nuevo pie de página con los nombres del equipo es visible para todos los usuarios en el entorno de producción.

## Conclusiones y trabajo futuro
El desarrollo del proyecto PixelHub2 nos ha permitido conocer en más profundidad como funcionan los flujos de trabajos basados en integración y despliegue continuos, implementando desde cero pipelines que nos han permitido ahorrar tiempo de desarrollo, despliegue y depuración.

El hecho de integrarnos con el grupo de trabajo `PixelHub1`, ha supuesto un gran desafío de coordinación.Elaborar una buena metodología para poder sincronizar el código y configuraciones externas de ambos proyectos ha sido un factor clave para poder garantizar la estabilidad del sistema, permitiendo a ambos equipos colaborar sin apenas conflictos.

La elaboración de estándares para los formatos `issues`, `ramas` y `commits` ha sido un aspecto fundamental del proyecto, ya que ha permitido una organización más eficiente del trabajo, una comunicación más clara entre los miembros del equipo y una trazabilidad precisa de los cambios realizados. Estos estándares no solo facilitan la colaboración interna, sino que también garantizan que la evolución del código sea coherente y predecible, contribuyendo directamente a la calidad y mantenibilidad del proyecto a largo plazo.

Además, el proyecto nos ha brindado la oportunidad de aplicar buenas prácticas de ingeniería de software nunca antes vistas en la carrera de Ingeniería del Software, como la contenerización con Docker, la gestión de entornos reproducibles y la automatización de pruebas, lo que ha incrementado la calidad del software entregado.

De cara al futuro, se identifican varias áreas de mejora que podrían optimizar aún más la plataforma y la dinámica del equipo:

Optimización de la interfaz del carrito de compra: La experiencia de usuario en el módulo del carrito podría ser más intuitiva y visualmente clara, facilitando la selección, visualización y descarga de los modelo. Mejorar esta interfaz contribuirá a una interacción más ágil y satisfactoria para los usuarios.

Fortalecer la comunicación del equipo: Durante el desarrollo, en algunas ocasiones se han producido errores o confusiones derivadas de una comunicación insuficiente entre los miembros del equipo. Una Una comunicación  más eficiente permitirá reducir malentendidos y aumentar la productividad colectiva.

Implementación de pruebas automatizadas con Selenium para Docker: Actualmente, la ejecución de pruebas podría ampliarse integrando Selenium dentro de los contenedores Docker, lo que permitiría validar la aplicación de manera consistente en entornos contenerizados y garantizar que los cambios no introduzcan errores en la interfaz o la funcionalidad.

## Declaración de IA

Durante el desarrollo del proyecto PixelHub2, se ha utilizado la Inteligencia Artificial como una herramienta de apoyo complementaria, con el objetivo de mejorar la eficiencia y la calidad del trabajo realizado. Concretamente, la IA ha sido empleada para:

- **Comprobación y corrección de errores:** Se ha utilizado como asistente para identificar inconsistencias o posibles errores en fragmentos de código, sugiriendo correcciones o mejoras, siempre bajo la supervisión y validación del equipo.

- **Apoyo en implementaciones específicas:** En algunos casos, la IA ha servido como guía o referencia para implementar funciones y módulos, acelerando el proceso de desarrollo y ofreciendo alternativas técnicas que luego han sido revisadas y adaptadas por los desarrolladores.

- **Mejora de la expresión en documentos y reportes:** Se ha usado para revisar secciones de la documentación del proyecto, optimizando la claridad, coherencia y formalidad del lenguaje sin sustituir el juicio del equipo.

En todo momento, la IA ha sido una herramienta auxiliar y no ha sustituido la toma de decisiones ni el trabajo técnico del equipo. Todas las propuestas generadas por la IA han sido revisadas, validadas y adaptadas por los miembros del proyecto antes de su integración en el sistema o en la documentación.
