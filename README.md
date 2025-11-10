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

---

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
