# Evaluación Parcial N° 2: Desarrollo de Pruebas Unitarias y Análisis de Seguridad II

| Asignatura | Sigla | Ponderación | Semestre |
| :--- | :--- | :--- | :--- |
| **Ciclo de Vida del Software I** | AUY1102 | 40% | 2026-2 |

---

## 👥 Datos del Grupo de Trabajo (Grupo 5)

* **Organización de GitHub:** [https://github.com/CVDS-Grupo5](https://github.com/CVDS-Grupo5)
* **Repositorio del Proyecto:** [https://github.com/CVDS-Grupo5/AUY1102-Pipeline](https://github.com/CVDS-Grupo5/AUY1102-Pipeline)
* **Repositorio Base Original:** [https://github.com/Fundacion-Instituto-Profesional-Duoc-UC/AUY1102-Pipeline](https://github.com/Fundacion-Instituto-Profesional-Duoc-UC/AUY1102-Pipeline)

### Distribución de Responsabilidades y Roles

| Integrante | Usuario / ID GitHub | Rol Asignado | Responsabilidades Principales |
| :--- | :--- | :--- | :--- |
| **Christian Reyes** | `ChRiStIaNo0O` | **Líder QA y Calidad** | • Fork y configuración inicial del repositorio.<br>• Creación del script ejecutor de pruebas unitarias (`scripts/analisis-pruebas.js`).<br>• Obtención de métricas de cobertura y detección de pruebas fallidas.<br>• Integración y configuración de **SonarCloud** (`sonar-project.properties`).<br>• Desarrollo teórico del indicador IE3.1.1. |
| **Danilo Romero G.** | `DMROMEROG` | **Líder SecOps y Seguridad** | • Integración del repositorio en la consola web de **Snyk**.<br>• Configuración y análisis de vulnerabilidades con **npm audit**.<br>• Verificación de **GitHub Advanced Security** (Secret Scanning y Dependabot).<br>• **Remediación** de código vulnerable y actualización de dependencias (`chokidar`).<br>• Desarrollo teórico del indicador IE3.2.1. |

---

## 1. Fundamentación Teórica

### 1.1 Indicador IE3.1.1: Conceptos Clave de Calidad de Software (por Christian Reyes - `ChRiStIaNo0O`)

El aseguramiento de la calidad del software (QA) abarca múltiples técnicas que garantizan que el producto cumpla los requerimientos funcionales y técnicos con la menor deuda técnica posible:

* **Pruebas Unitarias (Unit Testing):** Verificación aislada del comportamiento de las unidades mínimas de código (funciones, clases, métodos). Garantizan que ante entradas conocidas se obtengan salidas predecibles, aislando dependencias mediante simulaciones (*mocks* o *stubs*).
* **Calidad de Código Estático vs. Dinámico:**
  * *Estático (SAST / Linters):* Se analiza el código fuente sin ejecutarlo. Permite detectar errores de sintaxis, incumplimiento de estándares, malas prácticas de tipado y fallas de seguridad tempranas.
  * *Dinámico (DAST / Testing en ejecución):* Se evalúa la aplicación en tiempo de ejecución para analizar rendimiento, manejo de memoria y respuesta ante datos imprevistos.
* **Análisis de Seguridad y Vulnerabilidades:** Identificación de patrones inseguros (como inyecciones SQL o Cross-Site Scripting) y detección de componentes obsoletos con fallos conocidos (SCA - *Software Composition Analysis*).
* **Pruebas Integradas (Integration Testing):** Validan la correcta interoperabilidad y comunicación entre diferentes módulos, componentes y servicios externos (APIs, bases de datos).
* **Pruebas de Estrés (Stress Testing):** Someten al sistema a cargas extremas por encima de los límites normales operativos para evaluar su estabilidad, umbrales de fallo y comportamiento bajo degradación controlada.
* **Pruebas de Regresión (Regression Testing):** Re-ejecución de baterías de pruebas existentes cada vez que se introduce un cambio, refactorización o corrección, garantizando que nuevas modificaciones no rompan funcionalidades preexistentes.

---

### 1.2 Indicador IE3.2.1: Métodos y Herramientas en el Ciclo de Vida del Software (por Danilo Romero G. - `DMROMEROG`)

La adopción de herramientas automatizadas dentro del ciclo de vida del desarrollo de software (SDLC) impulsa el principio de **Shift-Left Testing & Security**, el cual traslada la detección de defectos hacia las etapas más tempranas del desarrollo:

* **SonarCloud:** Plataforma SaaS líder para la inspección continua de código estático (SAST). Evalúa la calidad global a través del *Quality Gate*, clasificando los hallazgos en *Bugs* (fallos de fiabilidad), *Vulnerabilities* (seguridad), *Security Hotspots* (código sensible que requiere revisión) y *Code Smells* (mantenibilidad y deuda técnica).
* **Snyk:** Solución integral de seguridad orientada a desarrolladores. Permite analizar el árbol completo de dependencias directas e indirectas (SCA), alertando sobre CVEs conocidos con su correspondiente calificación de severidad (*Critical, High, Medium, Low*) y proveyendo recomendaciones automatizadas de remediación.
* **npm audit:** Utilidad nativa de Node.js que compara el árbol de dependencias instalado en `package-lock.json` contra la base de datos de avisos de seguridad de npm (GitHub Advisory Database), permitiendo auditorías rápidas en la terminal y en pipelines CI/CD.
* **GitHub Advanced Security (GHAS):** Suite de seguridad nativa de GitHub que incluye *Secret Scanning* (detección de tokens o credenciales expuestas en commits) y alertas de *Dependabot* con actualizaciones de seguridad automáticas (*Automated Security Updates*).
* **Impacto en la Mejora Continua:** Corregir un error en la etapa de desarrollo local o revisión de Pull Request resulta entre 10 y 30 veces más económico y seguro que detectarlo en producción, garantizando entregas continuas estables.

---

## 2. Parte 1: Análisis de Código mediante Pruebas Unitarias

> **Responsable:** Christian Reyes (`ChRiStIaNo0O`)

### 2.1 Creación del Fork y Repositorio del Grupo
Se realizó el Fork del repositorio oficial [`AUY1102-Pipeline`](https://github.com/Fundacion-Instituto-Profesional-Duoc-UC/AUY1102-Pipeline) hacia la organización del grupo, quedando disponible en:
* URL: `https://github.com/CVDS-Grupo5/AUY1102-Pipeline`
* Estado: Público (lo que permite habilitar SonarCloud y GitHub Advanced Security sin costo).

### 2.2 Creación del Script Automatizado de Pruebas
Para dar cumplimiento exacto al requerimiento de construir un script que ejecute las pruebas unitarias existentes, calcule el porcentaje de cobertura y muestre por pantalla las pruebas fallidas y las partes de código no cubiertas, se desarrolló el script en Node.js [`scripts/analisis-pruebas.js`](file:///C:/Users/chris/.gemini/antigravity/scratch/AUY1102-Pipeline/scripts/analisis-pruebas.js) y se configuró el comando directo en `package.json`:

```bash
npm run test:analisis
```

### 2.3 Ejecución y Resultados Obtenidos

Al ejecutar el script de análisis, se obtuvo el siguiente reporte por consola:

```text
================================================================================
       EVALUACIÓN PARCIAL N° 2 - ANÁLISIS DE PRUEBAS UNITARIAS Y COBERTURA       
                    Ciclo de Vida del Software I (AUY1102)                      
================================================================================
 Integrante 1 (QA / Pruebas): Christian Reyes       [ID: ChRiStIaNo0O]
 Integrante 2 (SecOps / Fix): Danilo Romero G.      [ID: DMROMEROG]
 Repositorio: https://github.com/CVDS-Grupo5/AUY1102-Pipeline
 Fecha y hora de ejecución: 02-11-2026, 8:02:17 p. m.
================================================================================

--------------------------------------------------------------------------------
 1. RESUMEN DE EJECUCIÓN DE PRUEBAS UNITARIAS
--------------------------------------------------------------------------------
 Suites de prueba totales: 10
   - Aprobadas:            10
   - Fallidas:             0
 Pruebas unitarias totales: 18
   - Aprobadas:            18
   - Fallidas:             0
 Tiempo total de prueba:   8.46 s

--------------------------------------------------------------------------------
 2. DETALLE DE PRUEBAS QUE FALLAN
--------------------------------------------------------------------------------
  ✔ En esta ejecución actual, todas las suites de prueba pasaron exitosamente.
    (Nota: Se detectó advertencia de llamadas asíncronas no capturadas hacia api.example.com en src/index.ts).

--------------------------------------------------------------------------------
 3. PORCENTAJE DE COBERTURA DE LOS COMPONENTES ANALIZADOS
--------------------------------------------------------------------------------
 COBERTURA GLOBAL DEL PROYECTO:
   - Líneas de código cubiertas:    43.28% (29/67)
   - Sentencias (Statements):       43.28% (29/67)
   - Funciones/Métodos:             56.66% (17/30)
   - Ramas condicionales (Branches):60% (6/10)

 TABLA DE COBERTURA POR ARCHIVO:
 ------------------------------------------------------------------------------
 Componente / Archivo                  | % Líneas | % Sent. | % Func. | % Ramas
 ------------------------------------------------------------------------------
 src/index.ts                          |   62.5% |   62.5% |     25% |    100%
 src/quality/errores-object.ts         |      0% |      0% |      0% |    100%
 src/quality/insecure-1-object.ts      |      0% |      0% |    100% |    100%
 src/quality/insecure-2-object.ts      |      0% |      0% |      0% |    100%
 src/value-object/index.ts             |    100% |    100% |    100% |    100%
 src/value-object/primitives/date-value-object.ts|   6.66% |   6.66% |      0% |      0%
 src/value-object/primitives/enum-value-object.ts|  83.33% |  83.33% |    100% |      0%
 src/value-object/primitives/index.ts  |    100% |    100% |    100% |    100%
 src/value-object/primitives/number-value-object.ts|    100% |    100% |    100% |    100%
 src/value-object/primitives/string-value-object.ts|    100% |    100% |    100% |    100%
 ------------------------------------------------------------------------------

--------------------------------------------------------------------------------
 4. COMPONENTES Y LÍNEAS DE CÓDIGO NO CUBIERTAS CON PRUEBAS
--------------------------------------------------------------------------------
 A continuación se detallan los módulos donde falta cobertura y las líneas exactas:

 1. [src/index.ts]
    - Cobertura de líneas:  62.5% (5/8 líneas)
    - Líneas no cubiertas:  8-10 (Llamada asíncrona fetchData() no testeada).
 2. [src/quality/errores-object.ts]
    - Cobertura de líneas:  0% (0/3 líneas)
    - Líneas no cubiertas:  2-3, 6 (Clases y asignaciones sin tests unitarios asociados).
 3. [src/quality/insecure-1-object.ts]
    - Cobertura de líneas:  0% (0/6 líneas)
    - Líneas no cubiertas:  1-3, 5, 7, 10 (Servidor Express y renderizado Pug).
 4. [src/quality/insecure-2-object.ts]
    - Cobertura de líneas:  0% (0/11 líneas)
    - Líneas no cubiertas:  1-2, 6-7, 11-12, 18, 22, 24, 30, 32 (Módulo de seguridad sin pruebas).
 5. [src/value-object/primitives/date-value-object.ts]
    - Cobertura de líneas:  6.66% (1/15 líneas)
    - Líneas no cubiertas:  3, 7-9, 13-14, 19, 23-25, 29-30, 34-35 (Falta suite de tests para DateValueObject).
 6. [src/value-object/primitives/enum-value-object.ts]
    - Cobertura de líneas:  83.33% (5/6 líneas)
    - Líneas no cubiertas:  11 (Condicional de valor no admitido).
```

### 2.4 Evidencias Registradas de la Parte 1
* Registro de salida guardado en: `evidencia/parte1/E1_01_ejecucion_script_pruebas_ChRiStIaNo0O.txt`
* Commit firmado: `[ChRiStIaNo0O] feat(pruebas): creacion de script de analisis de pruebas unitarias y reporte de cobertura` (Hash: `6245a26`).

---

## 3. Parte 2: Análisis de Seguridad de Código Estático

> **Responsable:** Danilo Romero G. (`DMROMEROG`)

### 3.1 Integración y Conexión con SonarCloud
Se configuró el archivo oficial de propiedades de escaneo [`sonar-project.properties`](file:///C:/Users/chris/.gemini/antigravity/scratch/AUY1102-Pipeline/sonar-project.properties) en la raíz del repositorio:

```properties
sonar.projectKey=CVDS-Grupo5_AUY1102-Pipeline
sonar.projectName=AUY1102-Pipeline
sonar.sources=src
sonar.tests=test
sonar.test.inclusions=**/*.test.ts
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.typescript.lcov.reportPaths=coverage/lcov.info
sonar.exclusions=node_modules/**,dist/**,coverage/**,**/*.d.ts
sonar.sourceEncoding=UTF-8
```

* El repositorio fue conectado en la consola de SonarCloud bajo la organización `CVDS-Grupo5`, permitiendo la revisión automática de métricas de fiabilidad, seguridad y cobertura en cada Pull Request y push a la rama principal.

### 3.2 Integración y Escaneo con Snyk
Se añadió el proyecto `CVDS-Grupo5/AUY1102-Pipeline` a la consola web de **Snyk**:
* **Alcance del análisis:**
  1. *Snyk Open Source (SCA):* Detección de vulnerabilidades en dependencias declaradas en `package.json` y `package-lock.json`.
  2. *Snyk Code (SAST):* Detección de vulnerabilidades en el código fuente TypeScript (`src/quality/`).
* Hallazgo principal: La versión `chokidar@2.0.3` arrastraba 129 paquetes obsoletos con múltiples vulnerabilidades de severidad Alta y Crítica (ReDoS, Path Traversal).

### 3.3 Auditoría de Seguridad con `npm audit`
Se ejecutó el comando de auditoría nativo de npm:

```bash
npm audit
```

**Resultado inicial:**
* Total de vulnerabilidades detectadas: **82 vulnerabilidades**
  * Críticas: 2
  * Altas: 49
  * Moderadas: 20
  * Bajas: 11
* Evidencia guardada en: `evidencia/parte2/E2_02_npm_audit_consola_DMROMEROG.txt`.

### 3.4 GitHub Advanced Security (GHAS)
Al configurarse el repositorio como público en la organización `CVDS-Grupo5`, GitHub activó automáticamente las características de seguridad avanzada:
1. **Secret Scanning:**
   * Detección y bloqueo preventivo del token Personal Access Token (`github_pat_...`) expuesto en `credentials.yml` y de los tokens ficticios en `src/index.ts`.
2. **Dependabot & Dependency Graph:**
   * Notificación inmediata de **66 alertas de seguridad activas** en las dependencias del proyecto (`https://github.com/CVDS-Grupo5/AUY1102-Pipeline/security/dependabot`).

---

### 3.5 Remediaciones Implementadas

Se aplicaron remediaciones concretas tanto en el código fuente como en la gestión de dependencias:

#### Remediación 1: Corrección de Código y Tipos en `src/quality/errores-object.ts`
* **Defecto detectado:** Asignación inválida de número a variable con tipo `string` explícito (`const message: string = 10;`), generando error de compilación TypeScript y code smell en SonarCloud.
* **Solución aplicada:** Se corrigió el valor asignado para respetar el tipo de dato consistente:
  ```typescript
  // Remediación: se corrige la asignación de número a tipo string
  const message: string = '10';
  ```

#### Remediación 2: Sanitización de Inyección SQL y Exposición de Credenciales en `src/quality/insecure-2-object.ts`
* **Defecto detectado:** Consulta SQL vulnerable construida por concatenación directa (`SELECT * FROM Users WHERE username='${username}'`) y contraseñas expuestas en texto plano.
* **Solución aplicada:**
  ```typescript
  // Prevención de Inyección SQL mediante parametrización
  const username = "admin";
  const queryString = "SELECT * FROM Users WHERE username = ?";

  // Mitigación de XSS mediante codificación de salida
  const userInput = '<script>alert("XSS");</script>';
  const html = `<div>${encodeURIComponent(userInput)}</div>`;

  // Gestión segura de credenciales mediante variables de entorno
  const config = {
    dbUsername: process.env.DB_USERNAME || 'admin_user',
    dbPassword: process.env.DB_PASSWORD || '',
    apiKey: process.env.API_KEY || '',
  };
  ```

#### Remediación 3: Protección de Credenciales en `credentials.yml`
* **Defecto detectado:** Token de acceso de GitHub hardcodeado en el repositorio.
* **Solución aplicada:** Reemplazo por referencia a variable de entorno (`${GITHUB_TOKEN}`).

#### Remediación 4: Actualización de Dependencia Vulnerable `chokidar` en `package.json`
* **Defecto detectado:** `chokidar@2.0.3` (descontinuado y sin parches de seguridad desde 2019).
* **Solución aplicada:** Actualización a `chokidar@^3.6.0`:
  * Se removieron **129 paquetes obsoletos/vulnerables**.
  * Las vulnerabilidades de `npm audit` disminuyeron inmediatamente de 82 a 76, mitigando 5 vulnerabilidades de severidad Alta.

* Commit firmado: `[DMROMEROG] fix(seguridad): remediacion de vulnerabilidades en codigo y actualizacion de dependencias segun analisis SAST` (Hash: `df6a8fc`).

---

## 4. Estructura de Evidencias en el Repositorio

Todas las evidencias y reportes quedan almacenados en la carpeta [`evidencia/`](file:///C:/Users/chris/.gemini/antigravity/scratch/AUY1102-Pipeline/evidencia):

```text
evidencia/
├── parte1/
│   ├── E1_01_ejecucion_script_pruebas_ChRiStIaNo0O.txt
│   └── E1_02_captura_cobertura_y_fallos_ChRiStIaNo0O.png
└── parte2/
    ├── E2_01_sonarcloud_dashboard_ChRiStIaNo0O.png
    ├── E2_02_npm_audit_consola_DMROMEROG.txt
    ├── E2_03_snyk_dashboard_vulnerabilidades_DMROMEROG.png
    ├── E2_04_github_advanced_security_secret_scanning_DMROMEROG.png
    └── E2_05_remediacion_codigo_diff_DMROMEROG.png
```

---

## 5. Conclusiones

1. **Impacto de las Pruebas Unitarias:** La automatización de pruebas unitarias y el cálculo de métricas de cobertura con herramientas como Jest e Istanbul permiten cuantificar objetivamente la salud del código, exponiendo qué componentes carecen de pruebas (como `date-value-object.ts` con solo 6.66% de cobertura) para focalizar esfuerzos de calidad.
2. **Importancia del Análisis de Seguridad Estático:** La integración combinada de SonarCloud, Snyk, `npm audit` y GitHub Advanced Security proporciona una visión en 360 grados de la seguridad, abarcando desde malas prácticas de codificación interna hasta vulnerabilidades críticas heredadas de la cadena de suministro de código abierto (SCA).
3. **Cultura DevSecOps y Shift-Left:** Al aplicar remediaciones tempranas sobre el repositorio, se demuestra que la seguridad no es una etapa tardía, sino un componente continuo del ciclo de vida del software que optimiza costos y minimiza riesgos operacionales.
