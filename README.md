<!-- Dark header -->
<div align="center" style="background:#0d0f14;padding:28px 16px;border-radius:16px;border:1px solid #1b1f2a">
  <h1 style="color:#e6edf3;margin:0;font-size:34px;line-height:1.2">Las Sigma Metrics — Software Metrológico Σ (TCDS)</h1>
  <p style="color:#9fb1c7;margin:8px 0 0">Pipeline mínimo, auditable y reproducible para LI, R, RMSE_SL y κΣ en series temporales.<br>Probado en Android/Termux y PC con Python+NumPy.</p>
  <p>
    <a href="LICENSES/LICENSE-MIT.txt"><img alt="MIT" src="https://img.shields.io/badge/License-MIT-0b84fe.svg"></a>
    <a href="LICENSES/LICENSE-CC-BY-4.0.txt"><img alt="CC BY 4.0" src="https://img.shields.io/badge/Docs-CC%20BY%204.0-ef7d00.svg"></a>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.12+-3776AB.svg">
    <img alt="NumPy" src="https://img.shields.io/badge/NumPy-2.x-013243.svg">
  </p>
  <p>
    <!-- Cambia el enlace al DOI cuando publiques en Zenodo -->
    <a href="SigmaPredictor_TCDS_v1.1.0.zip"><img alt="Descargar ZIP" src="https://img.shields.io/badge/Descargar-ZIP%20v1.1.0-111111.svg?logo=download"></a>
    <a href="https://doi.org/10.5281/zenodo.XXXXXXX"><img alt="DOI Zenodo" src="https://img.shields.io/badge/DOI-Zenodo-1182c3.svg?logo=zenodo"></a>
  </p>
</div>

---# 🌑 Sigma-Metrics Package

Herramientas para evaluar coherencia causal (Q-driven) frente a ruido entrópico (φ-driven),  
basadas en el canon TCDS y desarrolladas por **Genaro Carrasco Ozuna**.

Tools to evaluate causal coherence (Q-driven) versus entropic noise (φ-driven),  
based on the TCDS canon and developed by **Genaro Carrasco Ozuna**.

---

## 🏷️ Badges

![License](https://img.shields.io/badge/License-MIT%20%2F%20Dual--Proprietary-blueviolet?style=for-the-badge&logo=balance-scale)  
![Status](https://img.shields.io/badge/Status-Active-darkgreen?style=for-the-badge&logo=github)  
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=githubactions)  
![Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-121212?style=for-the-badge&logo=github)

---

## 👤 Autor / Author
- **Nombre / Name:** Genaro Carrasco Ozuna  
- **Rol / Role:** Arquitecto de documentación científica modular (TCDS Project)  
- **Ubicación / Location:** México (Ecatepec de Morelos, Puebla, Orizaba)  
- **Intereses / Interests:** Filosofía de la ciencia, causalidad, reproducibilidad, open science, metrología aplicada  

---

## 📦 Instalación / Installation

```bash
git clone https://github.com/geozunac3536-jpg/Las-Sigma-Metrics.git
cd Las-Sigma-Metrics<p align="center">
  <img src="https://copilot.microsoft.com/th/id/BCO.7bcb8109-52a6-4b5c-9604-c02d595e1d5b.png" alt="Sigma-Metrics Banner" width="100%" />
</p>

## Tabla de contenidos
- [1. Propósito](#1-propósito)
- [2. Características](#2-características)
- [3. Instalación rápida](#3-instalación-rápida)
  - [3.1 Termux (Android)](#31-termux-android)
  - [3.2 PC (Linux/macOS/WSL)](#32-pc-linuxmacoswsl)
- [4. Uso operativo](#4-uso-operativo)
  - [4.1 Reporte con tus datos](#41-reporte-con-tus-datos)
  - [4.2 Estimación automática de banda y f₀](#42-estimación-automática-de-banda-y-f₀)
  - [4.3 Ejecución de demostración](#43-ejecución-de-demostración)
- [5. Formatos](#5-formatos)
  - [5.1 CSV de entrada](#51-csv-de-entrada)
  - [5.2 JSON de salida](#52-json-de-salida)
- [6. Definiciones de Σ-metrics](#6-definiciones-de-σmetrics)
- [7. Flujo de validación y reproducibilidad](#7-flujo-de-validación-y-reproducibilidad)
- [8. Estructura del paquete](#8-estructura-del-paquete)
- [9. Solución de problemas](#9-solución-de-problemas)
- [10. Rendimiento y buenas prácticas](#10-rendimiento-y-buenas-prácticas)
- [11. Licencias](#11-licencias)
- [12. Cita y autoría](#12-cita-y-autoría)
- [13. Changelog](#13-changelog)
- [14. Roadmap](#14-roadmap)

---

## 1. Propósito
Este repositorio entrega un **pipeline mínimo**, compatible con **Android/Termux** y **PC**, para calcular **Σ-metrics** sobre series temporales:
- **LI**: índice de bloqueo de fase.
- **R**: correlación de Pearson con el seno bloqueado.
- **RMSE_SL**: error de ajuste senoidal bloqueado.
- **κΣ**: concentración circular aproximada a partir de \(\bar R\).

El foco es **reproducibilidad** y **auditoría**: archivos de entrada y salida trazables, parámetros explícitos y scripts simples.

---

## 2. Características
- **Portátil**: sin dependencias pesadas. Solo `python` y `numpy`.
- **Trazabilidad**: se genera `.meta.json` con SHA-256 del CSV y parámetros usados.
- **Operativo**: wrappers para uso inmediato en campo: `sigma_report.sh` y `auto_band.sh`.
- **Demostración**: `run_example.sh` crea datos sintéticos y produce métricas esperadas.

---

## 3. Instalación rápida

### 3.1 Termux (Android)
```bash
pkg update -y && pkg upgrade -y
pkg install -y python python-numpy
termux-setup-storage

# Copia el ZIP a tu $HOME y descomprímelo
cp ~/storage/downloads/SigmaPredictor_TCDS_v1.1.0.zip ~
unzip ~/SigmaPredictor_TCDS_v1.1.0.zip -d ~
cd ~/SigmaPredictor_TCDS
````

### 3.2 PC (Linux/macOS/WSL)

```bash
python -m pip install --upgrade pip
python -m pip install numpy

# (Opcional) Clona o descomprime el paquete
cd SigmaPredictor_TCDS
```

---

## 4. Uso operativo

### 4.1 Reporte con tus datos

Asumiendo un CSV en Descargas con **t** y **s** o solo **s**:

```bash
bash ~/SigmaPredictor_TCDS/sigma_report.sh \
  --in ~/storage/downloads/tus_datos.csv \
  --fs 100 \
  --band 0.98 1.02 \
  --fdrive 1.00 \
  --win 20
```

Salida:

* `outputs/metrics_YYYYMMDD_HHMMSS.json`
* `outputs/metrics_YYYYMMDD_HHMMSS.meta.json` (SHA-256 + parámetros)
* Copia automática a `~/storage/downloads/`

### 4.2 Estimación automática de banda y f₀

```bash
bash ~/SigmaPredictor_TCDS/auto_band.sh \
  --in ~/storage/downloads/tus_datos.csv \
  --fs 100 \
  --pct 1.0 \
  --win 20
```

`auto_band.sh` estima el pico espectral (f_0) en `[fmin,fmax]` por defecto `[0.5, 5.0]` Hz y crea la banda ([f_0(1-%/100), f_0(1+%/100)]).

### 4.3 Ejecución de demostración

```bash
cd ~/SigmaPredictor_TCDS
bash run_example.sh
# genera data/sample_seismic.csv y outputs/metrics_sample.json
```

---

## 5. Formatos

### 5.1 CSV de entrada

* Con tiempo:

  ```
  t,s
  0.000000,0.19866933
  0.020000,0.21491507
  ...
  ```
* Solo señal:

  ```
  s
  0.19866933
  0.21491507
  ...
  ```

### 5.2 JSON de salida

```json
{
  "input": "data/sample_seismic.csv",
  "fs_Hz": 50.0,
  "band_Hz": [0.95, 1.05],
  "fdrive_Hz": 1.0,
  "N": 15000,
  "metrics": {
    "R": 0.74,
    "LI": 0.99,
    "RMSE_SL": 0.05,
    "kappa_sigma": 400.0
  },
  "estimates": {
    "amp_opt": 1.00,
    "phi0_opt_rad": 1.14
  },
  "notes": "Hilbert FFT; filtro rectangular; NumPy-only."
}
```

---

## 6. Definiciones de Σ-metrics

* **LI** (índice de locking de fase):
  [
  \mathrm{LI}=\left\lvert \frac{1}{N}\sum_{i=1}^{N}e^{,\mathrm{i},\Delta\phi_i}\right\rvert,\quad 0\le \mathrm{LI}\le 1
  ]
* **R** (correlación con seno bloqueado):
  [
  R=\frac{\sum_i (y_i-\bar y)(\hat y_i-\bar{\hat y})}{\sqrt{\sum_i (y_i-\bar y)^2\sum_i (\hat y_i-\bar{\hat y})^2}}
  ]
* **RMSE_SL**:
  [
  \mathrm{RMSE_SL}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat y_i)^2}
  ]
* **κΣ** (aprox. estándar por (\bar R)):
  [
  \kappa_\Sigma \approx
  \begin{cases}
  2\bar R+\bar R^3+\tfrac{5}{6}\bar R^5, & \bar R<0.53[4pt]
  -0.4+1.39\bar R+\dfrac{0.43}{1-\bar R}, & 0.53\le \bar R<0.85[6pt]
  \dfrac{1}{\bar R^3-4\bar R^2+3\bar R}, & \bar R\ge 0.85
  \end{cases}
  ]

---

## 7. Flujo de validación y reproducibilidad

1. **Registrar datos**: guarda el CSV de entrada.
2. **Ejecutar reporte**: `sigma_report.sh` con parámetros explícitos.
3. **Verificar trazabilidad**: usa el `.meta.json` para SHA-256 y parámetros.
4. **Publicar artefactos**: CSV + JSON + META en Zenodo/OSF (o anexo del paper).
5. **Comparar contra baseline**: métricas esperadas por dataset y banda.
6. **Reproducir por terceros**: instrucciones copiables en el README.

---

## 8. Estructura del paquete

```
SigmaPredictor_TCDS/
  compute_sigma_metrics.py
  generate_sample.py
  run_example.sh
  sigma_report.sh
  auto_band.sh
  data/sample_seismic.csv
  outputs/
  README.md
  CITATION.cff
  LICENSES/LICENSE-MIT.txt
  LICENSES/LICENSE-CC-BY-4.0.txt
  zenodo.json
  MANIFEST.txt
```

---

## 9. Solución de problemas

* **Termux: “Installing pip is forbidden”**
  No uses `pip install --upgrade pip` en Termux. Ya empaquetamos `python-numpy`.
* **Permisos de almacenamiento**
  Ejecuta `termux-setup-storage` y usa rutas `~/storage/downloads/`.
* **“FileNotFoundError: tus_datos.csv”**
  Verifica la ruta exacta: `--in ~/storage/downloads/tus_datos.csv`.
* **Resultados atípicos**
  Ajusta banda y ventana: `--band` más estrecha y `--win` ≥ 20 s suelen estabilizar LI y κΣ.

---

## 10. Rendimiento y buenas prácticas

* **Pre-filtrado**: elimina DC y spikes antes del análisis si tu sensor los introduce.
* **Ventanas**: usa `--win` proporcional a varias decenas de ciclos a (f_0).
* **Barridos**: evalúa varias bandas 0.5–5 Hz si desconoces (f_0).
* **Reportes**: conserva CSV, JSON, META y anota condiciones de adquisición.

---

## 11. Licencias

* **Código**: MIT → `LICENSES/LICENSE-MIT.txt`
* **Documentación**: CC BY 4.0 → `LICENSES/LICENSE-CC-BY-4.0.txt`

---

## 12. Cita y autoría

**Carrasco Ozuna, Genaro.** *SigmaPredictor_TCDS: Σ-metrics reproducibles en Termux (Android)*. Zenodo, **DOI:** *(pendiente)*.
**ORCID:** 0009-0005-6358-9910 — **Afiliación:** Proyecto TCDS / Motor Sincrónico de Luz (MSL), México.

Archivo de citación: `CITATION.cff`.

---

## 13. Changelog

* **v1.1.0**

  * Wrapper `auto_band.sh` para estimación de (f_0) y banda ±pct.
  * `.meta.json` con SHA-256 del CSV y parámetros.
  * README oscuro con Quick Start y definiciones formales.

---

## 14. Roadmap

* Integrar tests unitarios para validación de fases.
* Exportar gráficos rápidos (PSD, espectro de fase) sin dependencias pesadas.
* Paquete PyPI opcional para entorno PC.

```
```
