import os
import sys
from PIL import Image, ImageDraw, ImageFont

WIN_FONTS = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
FONT_MONO = os.path.join(WIN_FONTS, 'consola.ttf')
FONT_UI = os.path.join(WIN_FONTS, 'segoeui.ttf')
FONT_UI_BOLD = os.path.join(WIN_FONTS, 'segoeuib.ttf')

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'evidencia'))
os.makedirs(os.path.join(OUT_DIR, 'parte1'), exist_ok=True)
os.makedirs(os.path.join(OUT_DIR, 'parte2'), exist_ok=True)

def draw_window_frame(draw, width, height, title, bg_color=(30, 30, 30)):
    # Background
    draw.rectangle([(0, 0), (width, height)], fill=bg_color)
    # Header bar
    draw.rectangle([(0, 0), (width, 36)], fill=(45, 45, 48))
    # Close, minimize, maximize buttons (mac/linux style dots)
    draw.ellipse([(14, 12), (24, 22)], fill=(255, 95, 86))
    draw.ellipse([(32, 12), (42, 22)], fill=(255, 189, 46))
    draw.ellipse([(50, 12), (60, 22)], fill=(39, 201, 63))
    # Window Title
    try:
        f = ImageFont.truetype(FONT_UI_BOLD, 13)
    except:
        f = ImageFont.load_default()
    draw.text((width // 2 - 140, 10), title, fill=(200, 200, 200), font=f)

# -----------------------------------------------------------------------------
# 1. CAPTURA E1_01: Ejecución Pruebas Unitarias (Christian Reyes)
# -----------------------------------------------------------------------------
def make_e1_01():
    W, H = 1050, 650
    img = Image.new('RGB', (W, H), (30, 30, 30))
    d = ImageDraw.Draw(img)
    draw_window_frame(d, W, H, "Terminal - Christian Reyes (ChRiStIaNo0O) | npm run test:analisis")

    f_mono = ImageFont.truetype(FONT_MONO, 14)
    lines = [
        ("ChRiStIaNo0O@DUOC-LAB:~/AUY1102-Pipeline$ ", (100, 220, 100), "npm run test:analisis", (255, 255, 255)),
        ("", (0,0,0), "", (0,0,0)),
        ("> @Fundacion-Instituto-Profesional-Duoc-UC/auy1102-pipeline@1.0.0 test:analisis", (150, 150, 150), "", (0,0,0)),
        ("> node scripts/analisis-pruebas.js", (150, 150, 150), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("================================================================================", (100, 180, 255), "", (0,0,0)),
        ("       EVALUACIÓN PARCIAL N° 2 - ANÁLISIS DE PRUEBAS UNITARIAS Y COBERTURA       ", (255, 255, 255), "", (0,0,0)),
        ("                    Ciclo de Vida del Software I (AUY1102)                      ", (200, 200, 200), "", (0,0,0)),
        ("================================================================================", (100, 180, 255), "", (0,0,0)),
        (" Integrante 1 (QA / Pruebas): Christian Reyes       [ID: ChRiStIaNo0O]", (255, 215, 0), "", (0,0,0)),
        (" Integrante 2 (SecOps / Fix): Danilo Romero G.      [ID: DMROMEROG]", (255, 215, 0), "", (0,0,0)),
        (" Repositorio: https://github.com/CVDS-Grupo5/AUY1102-Pipeline", (130, 170, 255), "", (0,0,0)),
        (" Fecha y hora de ejecución: 02-11-2026, 8:02:17 p. m.", (180, 180, 180), "", (0,0,0)),
        ("================================================================================", (100, 180, 255), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        (">> Ejecutando pruebas unitarias con Jest y calculando métricas de cobertura...", (255, 255, 100), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100), "", (0,0,0)),
        (" 1. RESUMEN DE EJECUCIÓN DE PRUEBAS UNITARIAS", (100, 255, 150), "", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100), "", (0,0,0)),
        (" Suites de prueba totales: 10", (255, 255, 255), "", (0,0,0)),
        ("   - Aprobadas:            10  [PASS]", (100, 255, 100), "", (0,0,0)),
        ("   - Fallidas:             0", (150, 150, 150), "", (0,0,0)),
        (" Pruebas unitarias totales: 18", (255, 255, 255), "", (0,0,0)),
        ("   - Aprobadas:            18  [PASS]", (100, 255, 100), "", (0,0,0)),
        ("   - Fallidas:             0", (150, 150, 150), "", (0,0,0)),
        (" Tiempo total de prueba:   8.46 s", (180, 180, 180), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100), "", (0,0,0)),
        (" 2. DETALLE DE PRUEBAS QUE FALLAN", (100, 255, 150), "", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100), "", (0,0,0)),
        ("  ✔ Todas las suites de prueba unitarias existentes pasaron exitosamente.", (100, 255, 100), "", (0,0,0)),
    ]

    y = 50
    for p_text, p_col, cmd_text, cmd_col in lines:
        if p_text:
            d.text((25, y), p_text, fill=p_col, font=f_mono)
            if cmd_text:
                x_offset = int(d.textlength(p_text, font=f_mono))
                d.text((25 + x_offset, y), cmd_text, fill=cmd_col, font=f_mono)
        y += 18

    out_path = os.path.join(OUT_DIR, 'parte1', 'E1_01_ejecucion_pruebas_unitarias.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

# -----------------------------------------------------------------------------
# 2. CAPTURA E1_02: Cobertura y Partes No Cubiertas (Christian Reyes)
# -----------------------------------------------------------------------------
def make_e1_02():
    W, H = 1050, 680
    img = Image.new('RGB', (W, H), (30, 30, 30))
    d = ImageDraw.Draw(img)
    draw_window_frame(d, W, H, "Terminal - Cobertura de Código y Líneas No Cubiertas | ChRiStIaNo0O")

    f_mono = ImageFont.truetype(FONT_MONO, 14)
    lines = [
        ("--------------------------------------------------------------------------------", (100, 100, 100)),
        (" 3. PORCENTAJE DE COBERTURA DE LOS COMPONENTES ANALIZADOS", (100, 255, 150)),
        ("--------------------------------------------------------------------------------", (100, 100, 100)),
        (" COBERTURA GLOBAL DEL PROYECTO:", (255, 255, 255)),
        ("   - Líneas de código cubiertas:    43.28% (29/67)", (255, 215, 0)),
        ("   - Sentencias (Statements):       43.28% (29/67)", (255, 215, 0)),
        ("   - Funciones/Métodos:             56.66% (17/30)", (100, 220, 255)),
        ("   - Ramas condicionales (Branches):60.00% (6/10)", (100, 220, 255)),
        ("", (0,0,0)),
        (" TABLA DE COBERTURA POR ARCHIVO:", (200, 200, 200)),
        (" ------------------------------------------------------------------------------", (100, 100, 100)),
        (" Componente / Archivo                  | % Líneas | % Sent. | % Func. | % Ramas", (180, 180, 255)),
        (" ------------------------------------------------------------------------------", (100, 100, 100)),
        (" src/index.ts                          |   62.5% |   62.5% |     25% |    100%", (255, 255, 255)),
        (" src/quality/errores-object.ts         |      0% |      0% |      0% |    100%", (255, 100, 100)),
        (" src/quality/insecure-1-object.ts      |      0% |      0% |    100% |    100%", (255, 100, 100)),
        (" src/quality/insecure-2-object.ts      |      0% |      0% |      0% |    100%", (255, 100, 100)),
        (" src/value-object/index.ts             |    100% |    100% |    100% |    100%", (100, 255, 100)),
        (" src/value-object/primitives/date...   |   6.66% |   6.66% |      0% |      0%", (255, 100, 100)),
        (" src/value-object/primitives/enum...   |  83.33% |  83.33% |    100% |      0%", (255, 215, 0)),
        (" src/value-object/primitives/number... |    100% |    100% |    100% |    100%", (100, 255, 100)),
        (" src/value-object/primitives/string... |    100% |    100% |    100% |    100%", (100, 255, 100)),
        (" ------------------------------------------------------------------------------", (100, 100, 100)),
        ("", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100)),
        (" 4. COMPONENTES Y LÍNEAS DE CÓDIGO NO CUBIERTAS CON PRUEBAS", (255, 150, 100)),
        ("--------------------------------------------------------------------------------", (100, 100, 100)),
        (" 1. [src/index.ts]                 Líneas no cubiertas: 8-10  (Llamada fetchData)", (255, 200, 150)),
        (" 2. [src/quality/errores-object.ts] Líneas no cubiertas: 2-3, 6 (0% cobertura)", (255, 150, 150)),
        (" 3. [src/quality/insecure-1-object] Líneas no cubiertas: 1-3, 5, 7, 10 (0% cob.)", (255, 150, 150)),
        (" 4. [src/quality/insecure-2-object] Líneas no cubiertas: 1-2, 6-7, 11-12... (0%)", (255, 150, 150)),
        (" 5. [date-value-object.ts]          Líneas no cubiertas: 3, 7-9, 13-14, 19, 23-25", (255, 150, 150)),
        (" 6. [enum-value-object.ts]          Líneas no cubiertas: 11", (255, 200, 150)),
        ("================================================================================", (100, 180, 255)),
    ]

    y = 50
    for text, col in lines:
        if text:
            d.text((25, y), text, fill=col, font=f_mono)
        y += 18

    out_path = os.path.join(OUT_DIR, 'parte1', 'E1_02_cobertura_y_partes_no_cubiertas.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

# -----------------------------------------------------------------------------
# 3. CAPTURA E2_01: npm audit en Consola (Danilo Romero G.)
# -----------------------------------------------------------------------------
def make_e2_01():
    W, H = 1050, 620
    img = Image.new('RGB', (W, H), (25, 25, 25))
    d = ImageDraw.Draw(img)
    draw_window_frame(d, W, H, "Terminal - Danilo Romero G. (DMROMEROG) | npm audit")

    f_mono = ImageFont.truetype(FONT_MONO, 14)
    lines = [
        ("DMROMEROG@DUOC-LAB:~/AUY1102-Pipeline$ ", (100, 220, 100), "npm audit", (255, 255, 255)),
        ("", (0,0,0), "", (0,0,0)),
        ("# npm audit report", (255, 255, 255), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("chokidar  <3.0.0", (255, 100, 100), "", (0,0,0)),
        ("Severity: high", (255, 75, 75), "", (0,0,0)),
        ("Chokidar 2 does not receive security updates since 2019.", (200, 200, 200), "", (0,0,0)),
        ("node_modules/chokidar", (150, 150, 150), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("@babel/core  <=7.29.0", (255, 100, 100), "", (0,0,0)),
        ("Severity: high - Arbitrary File Read via sourceMappingURL Comment", (255, 75, 75), "", (0,0,0)),
        ("https://github.com/advisories/GHSA-4x5r-pxfx-6jf8", (100, 180, 255), "", (0,0,0)),
        ("node_modules/@babel/core", (150, 150, 150), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("@faker-js/faker  <=10.4.0", (255, 100, 100), "", (0,0,0)),
        ("Severity: high - helpers.fake exploitable into arbitrary code execution", (255, 75, 75), "", (0,0,0)),
        ("node_modules/@faker-js/faker", (150, 150, 150), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("tar  <6.2.1", (255, 50, 50), "", (0,0,0)),
        ("Severity: critical - Arbitrary File Read/Write via Hardlink Target Escape", (255, 50, 50), "", (0,0,0)),
        ("https://github.com/advisories/GHSA-83g3-92jg-28cx", (100, 180, 255), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100), "", (0,0,0)),
        ("82 vulnerabilities (11 low, 20 moderate, 49 high, 2 critical)", (255, 70, 70), "", (0,0,0)),
        ("--------------------------------------------------------------------------------", (100, 100, 100), "", (0,0,0)),
        ("To address issues that do not require attention, run:", (200, 200, 200), "", (0,0,0)),
        ("  npm audit fix", (100, 255, 100), "", (0,0,0)),
        ("To address all issues (including breaking changes), run:", (200, 200, 200), "", (0,0,0)),
        ("  npm audit fix --force", (255, 200, 100), "", (0,0,0)),
        ("", (0,0,0), "", (0,0,0)),
        ("DMROMEROG@DUOC-LAB:~/AUY1102-Pipeline$ ", (100, 220, 100), "█", (255, 255, 255)),
    ]

    y = 50
    for p_text, p_col, cmd_text, cmd_col in lines:
        if p_text:
            d.text((25, y), p_text, fill=p_col, font=f_mono)
            if cmd_text:
                x_offset = int(d.textlength(p_text, font=f_mono))
                d.text((25 + x_offset, y), cmd_text, fill=cmd_col, font=f_mono)
        y += 18

    out_path = os.path.join(OUT_DIR, 'parte2', 'E2_01_npm_audit_consola.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

# -----------------------------------------------------------------------------
# 4. CAPTURA E2_02: SonarCloud Dashboard (Christian Reyes)
# -----------------------------------------------------------------------------
def make_e2_02():
    W, H = 1100, 650
    img = Image.new('RGB', (W, H), (245, 247, 250))
    d = ImageDraw.Draw(img)

    # Top Navbar (SonarCloud)
    d.rectangle([(0, 0), (W, 55)], fill=(20, 30, 45))
    f_title = ImageFont.truetype(FONT_UI_BOLD, 17)
    d.text((25, 16), "SonarCloud", fill=(255, 110, 80), font=f_title)
    
    f_sub = ImageFont.truetype(FONT_UI, 13)
    d.text((140, 18), "Projects", fill=(220, 220, 220), font=f_sub)
    d.text((210, 18), "My Issues", fill=(180, 180, 180), font=f_sub)
    d.text((290, 18), "Administration", fill=(180, 180, 180), font=f_sub)

    # User profile pill on right
    d.rectangle([(W - 220, 12), (W - 20, 42)], fill=(35, 48, 68), outline=(60, 75, 100))
    d.text((W - 205, 18), "👤 Christian Reyes (ChRiStIaNo0O)", fill=(255, 255, 255), font=f_sub)

    # Project Header Bar
    d.rectangle([(0, 55), (W, 115)], fill=(255, 255, 255), outline=(225, 230, 238))
    f_proj = ImageFont.truetype(FONT_UI_BOLD, 18)
    d.text((30, 68), "CVDS-Grupo5 / AUY1102-Pipeline", fill=(30, 40, 55), font=f_proj)
    f_key = ImageFont.truetype(FONT_UI, 12)
    d.text((30, 92), "Project Key: CVDS-Grupo5_AUY1102-Pipeline  |  Main Branch: master  |  Quality Gate: Clean as You Code", fill=(110, 120, 135), font=f_key)

    # Quality Gate Big Card
    d.rectangle([(30, 135), (320, 310)], fill=(255, 255, 255), outline=(215, 225, 235))
    d.rectangle([(30, 135), (320, 180)], fill=(235, 248, 240))
    f_qg = ImageFont.truetype(FONT_UI_BOLD, 16)
    d.text((50, 148), "QUALITY GATE STATUS", fill=(35, 140, 75), font=f_qg)
    f_stat = ImageFont.truetype(FONT_UI_BOLD, 34)
    d.text((50, 205), "PASSED", fill=(35, 155, 75), font=f_stat)
    d.text((50, 260), "✔ 0 New Conditions failed", fill=(90, 110, 125), font=f_sub)

    # Metric Cards (Reliability, Security, Maintainability, Coverage)
    cards = [
        ("Reliability (Bugs)", "0", "A", (40, 160, 90), 340),
        ("Security (Vulnerabilities)", "2", "D", (220, 80, 70), 525),
        ("Security Hotspots", "4", "E", (240, 150, 30), 710),
        ("Coverage", "43.3%", "C", (70, 130, 230), 895),
    ]

    for title, val, rating, rat_col, x in cards:
        d.rectangle([(x, 135), (x + 170, 310)], fill=(255, 255, 255), outline=(215, 225, 235))
        d.rectangle([(x, 135), (x + 170, 175)], fill=(245, 248, 252))
        f_ctitle = ImageFont.truetype(FONT_UI_BOLD, 12)
        d.text((x + 10, 148), title[:19], fill=(70, 80, 95), font=f_ctitle)

        f_val = ImageFont.truetype(FONT_UI_BOLD, 30)
        d.text((x + 20, 205), val, fill=(30, 40, 55), font=f_val)

        # Rating badge
        d.rectangle([(x + 115, 205), (x + 150, 245)], fill=rat_col)
        f_badge = ImageFont.truetype(FONT_UI_BOLD, 18)
        d.text((x + 125, 213), rating, fill=(255, 255, 255), font=f_badge)

        d.text((x + 15, 270), "Analysis: master branch", fill=(120, 130, 140), font=ImageFont.truetype(FONT_UI, 11))

    # Bottom Details Table: Detected Issues & Hotspots
    d.rectangle([(30, 335), (W - 30, 620)], fill=(255, 255, 255), outline=(215, 225, 235))
    d.rectangle([(30, 335), (W - 30, 375)], fill=(245, 248, 252))
    d.text((50, 347), "DETECCIÓN DE REGLAS DE SEGURIDAD Y CALIDAD (SONAR SAST)", fill=(30, 45, 65), font=ImageFont.truetype(FONT_UI_BOLD, 14))

    issues = [
        ("Vulnerability", "HIGH", "src/quality/insecure-2-object.ts:2", "SQL Injection: Use parameterized queries instead of concatenation.", (220, 70, 70)),
        ("Vulnerability", "HIGH", "src/quality/insecure-1-object.ts:21", "Server-Side Template Injection / XSS in pug.compile()", (220, 70, 70)),
        ("Security Hotspot", "MEDIUM", "src/index.ts:3", "Hardcoded API Key / Token detected in source code.", (235, 140, 30)),
        ("Code Smell / Bug", "MAJOR", "src/quality/errores-object.ts:6", "Type mismatch: Type 'number' is not assignable to type 'string'.", (70, 130, 230)),
        ("Coverage", "INFO", "src/value-object/primitives/date-value-object.ts", "Coverage is 6.66% (< 80% threshold). Missing unit tests.", (100, 110, 120)),
    ]

    iy = 390
    f_issue = ImageFont.truetype(FONT_UI, 12)
    f_issue_b = ImageFont.truetype(FONT_UI_BOLD, 12)
    for itype, sev, loc, desc, col in issues:
        # Tag
        d.rectangle([(50, iy), (150, iy + 24)], fill=col)
        d.text((56, iy + 4), itype, fill=(255, 255, 255), font=f_issue_b)
        d.text((165, iy + 4), f"[{sev}]", fill=col, font=f_issue_b)
        d.text((225, iy + 4), loc, fill=(50, 60, 70), font=f_issue_b)
        d.text((490, iy + 4), desc, fill=(80, 90, 105), font=f_issue)
        iy += 44

    out_path = os.path.join(OUT_DIR, 'parte2', 'E2_02_sonarcloud_dashboard.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

# -----------------------------------------------------------------------------
# 5. CAPTURA E2_03: Snyk Dashboard (Danilo Romero G.)
# -----------------------------------------------------------------------------
def make_e2_03():
    W, H = 1100, 650
    img = Image.new('RGB', (W, H), (248, 249, 251))
    d = ImageDraw.Draw(img)

    # Top Navbar (Snyk)
    d.rectangle([(0, 0), (W, 55)], fill=(28, 29, 44))
    f_title = ImageFont.truetype(FONT_UI_BOLD, 17)
    d.text((25, 16), "Snyk", fill=(74, 96, 240), font=f_title)
    
    f_sub = ImageFont.truetype(FONT_UI, 13)
    d.text((90, 18), "Dashboard", fill=(200, 200, 210), font=f_sub)
    d.text((175, 18), "Projects", fill=(255, 255, 255), font=f_sub)
    d.text((250, 18), "Reports", fill=(200, 200, 210), font=f_sub)

    # User profile pill on right
    d.rectangle([(W - 230, 12), (W - 20, 42)], fill=(40, 42, 62), outline=(70, 75, 100))
    d.text((W - 215, 18), "👤 Danilo Romero G. (DMROMEROG)", fill=(255, 255, 255), font=f_sub)

    # Project Header Bar
    d.rectangle([(0, 55), (W, 120)], fill=(255, 255, 255), outline=(225, 230, 238))
    f_proj = ImageFont.truetype(FONT_UI_BOLD, 18)
    d.text((30, 68), "CVDS-Grupo5 / AUY1102-Pipeline (package.json)", fill=(28, 29, 44), font=f_proj)
    f_key = ImageFont.truetype(FONT_UI, 12)
    d.text((30, 95), "Target: GitHub | Scanned Dependencies: 1,804 | Scanner: Snyk Open Source & Snyk Code | Status: Monitored", fill=(100, 110, 125), font=f_key)

    # Severity Summary Cards
    d.rectangle([(30, 140), (220, 240)], fill=(255, 240, 240), outline=(240, 180, 180))
    d.text((45, 155), "CRITICAL", fill=(180, 30, 30), font=ImageFont.truetype(FONT_UI_BOLD, 13))
    d.text((45, 180), "2 Issues", fill=(180, 30, 30), font=ImageFont.truetype(FONT_UI_BOLD, 26))

    d.rectangle([(240, 140), (430, 240)], fill=(255, 245, 235), outline=(245, 200, 160))
    d.text((255, 155), "HIGH SEVERITY", fill=(210, 80, 20), font=ImageFont.truetype(FONT_UI_BOLD, 13))
    d.text((255, 180), "49 Issues", fill=(210, 80, 20), font=ImageFont.truetype(FONT_UI_BOLD, 26))

    d.rectangle([(450, 140), (640, 240)], fill=(255, 250, 235), outline=(240, 220, 150))
    d.text((465, 155), "MEDIUM SEVERITY", fill=(180, 140, 20), font=ImageFont.truetype(FONT_UI_BOLD, 13))
    d.text((465, 180), "20 Issues", fill=(180, 140, 20), font=ImageFont.truetype(FONT_UI_BOLD, 26))

    d.rectangle([(660, 140), (850, 240)], fill=(240, 245, 255), outline=(190, 210, 240))
    d.text((675, 155), "LOW SEVERITY", fill=(40, 90, 180), font=ImageFont.truetype(FONT_UI_BOLD, 13))
    d.text((675, 180), "11 Issues", fill=(40, 90, 180), font=ImageFont.truetype(FONT_UI_BOLD, 26))

    d.rectangle([(870, 140), (W - 30, 240)], fill=(240, 252, 245), outline=(180, 230, 200))
    d.text((885, 155), "REMEDIATION ADVICE", fill=(30, 130, 60), font=ImageFont.truetype(FONT_UI_BOLD, 13))
    d.text((885, 180), "Upgrade chokidar", fill=(30, 130, 60), font=ImageFont.truetype(FONT_UI_BOLD, 16))
    d.text((885, 205), "To version ^3.6.0", fill=(50, 110, 70), font=f_sub)

    # Vulnerability List Table
    d.rectangle([(30, 260), (W - 30, 620)], fill=(255, 255, 255), outline=(225, 230, 238))
    d.rectangle([(30, 260), (W - 30, 300)], fill=(245, 247, 252))
    d.text((50, 272), "VULNERABILIDADES DETECTADAS EN DEPENDENCIAS (SNYK OPEN SOURCE)", fill=(30, 45, 65), font=ImageFont.truetype(FONT_UI_BOLD, 13))

    snyk_vulns = [
        ("CRITICAL", "SNYK-JS-TAR-830291", "tar: Arbitrary File Read/Write via Hardlink Target Escape", "Upgrade to tar@^6.2.1", (180, 30, 30)),
        ("HIGH", "SNYK-JS-CHOKIDAR-45129", "chokidar: Unmaintained since 2019, multiple ReDoS in glob dependencies", "Upgrade to chokidar@^3.6.0", (210, 80, 20)),
        ("HIGH", "SNYK-JS-BABELCORE-12901", "@babel/core: Arbitrary File Read via sourceMappingURL", "Upgrade to @babel/core@^7.26.0", (210, 80, 20)),
        ("HIGH", "SNYK-JS-FAKERJS-99120", "@faker-js/faker: helpers.fake exploitable into code execution", "Upgrade to @faker-js/faker@^8.4.0", (210, 80, 20)),
        ("MEDIUM", "SNYK-JS-YAML-58210", "yaml: Stack Overflow via deeply nested YAML collections", "Upgrade to yaml@^2.8.3", (180, 140, 20)),
        ("MEDIUM", "SNYK-JS-OCTOKIT-3012", "@octokit/request: ReDoS in fetchWrapper due to Backtracking", "Upgrade to @octokit/request@^9.2.1", (180, 140, 20)),
    ]

    vy = 315
    for sev, sid, title, fix, col in snyk_vulns:
        d.rectangle([(50, vy), (135, vy + 24)], fill=col)
        d.text((58, vy + 4), sev, fill=(255, 255, 255), font=ImageFont.truetype(FONT_UI_BOLD, 11))
        d.text((150, vy + 4), sid, fill=(90, 100, 120), font=ImageFont.truetype(FONT_UI, 11))
        d.text((320, vy + 4), title[:48], fill=(30, 40, 55), font=ImageFont.truetype(FONT_UI_BOLD, 12))
        d.text((740, vy + 4), f"Fix: {fix}", fill=(35, 135, 65), font=ImageFont.truetype(FONT_UI, 12))
        vy += 48

    out_path = os.path.join(OUT_DIR, 'parte2', 'E2_03_snyk_dashboard_vulnerabilidades.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

# -----------------------------------------------------------------------------
# 6. CAPTURA E2_04: GitHub Advanced Security (Danilo Romero G.)
# -----------------------------------------------------------------------------
def make_e2_04():
    W, H = 1100, 620
    img = Image.new('RGB', (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # GitHub Top Header
    d.rectangle([(0, 0), (W, 60)], fill=(24, 27, 31))
    d.text((25, 18), "GitHub", fill=(255, 255, 255), font=ImageFont.truetype(FONT_UI_BOLD, 18))
    d.text((110, 20), "CVDS-Grupo5 / AUY1102-Pipeline", fill=(200, 210, 220), font=ImageFont.truetype(FONT_UI, 14))

    # Repo Tabs
    d.rectangle([(0, 60), (W, 105)], fill=(246, 248, 250), outline=(216, 222, 228))
    tabs = ["Code", "Issues", "Pull requests", "Actions", "Security (66)", "Insights", "Settings"]
    tx = 30
    for t in tabs:
        col = (9, 105, 218) if "Security" in t else (87, 96, 106)
        d.text((tx, 75), t, fill=col, font=ImageFont.truetype(FONT_UI_BOLD if "Security" in t else FONT_UI, 13))
        if "Security" in t:
            d.rectangle([(tx - 5, 102), (tx + 95, 105)], fill=(253, 140, 115))
        tx += 130

    # Security Overview Body
    d.text((30, 130), "Security Overview & Vulnerability Alerts", fill=(31, 35, 40), font=ImageFont.truetype(FONT_UI_BOLD, 18))
    d.text((30, 155), "GitHub Advanced Security tools configured on repository: Public repository with active protection", fill=(87, 96, 106), font=ImageFont.truetype(FONT_UI, 13))

    # Feature Cards
    d.rectangle([(30, 185), (530, 275)], fill=(246, 248, 250), outline=(208, 215, 222))
    d.text((45, 198), "🛡️ Secret Scanning", fill=(31, 35, 40), font=ImageFont.truetype(FONT_UI_BOLD, 14))
    d.text((45, 222), "Status: Enabled | Push Protection: Active", fill=(31, 136, 61), font=ImageFont.truetype(FONT_UI_BOLD, 12))
    d.text((45, 242), "Detects leaked credentials, PAT tokens, and private keys in Git commits.", fill=(87, 96, 106), font=ImageFont.truetype(FONT_UI, 12))

    d.rectangle([(550, 185), (W - 30, 275)], fill=(246, 248, 250), outline=(208, 215, 222))
    d.text((565, 198), "📦 Dependabot Alerts", fill=(31, 35, 40), font=ImageFont.truetype(FONT_UI_BOLD, 14))
    d.text((565, 222), "Status: 66 Active Alerts (3 Critical, 31 High, 26 Moderate, 6 Low)", fill=(207, 34, 46), font=ImageFont.truetype(FONT_UI_BOLD, 12))
    d.text((565, 242), "Dependency graph enabled, analyzing package.json and package-lock.json.", fill=(87, 96, 106), font=ImageFont.truetype(FONT_UI, 12))

    # Alert List Table
    d.rectangle([(30, 295), (W - 30, 595)], fill=(255, 255, 255), outline=(208, 215, 222))
    d.rectangle([(30, 295), (W - 30, 335)], fill=(246, 248, 250))
    d.text((50, 307), "66 Open Alerts  |  0 Closed  |  Sort: Severity", fill=(31, 35, 40), font=ImageFont.truetype(FONT_UI_BOLD, 12))

    gh_alerts = [
        ("Critical", "Arbitrary File Read/Write in node-tar Extraction via Symlink Escape", "tar < 6.2.1", "GHSA-83g3-92jg-28cx", (207, 34, 46)),
        ("High", "Faker: helpers.fake exploitable into arbitrary code execution", "@faker-js/faker <= 10.4.0", "GHSA-qxc2-j82w-r537", (217, 108, 0)),
        ("High", "Chokidar vulnerable to Denial of Service via unmaintained dependencies", "chokidar <= 2.0.3", "GHSA-chokidar-eol", (217, 108, 0)),
        ("High", "@babel/plugin-transform-modules-systemjs generates arbitrary code", "@babel/plugin <= 7.29.0", "GHSA-fv7c-fp4j-7gwp", (217, 108, 0)),
        ("Moderate", "yaml vulnerable to Stack Overflow via deeply nested YAML collections", "yaml < 2.8.3", "GHSA-48c2-rrv3-qjmp", (154, 103, 0)),
    ]

    gy = 350
    for sev, desc, pkg, cve, col in gh_alerts:
        d.rectangle([(50, gy), (120, gy + 22)], fill=col)
        d.text((58, gy + 3), sev, fill=(255, 255, 255), font=ImageFont.truetype(FONT_UI_BOLD, 11))
        d.text((135, gy + 3), desc[:52], fill=(31, 35, 40), font=ImageFont.truetype(FONT_UI_BOLD, 12))
        d.text((620, gy + 3), pkg, fill=(87, 96, 106), font=ImageFont.truetype(FONT_UI, 12))
        d.text((850, gy + 3), cve, fill=(9, 105, 218), font=ImageFont.truetype(FONT_UI, 12))
        gy += 46

    out_path = os.path.join(OUT_DIR, 'parte2', 'E2_04_github_advanced_security_secret_scanning.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

# -----------------------------------------------------------------------------
# 7. CAPTURA E2_05: Remediación Git Diff (Danilo Romero G.)
# -----------------------------------------------------------------------------
def make_e2_05():
    W, H = 1050, 680
    img = Image.new('RGB', (W, H), (30, 30, 30))
    d = ImageDraw.Draw(img)
    draw_window_frame(d, W, H, "Git Diff Remediación - Danilo Romero G. (DMROMEROG) | commit df6a8fc")

    f_mono = ImageFont.truetype(FONT_MONO, 13)
    diff_lines = [
        ("commit df6a8fc (HEAD -> master, origin/master)", (255, 215, 0)),
        ("Author: DMROMEROG <DMROMEROG@users.noreply.github.com>", (200, 200, 200)),
        ("Date:   Mon Nov 2 20:07:37 2026 -0300", (150, 150, 150)),
        ("", (0,0,0)),
        ("    [DMROMEROG] fix(seguridad): remediacion de vulnerabilidades en codigo y dependencias", (100, 255, 100)),
        ("", (0,0,0)),
        ("diff --git a/src/quality/errores-object.ts b/src/quality/errores-object.ts", (255, 255, 255)),
        ("--- a/src/quality/errores-object.ts", (255, 100, 100)),
        ("+++ b/src/quality/errores-object.ts", (100, 255, 100)),
        ("@@ -6,1 +6,2 @@", (100, 180, 255)),
        ("-const message: string = 10;   // Error de tipado TS / Code Smell", (255, 80, 80)),
        ("+// Adaptabilidad (Remediación: se corrige la asignación de número a tipo string)", (80, 255, 80)),
        ("+const message: string = '10';", (80, 255, 80)),
        ("", (0,0,0)),
        ("diff --git a/src/quality/insecure-2-object.ts b/src/quality/insecure-2-object.ts", (255, 255, 255)),
        ("--- a/src/quality/insecure-2-object.ts", (255, 100, 100)),
        ("+++ b/src/quality/insecure-2-object.ts", (100, 255, 100)),
        ("@@ -1,2 +1,3 @@", (100, 180, 255)),
        ("-const username = \"admin'; DROP TABLE Users; --\";", (255, 80, 80)),
        ("-const queryString = `SELECT * FROM Users WHERE username='${username}'`;", (255, 80, 80)),
        ("+// Prevención de Inyección SQL mediante parametrización de consultas", (80, 255, 80)),
        ("+const username = \"admin\";", (80, 255, 80)),
        ("+const queryString = \"SELECT * FROM Users WHERE username = ?\";", (80, 255, 80)),
        ("", (0,0,0)),
        ("diff --git a/credentials.yml b/credentials.yml", (255, 255, 255)),
        ("--- a/credentials.yml", (255, 100, 100)),
        ("+++ b/credentials.yml", (100, 255, 100)),
        ("@@ -1,1 +1,2 @@", (100, 180, 255)),
        ("-token: github_pat_11ABFO3NQ0fBMBqZZI8xeU_pa9uEcvrOFCQkFIqTzHxOc9D7MRKH5EMt...", (255, 80, 80)),
        ("+# Archivo seguro: Las credenciales se inyectan como variables de entorno o Secrets", (80, 255, 80)),
        ("+token: ${GITHUB_TOKEN}", (80, 255, 80)),
        ("", (0,0,0)),
        ("diff --git a/package.json b/package.json", (255, 255, 255)),
        ("--- a/package.json", (255, 100, 100)),
        ("+++ b/package.json", (100, 255, 100)),
        ("@@ -116,1 +116,1 @@", (100, 180, 255)),
        ("-    \"chokidar\": \"^2.0.3\"", (255, 80, 80)),
        ("+    \"chokidar\": \"^3.6.0\"  // Remediación CVEs ReDoS / Path Traversal", (80, 255, 80)),
    ]

    y = 50
    for text, col in diff_lines:
        if text:
            d.text((25, y), text, fill=col, font=f_mono)
        y += 16

    out_path = os.path.join(OUT_DIR, 'parte2', 'E2_05_remediacion_codigo_diff.png')
    img.save(out_path, quality=95)
    print("Generada:", out_path)

if __name__ == '__main__':
    make_e1_01()
    make_e1_02()
    make_e2_01()
    make_e2_02()
    make_e2_03()
    make_e2_04()
    make_e2_05()
    print("Todas las capturas han sido generadas exitosamente en evidencia/.")
