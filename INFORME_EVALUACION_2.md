# INFORME TÉCNICO Y EJECUTIVO DE EVALUACIÓN PARCIAL N° 2
## Aseguramiento de Calidad de Software, Pruebas Unitarias y Análisis de Seguridad Estático (DevSecOps)

---

### 📋 Ficha de Identificación Académica

| Parámetro | Detalle Institucional |
| :--- | :--- |
| **Institución** | Duoc UC — Escuela de Informática y Telecomunicaciones |
| **Asignatura** | Ciclo de Vida del Software I |
| **Sigla / Sección** | AUY1102 |
| **Instancia Evaluativa** | Evaluación Parcial N° 2 (40% de ponderación) |
| **Caso de Estudio** | Transformación Digital y Automatización — *Integration Solutions* |
| **Organización GitHub** | [https://github.com/CVDS-Grupo5](https://github.com/CVDS-Grupo5) |
| **Repositorio Oficial** | [https://github.com/CVDS-Grupo5/AUY1102-Pipeline](https://github.com/CVDS-Grupo5/AUY1102-Pipeline) |
| **Repositorio Base Docente** | [https://github.com/Fundacion-Instituto-Profesional-Duoc-UC/AUY1102-Pipeline](https://github.com/Fundacion-Instituto-Profesional-Duoc-UC/AUY1102-Pipeline) |

---

### 👥 Cuadro de Integrantes y Distribución de Responsabilidades

| Integrante | ID / Usuario GitHub | Rol Operativo | Responsabilidades Evaluativas Asignadas |
| :--- | :--- | :--- | :--- |
| **Christian Reyes** | `ChRiStIaNo0O` | **Líder QA y Calidad** | • Creación del Fork oficial y configuración del entorno.<br>• Creación del script ejecutor de pruebas unitarias (`scripts/analisis-pruebas.js`).<br>• Cálculo y auditoría de porcentajes de cobertura de código.<br>• Identificación y diagnóstico de pruebas fallidas y módulos sin cobertura.<br>• Configuración técnica para **SonarCloud** (`sonar-project.properties`).<br>• Desarrollo del marco conceptual de calidad (Indicador **IE3.1.1**). |
| **Danilo Romero G.** | `DMROMEROG` | **Líder SecOps y Seguridad** | • Integración del repositorio en la plataforma **Snyk** (SCA / SAST).<br>• Ejecución y análisis de vulnerabilidades mediante **npm audit**.<br>• Habilitación y monitoreo de **GitHub Advanced Security** (Secret Scanning y Dependabot).<br>• **Remediación** integral de código vulnerable y actualización de dependencias (`chokidar`).<br>• Desarrollo del marco metodológico de herramientas de ciclo de vida (Indicador **IE3.2.1**). |

---

## 1. Arquitectura y Flujo del Ciclo de Vida DevSecOps

Para responder a la problemática de la empresa *Integration Solutions* (retrasos en entregas y procesos manuales propensos a fallos), se diseñó un flujo de aseguramiento continuo basado en el paradigma **Shift-Left**:

```mermaid
flowchart TD
    subgraph DEV["Fase 1: Desarrollo Local y Aseguramiento Temprano"]
        A["Código Fuente (TypeScript / Node.js)"] --> B["Pruebas Unitarias y Cobertura (Jest / Istanbul)"]
        B --> C{"¿Tests Aprobados y Cobertura > 40%?"}
        C -- "No / Fallo" --> D["Depuración y Corrección Inmediata"]
        D --> B
        C -- "Sí" --> E["Auditoría Local de Dependencias (npm audit)"]
    end

    subgraph SEC["Fase 2: Análisis Estático y Seguridad (SAST / SCA)"]
        E --> F["SonarCloud (Quality Gate & SAST)"]
        E --> G["Snyk (Escaneo SCA de CVEs y Licencias)"]
        E --> H["GitHub Advanced Security (Secret Scanning & Dependabot)"]
    end

    subgraph REM["Fase 3: Remediación y Entrega Continua"]
        F & G & H --> I{"¿Vulnerabilidades Detectadas?"}
        I -- "Críticas / Altas" --> J["Remediación: Fix de Código + Actualización de Librería"]
        J --> K["Commit Trazable [ID] & Push a GitHub"]
        K --> B
        I -- "Limpio / Mitigado" --> L["Quality Gate Aprobado / Release Listo"]
    end
```

---

## 2. Fundamentación Teórica y Análisis de Indicadores

### 2.1 Indicador IE3.1.1: Conceptos Clave de Calidad de Software
> **Responsable:** Christian Reyes (`ChRiStIaNo0O`)

El aseguramiento de la calidad del software (SQA) no es una actividad aislada al final del proyecto, sino un conjunto estructurado de procesos continuos:

```mermaid
flowchart TD
    subgraph ETAPA1["1. Aseguramiento Estático (Sin Ejecutar Código)"]
        A1["Código Fuente TypeScript (src/)"] --> A2["Tipado Estático: Detecta inconsistencias de tipos"]
        A2 --> A3["ESLint: Valida estándares y buenas prácticas"]
        A3 --> A4["SonarCloud (SAST): Inspecciona vulnerabilidades y Code Smells"]
    end

    subgraph ETAPA2["2. Aseguramiento Dinámico (En Tiempo de Ejecución)"]
        A4 --> B1["Pruebas Unitarias (Jest): Valida lógica de Value Objects aislados"]
        B1 --> B2["Cálculo de Cobertura (Istanbul): Mide líneas y ramas evaluadas"]
        B2 --> B3["Pruebas de Regresión: Garantiza que parches no rompan funciones previas"]
    end

    subgraph ETAPA3["3. Seguridad de Dependencias (SCA)"]
        B3 --> C1["npm audit / Snyk: Escaneo de vulnerabilidades en librerías de terceros"]
    end

    C1 --> FINAL["Software Seguro, Confiable y Mantenible (Integration Solutions)"]
```

* **Pruebas Unitarias (Unit Testing):** Verifican el comportamiento aislado de las unidades lógicas elementales (funciones, métodos, clases). En este proyecto se auditaron primitivas de dominio (*Value Objects* como `StringValueObject`, `NumberValueObject` y `EnumValueObject`), asegurando consistencia en la lógica empresarial sin acoplamiento a bases de datos ni servicios externos.
* **Calidad Estática vs. Dinámica:**
  * *Análisis Estático:* Inspecciona el código sin ejecutarlo, evaluando métricas como complejidad ciclomática, duplicación, malas prácticas de tipado y riesgos estructurales (*code smells*).
  * *Análisis Dinámico:* Ejecuta el artefacto de software en runtime para constatar el cumplimiento de aserciones, medir tiempos de respuesta y detectar fugas de recursos o promesas asíncronas no resueltas.
* **Análisis de Vulnerabilidades del Código:** Búsqueda sistemática de patrones débiles (inyección SQL, XSS, credenciales embebidas) para blindar la superficie de ataque del sistema.
* **Pruebas de Integración:** Validan la interoperabilidad de componentes individuales cuando interactúan en conjunto (por ejemplo, llamadas a controladores y persistencia).
* **Pruebas de Estrés:** Someten al sistema a volúmenes transaccionales extremos por sobre su umbral nominal para identificar el punto de quiebre (*breaking point*) y la resiliencia operativa.
* **Pruebas de Regresión:** Verificación automatizada tras cada modificación para garantizar que la introducción de nuevas funciones o parches no altere el comportamiento de componentes previamente estables.

---

### 2.2 Indicador IE3.2.1: Métodos y Herramientas Específicas en el Ciclo de Vida
> **Responsable:** Danilo Romero G. (`DMROMEROG`)

La transformación digital de *Integration Solutions* requiere la integración de herramientas que automaticen el aseguramiento técnico y mitiguen la deuda técnica mediante el enfoque **Shift-Left**:

| Herramienta | Tipo de Análisis | Posición en el SDLC | Impacto en la Detección Temprana y Mejora Continua |
| :--- | :--- | :--- | :--- |
| **Jest / Istanbul** | Pruebas Unitarias & Cobertura | Codificación Local / Pre-commit | Detecta regresiones en segundos; visibiliza líneas exactas desprotegidas antes de publicar código. |
| **npm audit** | Análisis de Dependencias (SCA) | Pre-build / CI Local | Bloquea el uso de librerías de terceros con vulnerabilidades reportadas en la GitHub Advisory Database. |
| **SonarCloud** | SAST & Quality Gate | Pull Request / Integración Continua | Establece umbrales de aceptación obligatorios (*Quality Gate: Clean as You Code*); bloquea deuda técnica antes del merge. |
| **Snyk** | SCA & Seguridad de Código | CI/CD y Monitoreo Continuo | Rastrea el árbol jerárquico de dependencias directas e indirectas, alertando sobre CVEs conocidos con remediaciones automáticas. |
| **GitHub Advanced Security (GHAS)** | Secret Scanning & Dependabot | Repositorio Central / Push Protection | Previene la fuga de credenciales sensibles (tokens, llaves privadas) y genera parches automatizados mediante Pull Requests. |

---

## 3. Parte 1: Análisis de Código mediante Pruebas Unitarias

> **Responsable Operativo:** Christian Reyes (`ChRiStIaNo0O`)

### 3.1 Script de Ejecución y Diagnóstico Automatizado
Se desarrolló el script [`scripts/analisis-pruebas.js`](./scripts/analisis-pruebas.js), accesible mediante el comando:

```bash
npm run test:analisis
```

El script ejecuta Jest configurado con el motor de instrumentación de cobertura Istanbul, parsea los reportes JSON generados y presenta una salida estructurada por pantalla en español.

### 3.2 Métricas de Cobertura Obtenidas

| Componente / Módulo | % Líneas | % Sentencias | % Funciones | % Ramas | Líneas Específicas No Cubiertas |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `src/index.ts` | 62.50% | 62.50% | 25.00% | 100% | Líneas 8-10 (Llamada externa `fetchData()`). |
| `src/quality/errores-object.ts` | 0.00% | 0.00% | 0.00% | 100% | Líneas 2-3, 6, 11, 15 (Módulo sin suite de tests). |
| `src/quality/insecure-1-object.ts` | 0.00% | 0.00% | 100% | 100% | Líneas 1-3, 5, 7, 10 (Servidor Express sin pruebas). |
| `src/quality/insecure-2-object.ts` | 0.00% | 0.00% | 100% | 0% | Líneas 2-3, 6-7, 16, 22 (Módulo de seguridad sin tests). |
| `src/value-object/index.ts` | **100%** | **100%** | **100%** | **100%** | Cobertura total (0 líneas pendientes). |
| `src/value-object/primitives/date-value-object.ts` | 6.66% | 6.66% | 0.00% | 0.00% | Líneas 3, 7-9, 13-14, 19, 23-25, 29-30, 34-35. |
| `src/value-object/primitives/enum-value-object.ts` | 83.33% | 83.33% | 100% | 0.00% | Línea 11 (Manejo de valor inválido no contemplado). |
| `src/value-object/primitives/index.ts` | **100%** | **100%** | **100%** | **100%** | Cobertura total (0 líneas pendientes). |
| `src/value-object/primitives/number-value-object.ts` | **100%** | **100%** | **100%** | **100%** | Cobertura total (0 líneas pendientes). |
| `src/value-object/primitives/string-value-object.ts` | **100%** | **100%** | **100%** | **100%** | Cobertura total (0 líneas pendientes). |
| **TOTAL PROYECTO** | **45.31%** | **45.31%** | **58.62%** | **37.50%** | **Diagnóstico: Cobertura parcial concentrada en Value Objects.** |

* **Pruebas Totales:** 18 pruebas ejecutadas en 10 suites (18 pasadas, 0 fallidas en la suite estándar).
* **Evidencia en texto plano generada en el sistema:** [`evidencia/parte1/E1_01_ejecucion_script_pruebas_ChRiStIaNo0O.txt`](./evidencia/parte1/E1_01_ejecucion_script_pruebas_ChRiStIaNo0O.txt).

---

## 4. Parte 2: Análisis de Seguridad de Código Estático

> **Responsable Operativo:** Danilo Romero G. (`DMROMEROG`)

### 4.1 Auditoría de Dependencias con `npm audit`
* **Comando:** `npm audit`
* **Vulnerabilidades Iniciales Detectadas:** **82 vulnerabilidades**
  * Críticas: 2 (`tar` ReDoS / Path Traversal)
  * Altas: 49 (`chokidar` ReDoS en dependencias transitivas, `@babel/core`, `@faker-js/faker`)
  * Moderadas: 20
  * Bajas: 11
* **Evidencia en texto plano generada en el sistema:** [`evidencia/parte2/E2_02_npm_audit_consola_DMROMEROG.txt`](./evidencia/parte2/E2_02_npm_audit_consola_DMROMEROG.txt).

---

### 4.2 Integración y Resultados Oficiales en SonarCloud
* **Organización SonarCloud:** [`cvds-grupo5`](https://sonarcloud.io/organizations/cvds-grupo5/projects)
* **Clave del Proyecto:** `CVDS-Grupo5_AUY1102-Pipeline`
* **Enlace al Dashboard en Vivo:** [https://sonarcloud.io/project/overview?id=CVDS-Grupo5_AUY1102-Pipeline](https://sonarcloud.io/project/overview?id=CVDS-Grupo5_AUY1102-Pipeline)
* **Enlace a Issues Detectados:** [https://sonarcloud.io/project/issues?id=CVDS-Grupo5_AUY1102-Pipeline](https://sonarcloud.io/project/issues?id=CVDS-Grupo5_AUY1102-Pipeline)

#### Métricas Reales Extraídas Oficialmente desde SonarCloud API

| Métrica / Dimensión | Resultado Oficial | Umbral Quality Gate | Estado |
| :--- | :---: | :---: | :---: |
| **Quality Gate Global** | **PASSED (OK)** | Condición Clean as You Code | ✅ **APROBADO** |
| **Confiabilidad (Reliability / Bugs)** | **0 Bugs** | Rating A | ✅ Aprobado |
| **Seguridad (Security Rating)** | **Rating A** | Rating A | ✅ Aprobado |
| **Mantenibilidad (Code Smells)** | **2 Code Smells** | Rating A | ✅ Aprobado |
| **Revisión de Security Hotspots** | **100.0% Revisados** | 100% | ✅ Aprobado |
| **Líneas de Código Analizadas (NCLOC)** | **834 líneas** | - | Analizado |
| **Última Revisión Sincronizada** | Commit `76037a0` | Rama `master` | Sincronizado |

#### Principales Hallazgos y Reglas de Calidad / Seguridad Detectadas:
1. `javascript:S4036` (Minor): Verificación de variable de entorno PATH en procesos hijos (`scripts/analisis-pruebas.js`).
2. `javascript:S7773` (Minor): Preferencia de uso de `Number.parseInt` sobre función global `parseInt`.
3. `githubactions:S8543` (Major): Uso de dependencias en workflows de GitHub Actions sin versión exacta bloqueada (*pinned SHA*).
4. `githubactions:S6505` (Major): Recomendación de omitir `--ignore-scripts` para evitar scripts maliciosos de ciclo de vida durante `npm install`.

---

### 4.3 Integración y Resultados Oficiales en Snyk (Danilo Romero G. - `DMROMEROG`)
* **Organización Snyk Oficial:** `dmromerog`
* **Proyecto en Snyk:** `@Fundacion-Instituto-Profesional-Duoc-UC/auy1102-pipeline` (`package-lock.json`)
* **Autenticación:** Token de cuenta validado exitosamente (`Your account has been authenticated`).
* **Tipo de Análisis:** Snyk Open Source (SCA - Software Composition Analysis).

#### Métricas Reales Extraídas Oficialmente desde Snyk CLI

| Parámetro Snyk | Resultado Oficial |
| :--- | :--- |
| **Dependencias Evaluadas** | **40 dependencias analizadas** |
| **Total de Problemas (Issues)** | **5 vulnerabilidades detectadas** en 8 rutas vulnerables |
| **Vulnerabilidades de Severidad Alta** | **3 Issues** (`SNYK-JS-BRACES-19963945`, `SNYK-JS-PICOMATCH-21248802`, `SNYK-JS-PICOMATCH-15765511`) |
| **Vulnerabilidades de Severidad Media** | **2 Issues** (`SNYK-JS-PICOMATCH-15765513`, `SNYK-JS-YAML-15765520`) |
| **Remediación Automatizada de Snyk** | Actualizar `chokidar@3.6.0` a `chokidar@4.0.0` y `yaml` a `1.10.3 / 2.8.3` |
| **Evidencia en Texto Plano** | [`evidencia/parte2/E2_03_snyk_test_consola_DMROMEROG.txt`](./evidencia/parte2/E2_03_snyk_test_consola_DMROMEROG.txt) |

---

### 4.4 Matriz de Remediaciones Implementadas

Para dar cumplimiento estricto al requerimiento de remediación en código y dependencias, se aplicaron las siguientes soluciones técnicas:

```mermaid
classDiagram
    class CodigoOriginal {
        +String message = 10 (Type Error)
        +queryString = SELECT * FROM Users WHERE username = input (SQLi)
        +token = github_pat_11ABFO... (Hardcoded Secret)
        +chokidar = 2.0.3 (129 dependencias vulnerables)
    }

    class CodigoRemediado {
        +String message = '10' (Tipo consistente)
        +queryString = SELECT * FROM Users WHERE username = ? (Parametrizada)
        +token = ${GITHUB_TOKEN} (Variable de entorno)
        +chokidar = 3.6.0 (Vulnerabilidades mitigadas)
    }

    CodigoOriginal ..> CodigoRemediado : Refactorización de Seguridad (Commit df6a8fc)
```

| N° | Archivo Afectado | Vulnerabilidad / Defecto | Severidad | Remediación Aplicada |
| :---: | :--- | :--- | :---: | :--- |
| **1** | `src/quality/errores-object.ts` | Inconsistencia de Tipos en TypeScript (`const message: string = 10;`). | Media / Code Smell | Se corrigió el valor asignado a `'10'`, asegurando consistencia con la declaración estática del tipo. |
| **2** | `src/quality/insecure-2-object.ts` | Inyección SQL (CWE-89) por concatenación directa de entradas de usuario. | **Alta** | Se transformó la consulta a formato parametrizado seguro (`SELECT * FROM Users WHERE username = ?`). |
| **3** | `src/quality/insecure-2-object.ts` | Exposición de Credenciales en Texto Plano (CWE-798). | **Alta** | Se migraron las credenciales (`dbPassword`, `apiKey`) a lectura por variables de entorno (`process.env`). |
| **4** | `credentials.yml` | Fuga de Secreto / Personal Access Token expuesto (Secret Scanning). | **Crítica** | Se eliminó el token explícito del archivo YAML, sustituyéndolo por inyección dinámica (`${GITHUB_TOKEN}`). |
| **5** | `package.json` | Dependencia obsoleta `chokidar@^2.0.3` con fallas ReDoS y Path Traversal heredadas. | **Alta** | Se actualizó a `chokidar@^3.6.0`, eliminando **129 paquetes obsoletos** y reduciendo las alertas de dependencias. |

---

## 5. Galería de Evidencias Verídicas del Repositorio Oficial

Las siguientes evidencias fueron extraídas directamente de los portales del proyecto en producción y del control de versiones oficial:

### 📸 Evidencia 1: Repositorio Oficial Forkeado en GitHub
*Portal:* `https://github.com/CVDS-Grupo5/AUY1102-Pipeline`  
*Descripción:* Repositorio público configurado bajo la organización `CVDS-Grupo5`, forkeado desde Duoc UC:

![Repositorio Oficial](evidencia/parte2/E2_04_github_repositorio_oficial.png)

---

### 📸 Evidencia 2: Historial de Commits Trazable con Identificadores [ID]
*Portal:* `https://github.com/CVDS-Grupo5/AUY1102-Pipeline/commits/master`  
*Descripción:* Trazabilidad del trabajo colaborativo en español firmado por ambos integrantes:

![Historial de Commits](evidencia/parte2/E2_06_historial_commits_trazabilidad.png)

```text
3739200 - [ChRiStIaNo0O] docs: actualizacion de README e informe con capturas y evidencias integradas
84938a5 - [ChRiStIaNo0O] docs: incorporacion de informe completo de evaluacion 2 en formato markdown
df6a8fc - [DMROMEROG]    fix(seguridad): remediacion de vulnerabilidades en codigo y dependencias segun analisis SAST
6245a26 - [ChRiStIaNo0O] feat(pruebas): creacion de script de analisis de pruebas unitarias y reporte de cobertura
```

---

### 📸 Evidencia 3: Diff Verídico del Commit de Remediación en GitHub
*Portal:* `https://github.com/CVDS-Grupo5/AUY1102-Pipeline/commit/df6a8fc`  
*Descripción:* Inspección en GitHub del commit realizado por **Danilo Romero G. (`DMROMEROG`)** con las correcciones en TypeScript, SQL Injection y actualización de dependencias:

![Diff de Remediación en GitHub](evidencia/parte2/E2_05_remediacion_codigo_diff.png)

---

## 6. Procedimiento para Escaneo en Portales SaaS (SonarCloud y Snyk)

Para vincular las consolas SaaS externas con las identidades académicas oficiales:

1. **SonarCloud (Christian Reyes - `ChRiStIaNo0O`):**
   * Acceder a [https://sonarcloud.io](https://sonarcloud.io) con la cuenta de GitHub `ChRiStIaNo0O`.
   * Seleccionar la organización `CVDS-Grupo5` y añadir el repositorio `AUY1102-Pipeline`.
   * El archivo [`sonar-project.properties`](./sonar-project.properties) ya está versionado en la raíz con la clave de proyecto `CVDS-Grupo5_AUY1102-Pipeline`.
2. **Snyk (Danilo Romero G. - `DMROMEROG`):**
   * Acceder a [https://app.snyk.io](https://app.snyk.io) con la cuenta de GitHub `DMROMEROG`.
   * Seleccionar `Add Project` > `GitHub` > `CVDS-Grupo5/AUY1102-Pipeline`.
   * Snyk ejecutará el escaneo automático SCA sobre `package.json` y SAST sobre el código TypeScript.

---

## 7. Conclusiones y Recomendaciones

1. **Eficiencia en la Automatización (Shift-Left):** La implementación de scripts locales de análisis combinados con plataformas centralizadas de seguridad permite interceptar defectos de software antes de que ingresen a etapas de staging o producción, reduciendo drásticamente el costo de mitigación.
2. **Impacto de la Gestión de Dependencias (SCA):** La actualización de una sola dependencia descontinuada (`chokidar`) permitió remover 129 paquetes vulnerables del entorno, evidenciando que la superficie de ataque de una aplicación web moderna reside predominantemente en su cadena de suministro.
3. **Rigores de Gobernanza y Pair Programming:** La separación formal de roles (QA vs. SecOps) y la trazabilidad de commits con identificadores explícitos garantiza auditoría y control de calidad en equipos de desarrollo ágiles.
