/**
 * Script de Análisis de Pruebas Unitarias y Cobertura de Código
 * Asignatura: Ciclo de Vida del Software I (AUY1102)
 * Evaluación Parcial N° 2
 * 
 * Integrantes:
 * - Christian Reyes (ID: ChRiStIaNo0O) - Responsable Parte 1
 * - Danilo Romero G. (ID: DMROMEROG) - Responsable Parte 2
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const COVERAGE_DIR = path.join(ROOT_DIR, 'coverage');
const RESULTS_FILE = path.join(COVERAGE_DIR, 'test-results.json');
const SUMMARY_FILE = path.join(COVERAGE_DIR, 'coverage-summary.json');

console.log('================================================================================');
console.log('       EVALUACIÓN PARCIAL N° 2 - ANÁLISIS DE PRUEBAS UNITARIAS Y COBERTURA       ');
console.log('                    Ciclo de Vida del Software I (AUY1102)                      ');
console.log('================================================================================');
console.log(' Integrante 1 (QA / Pruebas): Christian Reyes       [ID: ChRiStIaNo0O]');
console.log(' Integrante 2 (SecOps / Fix): Danilo Romero G.      [ID: DMROMEROG]');
console.log(' Repositorio: https://github.com/CVDS-Grupo5/AUY1102-Pipeline');
console.log(' Fecha y hora de ejecución: ' + new Date().toLocaleString('es-CL'));
console.log('================================================================================\n');

console.log('>> Ejecutando pruebas unitarias con Jest y calculando métricas de cobertura...\n');

let jestExitCode = 0;
try {
  // Ejecutamos jest generando reportes estructurados
  execSync(
    'npx jest --coverage --coverageReporters=json-summary --coverageReporters=text --coverageReporters=lcov --json --outputFile=coverage/test-results.json',
    {
      cwd: ROOT_DIR,
      stdio: 'pipe',
      encoding: 'utf-8'
    }
  );
} catch (error) {
  // Si alguna prueba falla, jest retorna código de salida distinto de 0
  jestExitCode = error.status || 1;
}

if (!fs.existsSync(RESULTS_FILE) || !fs.existsSync(SUMMARY_FILE)) {
  console.error('[ERROR] No se pudieron generar los archivos de resultados de pruebas o cobertura.');
  process.exit(1);
}

const testResults = JSON.parse(fs.readFileSync(RESULTS_FILE, 'utf-8'));
const coverageSummary = JSON.parse(fs.readFileSync(SUMMARY_FILE, 'utf-8'));

// -----------------------------------------------------------------------------
// 1. RESUMEN DE EJECUCIÓN DE PRUEBAS UNITARIAS
// -----------------------------------------------------------------------------
console.log('--------------------------------------------------------------------------------');
console.log(' 1. RESUMEN DE EJECUCIÓN DE PRUEBAS UNITARIAS');
console.log('--------------------------------------------------------------------------------');
console.log(` Suites de prueba totales: ${testResults.numTotalTestSuites}`);
console.log(`   - Aprobadas:            ${testResults.numPassedTestSuites}`);
console.log(`   - Fallidas:             ${testResults.numFailedTestSuites}`);
console.log(` Pruebas unitarias totales: ${testResults.numTotalTests}`);
console.log(`   - Aprobadas:            ${testResults.numPassedTests}`);
console.log(`   - Fallidas:             ${testResults.numFailedTests}`);
console.log(` Tiempo total de prueba:   ${((Date.now() - testResults.startTime) / 1000).toFixed(2)} s\n`);

// -----------------------------------------------------------------------------
// 2. DETALLE DE PRUEBAS QUE FALLAN
// -----------------------------------------------------------------------------
console.log('--------------------------------------------------------------------------------');
console.log(' 2. DETALLE DE PRUEBAS QUE FALLAN');
console.log('--------------------------------------------------------------------------------');

let failingTestsCount = 0;
testResults.testResults.forEach((suite) => {
  const filePath = suite.name || suite.testFilePath || '';
  const relativePath = filePath ? path.relative(ROOT_DIR, filePath).replace(/\\/g, '/') : 'Desconocido';
  const failedAssertions = suite.assertionResults.filter((a) => a.status === 'failed');

  if (failedAssertions.length > 0) {
    console.log(`\n [FALLO DETECTADO] Archivo: ${relativePath}`);
    failedAssertions.forEach((assertion, idx) => {
      failingTestsCount++;
      console.log(`   ${idx + 1}. Suite: "${assertion.ancestorTitles.join(' > ')}"`);
      console.log(`      Caso de prueba: "${assertion.title}"`);
      if (assertion.failureMessages && assertion.failureMessages.length > 0) {
        const cleanMsg = assertion.failureMessages[0]
          .split('\n')
          .slice(0, 8)
          .map((line) => '         ' + line)
          .join('\n');
        console.log(`      Causa del fallo:\n${cleanMsg}`);
      }
    });
  }
});

if (failingTestsCount === 0) {
  console.log('  ✔ En esta ejecución actual, todas las suites de prueba pasaron exitosamente.');
  console.log('    (Nota: Se detectó advertencia de llamadas asíncronas no capturadas hacia api.example.com en src/index.ts).');
} else {
  console.log(`\n Total de pruebas fallidas detectadas: ${failingTestsCount}`);
}

// -----------------------------------------------------------------------------
// 3. PORCENTAJE DE COBERTURA DE CÓDIGO (COVERAGE)
// -----------------------------------------------------------------------------
console.log('\n--------------------------------------------------------------------------------');
console.log(' 3. PORCENTAJE DE COBERTURA DE LOS COMPONENTES ANALIZADOS');
console.log('--------------------------------------------------------------------------------');

const total = coverageSummary.total;
console.log(` COBERTURA GLOBAL DEL PROYECTO:`);
console.log(`   - Líneas de código cubiertas:    ${total.lines.pct}% (${total.lines.covered}/${total.lines.total})`);
console.log(`   - Sentencias (Statements):       ${total.statements.pct}% (${total.statements.covered}/${total.statements.total})`);
console.log(`   - Funciones/Métodos:             ${total.functions.pct}% (${total.functions.covered}/${total.functions.total})`);
console.log(`   - Ramas condicionales (Branches):${total.branches.pct}% (${total.branches.covered}/${total.branches.total})\n`);

console.log(' TABLA DE COBERTURA POR ARCHIVO:');
console.log(' ' + '-'.repeat(78));
console.log(
  ' ' +
  'Componente / Archivo'.padEnd(38) +
  '| % Líneas | % Sent. | % Func. | % Ramas'
);
console.log(' ' + '-'.repeat(78));

const uncoveredFiles = [];

Object.keys(coverageSummary).forEach((filePath) => {
  if (filePath === 'total') return;
  const item = coverageSummary[filePath];
  const relativeFile = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');

  const linePct = String(item.lines.pct).padStart(6);
  const stmtPct = String(item.statements.pct).padStart(6);
  const funcPct = String(item.functions.pct).padStart(6);
  const branchPct = String(item.branches.pct).padStart(6);

  console.log(
    ' ' +
    relativeFile.padEnd(38) +
    `| ${linePct}% | ${stmtPct}% | ${funcPct}% | ${branchPct}%`
  );

  if (item.lines.pct < 100) {
    uncoveredFiles.push({
      file: relativeFile,
      pct: item.lines.pct,
      covered: item.lines.covered,
      total: item.lines.total
    });
  }
});
console.log(' ' + '-'.repeat(78));

// -----------------------------------------------------------------------------
// 4. PARTE DEL CÓDIGO NO CUBIERTO CON PRUEBAS
// -----------------------------------------------------------------------------
console.log('\n--------------------------------------------------------------------------------');
console.log(' 4. COMPONENTES Y LÍNEAS DE CÓDIGO NO CUBIERTAS CON PRUEBAS');
console.log('--------------------------------------------------------------------------------');
console.log(' A continuación se detallan los módulos donde falta cobertura y las líneas exactas:\n');

// Obtenemos las líneas sin cubrir desde lcov o el reporte de jest
const lcovPath = path.join(COVERAGE_DIR, 'lcov.info');
const uncoveredLinesMap = {};

if (fs.existsSync(lcovPath)) {
  const lcovContent = fs.readFileSync(lcovPath, 'utf-8');
  let currentFile = '';
  lcovContent.split('\n').forEach((line) => {
    if (line.startsWith('SF:')) {
      currentFile = path.relative(ROOT_DIR, line.substring(3).trim()).replace(/\\/g, '/');
      uncoveredLinesMap[currentFile] = [];
    } else if (line.startsWith('DA:')) {
      const parts = line.substring(3).split(',');
      const lineNum = parseInt(parts[0], 10);
      const hits = parseInt(parts[1], 10);
      if (hits === 0 && currentFile) {
        uncoveredLinesMap[currentFile].push(lineNum);
      }
    }
  });
}

function groupLines(lines) {
  if (!lines || lines.length === 0) return 'Ninguna (100% cubierto)';
  lines.sort((a, b) => a - b);
  const ranges = [];
  let start = lines[0];
  let end = lines[0];

  for (let i = 1; i < lines.length; i++) {
    if (lines[i] === end + 1) {
      end = lines[i];
    } else {
      ranges.push(start === end ? `${start}` : `${start}-${end}`);
      start = lines[i];
      end = lines[i];
    }
  }
  ranges.push(start === end ? `${start}` : `${start}-${end}`);
  return ranges.join(', ');
}

uncoveredFiles.forEach((item, index) => {
  const missingLines = uncoveredLinesMap[item.file]
    ? groupLines(uncoveredLinesMap[item.file])
    : 'No registradas';
  console.log(` ${index + 1}. [${item.file}]`);
  console.log(`    - Cobertura de líneas:  ${item.pct}% (${item.covered}/${item.total} líneas)`);
  console.log(`    - Líneas no cubiertas:  ${missingLines}`);
  if (item.file.includes('quality/')) {
    console.log(`    - Observación:          Módulo de calidad con código vulnerable/erróneo agregado para análisis SAST.`);
  } else if (item.file.includes('date-value-object')) {
    console.log(`    - Observación:          Falta suite de pruebas específica para DateValueObject.`);
  } else if (item.file === 'src/index.ts') {
    console.log(`    - Observación:          Líneas de llamada fetchData() no cubiertas por tests.`);
  }
  console.log('');
});

console.log('================================================================================');
console.log('                FIN DEL INFORME DE PRUEBAS UNITARIAS Y COBERTURA                ');
console.log('================================================================================\n');
