# SigmaPredictor TCDS v1.1.0

[![Descargar ZIP](https://img.shields.io/badge/Descargar-ZIP%20v1.1.0-111111.svg?logo=download)](SigmaPredictor_TCDS_v1.1.0.zip)
[![DOI Zenodo](https://img.shields.io/badge/DOI-Zenodo-1182c3.svg?logo=zenodo)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Dual--Proprietary-blueviolet?style=for-the-badge&logo=balance-scale)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-darkgreen?style=for-the-badge&logo=github)](https://github.com/geozunac3536-jpg/Las-Sigma-Metrics)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=githubactions)](https://github.com/geozunac3536-jpg/Las-Sigma-Metrics/actions)
[![Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-121212?style=for-the-badge&logo=github)](https://geozunac3536-jpg.github.io/Las-Sigma-Metrics/)

<p align="center">
  <img src="https://copilot.microsoft.com/th/id/BCO.7bcb8109-52a6-4b5c-9604-c02d595e1d5b.png" alt="Sigma-Metrics Banner" width="100%" />
</p>

---

## 👤 Autor / Author
- **Nombre / Name:** Genaro Carrasco Ozuna
- **Rol / Role:** Arquitecto de documentación científica modular (TCDS Project)
- **Ubicación / Location:** México (Ecatepec de Morelos, Puebla, Orizaba)
- **Intereses / Interests:** Filosofía de la ciencia, causalidad, reproducibilidad, open science, metrología aplicada

---

## 📋 Tabla de contenidos
- [1. Propósito](#1-propósito)
- [2. Características](#2-características)
- [3. Requisitos del Sistema](#3-requisitos-del-sistema)
- [4. Instalación](#4-instalación)
  - [4.1 Termux (Android)](#41-termux-android)
  - [4.2 PC (Linux/macOS/WSL)](#42-pc-linuxmacoswsl)
- [5. Uso operativo](#5-uso-operativo)
  - [5.1 Reporte con tus datos](#51-reporte-con-tus-datos)
  - [5.2 Estimación automática de banda y f₀](#52-estimación-automática-de-banda-y-f₀)
  - [5.3 Ejecución de demostración](#53-ejecución-de-demostración)
- [6. Formatos de Datos](#6-formatos-de-datos)
- [7. Fundamentos Teóricos: Σ-metrics](#7-fundamentos-teóricos-σ-metrics)
- [8. Validación y Reproducibilidad](#8-validación-y-reproducibilidad)
- [9. Estructura del Repositorio](#9-estructura-del-repositorio)
- [10. Solución de Problemas](#10-solución-de-problemas)
- [11. Licencias](#11-licencias)
- [12. Citación](#12-citación)

---

## 1. Propósito
**SigmaPredictor_TCDS** proporciona un **pipeline computacional ligero y robusto** diseñado para la extracción y análisis de **Métricas Sigma (Σ-metrics)** en series temporales. Optimizado para entornos de bajos recursos (como dispositivos móviles vía Termux) y estaciones de trabajo (PC), facilita el cálculo de indicadores críticos de coherencia y sincronización:

- **LI (Locking Index):** Índice de bloqueo de fase.
- **R (Pearson Correlation):** Correlación con osciladores armónicos acoplados.
- **RMSE_SL:** Error cuadrático medio del ajuste de fase.
- **κΣ (Kappa Sigma):** Estimador de concentración circular derivado.

El diseño prioriza la **reproducibilidad científica** y la **auditoría forense de datos**, garantizando trazabilidad total desde la entrada cruda hasta el reporte analítico.

---

## 2. Características
- **Portabilidad Extrema:** Dependencias mínimas (Python + NumPy standard library). Ejecutable en cualquier entorno POSIX.
- **Trazabilidad Forense:** Generación automática de manifiestos `.meta.json` incluyendo hash SHA-256 de los datos de entrada y configuración de parámetros para auditoría.
- **Despliegue Rápido:** Scripts `bash` (wrappers) preconfigurados para operación inmediata en campo (`sigma_report.sh`, `auto_band.sh`).
- **Verificación Integrada:** Módulo de demostración `run_example.sh` para validar la integridad del cálculo con datos sintéticos controlados.

---

## 3. Requisitos del Sistema
- **Sistema Operativo:** Android (vía Termux), Linux, macOS, Windows (WSL).
- **Python:** Versión 3.6 o superior.
- **Librerías Python:** `numpy` (única dependencia externa estricta).
- **Herramientas CLI:** `bash`, `git`, `unzip`.

---

## 4. Instalación

### 4.1 Termux (Android)
Transforma tu dispositivo móvil en una estación de análisis:

```bash
# 1. Actualizar repositorios y sistema
pkg update -y && pkg upgrade -y

# 2. Instalar entorno Python y herramientas
pkg install -y python python-numpy git unzip

# 3. Configurar acceso al almacenamiento
termux-setup-storage

# 4. Clonar repositorio
git clone [https://github.com/geozunac3536-jpg/Las-Sigma-Metrics.git](https://github.com/geozunac3536-jpg/Las-Sigma-Metrics.git) ~/SigmaPredictor_TCDS

# 5. Acceder al directorio
cd ~/SigmaPredictor_TCDS
