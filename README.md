##Sigma-Metrics Package

Herramientas para evaluar coherencia causal (Q-driven) frente a ruido entrópico (φ-driven), 
basadas en el canon TCDS y desarrolladas por Genaro Carrasco Ozuna.

Tools to evaluate causal coherence (Q-driven) versus entropic noise (φ-driven), 
based on the TCDS canon and developed by Genaro Carrasco Ozuna.

---

👤 Autor / Author

- Nombre / Name: Genaro Carrasco Ozuna  
- Rol / Role: Arquitecto de documentación científica modular (TCDS Project)  
- Ubicación / Location: México (Ecatepec de Morelos, Puebla, Orizaba)  
- Intereses / Interests: Filosofía de la ciencia, causalidad, reproducibilidad, open science, metrología aplicada  

---

📦 Instalación / Installation

Clona el repositorio:

`bash
git clone https://github.com/geozunac3536-jpg/Las-Sigma-Metrics.git
cd Las-Sigma-Metrics
`

(Opcional: instala dependencias si usas Python o Node.js según requirements.txt o package.json).

---

🚀 Uso rápido / Quick Start

Python Example

`python
from sigma_metrics import coherence, rmse

signal_q = [0.1, 0.2, 0.3, 0.4]
signal_phi = [0.1, -0.1, 0.5, 0.2]

print("RMSE:", rmse(signalq, signalphi))
print("Coherencia:", coherence(signalq, signalphi))
`

Web Example (Plotly.js)

`html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
  const causal = [0.1, 0.2, 0.3, 0.4];
  const ruido = [0.1, -0.1, 0.5, 0.2];
  // Visualización Σ-Metrics
</script>
`

---

📖 Definiciones de métricas Σ / Σ Metrics Definitions

- RMSE (Root Mean Square Error):

\[
RMSE = \sqrt{\frac{1}{n} \sum{i=1}^{n} (Qi - \phi_i)^2}
\]

- Coeficiente de coherencia κΣ:

\[
\kappa{\Sigma} = \frac{\text{Cov}(Q, \phi)}{\sigmaQ \cdot \sigma_\phi}
\]

- Índice de linealidad LI:

\[
LI = \frac{\sum (Qi \cdot \phii)}{\sum Q_i^2}
\]

- R (correlación causal):

\[
R = \frac{\sum (Qi - \bar{Q})(\phii - \bar{\phi})}{\sqrt{\sum (Qi - \bar{Q})^2 \cdot \sum (\phii - \bar{\phi})^2}}
\]

---

📊 Ejemplos interactivos / Interactive Examples

- Demo en GitHub Pages  
- [Firebase Hosting Demo] (pendiente de despliegue)  

---

🧭 Roadmap

- [ ] Integración con Firebase Hosting para demos interactivos.  
- [ ] API REST para consultas Σ-Metrics.  
- [ ] Dashboard de coherencia causal.  
- [ ] Traducción completa de documentación (ES/EN).  

---

⚖️ Licencia / License

MIT / Propietaria dual (para despliegues industriales).  
MIT / Dual proprietary license (for industrial deployments).
`

---
