# TODO: 
- Hablar del cambio propuesto en Visión global del proceso de desarrollo. (ISMAEL)
- Revisar todo lo escrito en ese punto, hay cosas que no tienen mucho sentido como hablar de Rosemary que no lo hemos implementado nosotros. (no lo veo del todo mal hablar un poco de rosemary) (ISMAEL)
- Guía de instalación HECHO, falta vagrant
- Ejercicio de propuesta de cambio
- Cambiar la visión global, se nota demasiado que es IA  (ISMAEL)
- Rellenar las horas, una vez que esté completo el Clockify, y adjuntar el report

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
[Ángel Postigo, Estrella del Carmen](https://github.com/nombredeusuariodegithub) | HH | 12 | 987 | 17 | 4 | Build my own dataset | M |
[Carrasco Mkhazni, Ismael](https://github.com/nombredeusuariodegithub) | HH | 8 | 468 | 3 | 6 | Download own dataset | M |
[Cerdá Morales, Carlos](https://github.com/nombredeusuariodegithub) | HH | 64 | 16.632 | 47 | 9 | Differences between versions | H |
[Founoun El Aoud, Loubna](https://github.com/nombredeusuariodegithub) | HH | 48 | 1.163| 4 | 5 | View user profile | L |
[Moraza Vergara, José Luis](https://github.com/nombredeusuariodegithub) | HH | 23 | 2.930 | 57 | 9 | Upload from Github/Zip | H |
[Terrón Hernández, Diego](https://github.com/nombredeusuariodegithub) | HH | 10 | 698 | 4 | 3 | Auth with ORCID | L |
**TOTAL** | HH | 165  | 22878 | 132 | 36 |  | H(2)/M(2)/L(2) |

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

## Visión global del proceso de desarrollo (1.500 palabras aproximadamente)

Debe dar una visión general del proceso que ha seguido enlazándolo con las herramientas que ha utilizado. Ponga un ejemplo de un cambio que se proponga al sistema y cómo abordaría todo el ciclo hasta tener ese cambio en producción. Los detalles de cómo hacer el cambio vendrán en el apartado correspondiente.

### ***TODO LO SIGUIENTE, HASTA ENTORNO DE DESARROLLO ES UN BORRADOR, HAY QUE QUITAR COSAS MUY GENERALES COMO ROSEMARY***

(hecho por Ismael)

El proceso de desarrollo del sistema **PixelHub-2** ha sido diseñado bajo una filosofía de **Ingeniería de Software Moderna**, priorizando la reproducibilidad, la automatización y la calidad continua. Al tratarse de un sistema complejo que integra gestión de datos, interfaces web y comunicación con repositorios externos (Zenodo), el ciclo de vida del desarrollo (SDLC) se aleja de los métodos tradicionales en cascada para adoptar un enfoque ágil apoyado fuertemente en prácticas de **DevOps** y **Containerización**.

El flujo de trabajo no es simplemente una secuencia de pasos, sino un ecosistema integrado donde el código, la infraestructura y las pruebas conviven de manera sincronizada. A continuación, se detalla cómo se orquesta este proceso, vinculándolo con las herramientas específicas que conforman el esqueleto tecnológico del proyecto.

#### 1. Los Pilares del Proceso: Infraestructura como Código y Contenerización

La base fundamental sobre la que se cimienta todo el proceso de desarrollo es la eliminación de la discrepancia entre entornos. En el desarrollo de software distribuido, el problema de "funciona en mi máquina" es un obstáculo crítico. Para mitigar esto, PixelHub-2 ha adoptado **Docker** como estándar absoluto para la definición del entorno.

El proceso de desarrollo comienza con la orquestación de servicios definida en los archivos `docker-compose`. El equipo no instala dependencias como bases de datos o servidores web directamente en sus sistemas operativos anfitriones. En su lugar, el archivo `docker/docker-compose.dev.yml` define la "verdad única" del entorno de desarrollo. Este archivo levanta simultáneamente:

* **La aplicación web (Flask):** En un contenedor dedicado.
* **Base de datos MariaDB:** Garantizando que todos usen la misma versión y configuración, ejecutánose al inicio todos los comandos necesarios para garantizar que se obtenga la última versión de las migraciones y los seeders correspondiente.
* **Servidor Nginx:** Actúa como proxy inverso incluso en desarrollo, replicando la arquitectura de producción.

Un componente distintivo de esta arquitectura es el servicio **Fakenodo**. Dado que PixelHub-2 interactúa con la API de Zenodo, depender de la API real para el desarrollo diario sería lento, propenso a errores y "ensuciaría" el entorno de producción de Zenodo. El equipo desarrolló un microservicio simulado, ubicado en la carpeta `fakenodo/` y dockerizado con su propio contenedor independiente. Esto permite que el ciclo de desarrollo sea autosuficiente y desconectado, una característica vital para la velocidad del proceso.

#### 2. Estandarización y Gestión de la Configuración

El control de versiones se gestiona mediante **Git**, utilizando una estrategia de ramas (*Branching Strategy*) que protege la rama principal. Sin embargo, el proceso va un paso más allá en la estandarización mediante el uso de **Commitlint**.

Analizando el archivo `commitlint.config.js` y el flujo de trabajo `CI_commits.yml`, se evidencia que el sistema impone una disciplina estricta en los mensajes de confirmación (commits). Se utiliza la especificación de *Conventional Commits* (ej. `feat:`, `fix:`, `chore:`). Esto no es meramente estético; es una decisión procesal que permite la generación automática de registros de cambios (changelogs) y facilita la trazabilidad semántica de la evolución del proyecto.

La configuración del entorno se gestiona a través de variables de entorno, con plantillas claras como `.env.local.example` y `.env.docker.example`, lo que asegura que las credenciales y configuraciones sensibles nunca se filtren al repositorio, siguiendo las mejores prácticas de seguridad (The Twelve-Factor App).

#### 3. Automatización de la Experiencia de Desarrollo (DX): "Rosemary"

Uno de los aspectos más innovadores del proceso de desarrollo de este sistema es la creación de una herramienta de línea de comandos (CLI) personalizada llamada **Rosemary**.

En lugar de obligar a los desarrolladores a memorizar complejos comandos de Docker, Flask o Alembic, el equipo ha encapsulado la lógica operativa del proyecto en scripts de Python ubicados en el directorio `rosemary/`. Esta herramienta actúa como un orquestador de tareas de desarrollo:

* **Gestión de Datos:** Si un desarrollador necesita reiniciar la base de datos y poblarla con datos de prueba, ejecuta `rosemary db:reset` y `rosemary db:seed`.
* **Scaffolding:** Para crear un nuevo módulo, el comando `rosemary make:module` genera automáticamente toda la estructura de carpetas (modelos, rutas, servicios, tests) utilizando plantillas Jinja2, garantizando que todo el código nuevo siga la arquitectura modular predefinida.
* **Testing:** Para ejecutar pruebas, `rosemary test` o `rosemary selenium` simplifican la invocación de los contenedores de prueba.

Esta herramienta reduce la carga cognitiva del equipo y acelera significativamente la incorporación de nuevos miembros y el desarrollo diario.

#### 4. Estrategia de Aseguramiento de la Calidad (QA)

El proceso de desarrollo integra la calidad no como una fase final, sino como una actividad continua. La arquitectura de pruebas es piramidal y exhaustiva:

1.  **Pruebas Unitarias:** Son la primera línea de defensa. Utilizando **Pytest**, cada módulo (por ejemplo, `auth`, `dataset`, `cart`) tiene su propia suite de pruebas unitarias (`test_unit.py`). Estas validan la lógica de negocio aislada, asegurando que las funciones individuales se comporten correctamente.
2.  **Pruebas de Integración y End-to-End (E2E):** Para validar que los componentes funcionan juntos y que la interfaz de usuario responde adecuadamente, se utiliza **Selenium WebDriver**. El sistema está configurado para lanzar navegadores *headless* (sin interfaz gráfica) dentro de contenedores Docker, simulando interacciones humanas reales (clics, envíos de formularios, navegación).
3.  **Pruebas de Carga y Rendimiento:** Antes de considerar que un cambio está listo para producción, se verifica su impacto en el rendimiento utilizando **Locust**. Los archivos `locustfile.py` definen escenarios de usuarios concurrentes, permitiendo al equipo detectar cuellos de botella bajo estrés.

Además, se aplica un análisis estático de código (Linting) mediante `flake8` y otras herramientas configuradas en `rosemary/commands/linter.py`, asegurando que el código cumpla con los estándares de estilo PEP8.

#### 5. Integración Continua (CI) y Despliegue Continuo (CD)

El "pegamento" que une todo este proceso es **GitHub Actions**. El repositorio contiene una carpeta `.github/workflows` robusta que automatiza la validación y entrega del software.

### Integración Continua (CI)
Cada vez que un desarrollador sube código (*push*) o abre una solicitud de cambio (*Pull Request*), se disparan flujos de trabajo automáticos:
* `CI_lint.yml`: Verifica el estilo del código.
* `CI_pytest.yml`: Ejecuta toda la batería de pruebas unitarias.
* `CI_coverage.yml`: Asegura que el porcentaje de código cubierto por pruebas no disminuya.
* `CI_commits.yml`: Valida la semántica de los mensajes de commit.

Si alguno de estos pasos falla, el cambio es rechazado automáticamente, impidiendo que código defectuoso llegue a la rama principal.

### Despliegue Continuo (CD)
Una vez que el código se fusiona en la rama principal (`trunk` o `main`), el proceso de despliegue se activa:
* `CD_dockerhub.yml`: Construye las imágenes de Docker optimizadas para producción (`Dockerfile.prod`) y las sube al registro de contenedores Docker Hub.
* `CD_render.yml`: Gestiona el despliegue automático en la plataforma Render, actualizando la aplicación en vivo sin intervención humana.

#### Ejemplo Ilustrativo: Ciclo de Vida de un Cambio

Para visualizar cómo todas estas piezas encajan en la práctica, analicemos el ciclo de vida completo de una propuesta de cambio concreta: **"Implementar la descarga del contenido del carrito en formato ZIP"**.

1.  **Concepción y Ramificación:**
    El desarrollador comienza actualizando su repositorio local y creando una nueva rama de funcionalidad siguiendo la convención:
    `git checkout -b feature/download-cart-zip`.

2.  **Desarrollo Local Asistido:**
    El desarrollador levanta el entorno con `rosemary compose-env up` (que invoca a `docker compose up`). Utiliza `rosemary make:module cart` si el módulo no existiera, o edita directamente `app/modules/cart/routes.py` para añadir la lógica de compresión ZIP utilizando la librería `zipfile` de Python. Modifica la plantilla `view_cart.html` para añadir el botón de descarga.

3.  **Verificación Local (Feedback Loop Rápido):**
    Antes de subir nada, el desarrollador ejecuta:
    * `rosemary linter`: Para corregir errores de estilo automáticamente.
    * `rosemary test cart`: Para ejecutar los tests unitarios solo del módulo afectado.
    * Crea un nuevo test E2E en `app/modules/cart/tests/test_selenium.py` que simula a un usuario añadiendo ítems y pulsando el botón de descarga, verificando que no hay errores 500. Ejecuta este test localmente contra el contenedor de Selenium.

4.  **Confirmación (Commit):**
    El desarrollador realiza el commit. Si intenta poner un mensaje vago como "fixed zip", el *hook* de `commitlint` local o el CI fallarán. Debe usar un mensaje semántico:
    `git commit -m "feat(cart): add bulk download functionality via zip"`

5.  **Integración Continua (The Guardian):**
    Al hacer `git push`, GitHub Actions despierta.
    * El workflow `CI_lint` escanea los archivos modificados.
    * El workflow `CI_pytest` levanta un entorno efímero en la nube y ejecuta todos los tests del sistema para asegurar que la compresión ZIP no rompió, por ejemplo, la sincronización con Zenodo (test de regresión).

6.  **Revisión y Fusión:**
    Un compañero revisa el código (Code Review). Al aprobarse, se realiza el *Merge* a la rama `trunk`.

7.  **Despliegue Automático:**
    El merge en `trunk` dispara el workflow `CD_dockerhub`. Este construye una nueva imagen Docker usando `Dockerfile.prod`, la cual es mucho más ligera y segura que la de desarrollo (sin herramientas de debug). Finalmente, Render detecta la nueva imagen y actualiza el servidor de producción.

En cuestión de minutos, y habiendo pasado por múltiples filtros de calidad automáticos, la funcionalidad está disponible para los usuarios finales. Este ciclo demuestra cómo PixelHub-2 utiliza herramientas modernas para convertir el desarrollo de software en un proceso industrializado, predecible y de alta calidad.

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

#### 1. Instalación de Docker y Docker Compose

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

#### 2. Clonado del repositorio del proyecto

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

#### 3. Ejecución de scripts de despliegue

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

#### 4. Acceso a los servicios

Una vez que los contenedores estén levantados:

#### Backend

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

#### Frontend

Abrir un navegador web y acceder a para comprobar que PixelHub funciona:

```
http://localhost
```

Si queremos comprobar que el contenedor de fakenodo a funcionado correctamente abriremos en el navegador:
```
http://localhost:5001
```

---

### 5. Detener y limpiar el entorno (`docker_down.sh`)

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

#### Opción D: Local


Esta guía detalla los pasos para instalar y poner en marcha **PixelHub2** en un entorno Ubuntu limpio.

---

### 1. Instalación y configuración de MariaDB

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
#### 2. Crear el archivo de variables de entorno `.env`
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

### 3. Instalación de Python3.12
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

#### 5. Aplicar las migraciones
Ejecutamos la actualización de las migraciones y la población de la base de datos:

```bash
flask db upgrade
rosemary db:seed

```

#### 6. Arrancar la aplicación
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
Se presentará un ejercicio con una propuesta concreta de cambio en la que a partir de un cambio que se requiera, se expliquen paso por paso (incluyendo comandos y uso de herramientas) lo que hay que hacer para realizar dicho cambio. Debe ser un ejercicio ilustrativo de todo el proceso de evolución y gestión de la configuración del proyecto. 

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
