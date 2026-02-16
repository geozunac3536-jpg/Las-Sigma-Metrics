"""
Sigma Metrics Engine
--------------------
Core implementation of coherence metrics (R, LI, RMSE, kappaSigma)
with Entropic Validation (ΔH) and E-Veto classification.

Designed for research and experimental signal analysis.
Author: Your Name
License: MIT
"""

import numpy as np
from scipy.signal import butter, filtfilt, hilbert


# ============================================================
# Signal Processing
# ============================================================

def bandpass(x, fs, f1, f2, order=4):
    nyq = fs / 2.0
    b, a = butter(order, [f1/nyq, f2/nyq], btype='band')
    return filtfilt(b, a, x)


def analytic_phase(x):
    return np.unwrap(np.angle(hilbert(x)))


def envelope(x):
    return np.abs(hilbert(x))


# ============================================================
# Core Metrics
# ============================================================

def order_parameter(dphi):
    z = np.exp(1j*(dphi - np.mean(dphi)))
    return float(np.abs(np.mean(z)))


def plv(ph_sig, ph_drv):
    return float(np.abs(np.mean(np.exp(1j*(ph_sig - ph_drv)))))


def envelope_rmse(x, y):
    ex = envelope(x)
    ey = envelope(y)

    ex = (ex - ex.mean()) / (ex.std() + 1e-9)
    ey = (ey - ey.mean()) / (ey.std() + 1e-9)

    return float(np.sqrt(np.mean((ex - ey)**2)))


def kappa_sigma(dphi):
    var = np.var(np.diff(dphi))
    return float(1.0 / (var + 1e-6))


# ============================================================
# Entropy & Validation
# ============================================================

def shannon_entropy(x, bins=64):
    hist, _ = np.histogram(x, bins=bins, density=True)
    hist = hist[hist > 0]
    return -np.sum(hist * np.log(hist))


def delta_entropy(x_window):
    h1 = shannon_entropy(x_window[:-1])
    h2 = shannon_entropy(x_window[1:])
    return float(h2 - h1)


def e_veto(R, LI, dH, R_th=0.95, LI_th=0.9, dH_th=-0.2):
    """
    Entropic validation rule:
    High coherence is valid ONLY if entropy decreases.
    """
    if R > R_th and LI > LI_th and dH <= dH_th:
        return "VALID_COHERENT_EVENT"
    elif R > R_th and LI > LI_th and dH > dH_th:
        return "FALSE_COHERENCE (ENTROPIC_VETO)"
    else:
        return "NO_LOCKING"


# ============================================================
# Sliding Window Engine
# ============================================================

def sliding_windows(n, win, step):
    i = 0
    while i + win <= n:
        yield i, i + win
        i += step


def compute_sigma_metrics(sig, drv, fs, f1, f2, win_s, step_frac=0.2):

    sig_f = bandpass(sig, fs, f1, f2)
    drv_f = bandpass(drv, fs, f1, f2)

    phs = analytic_phase(sig_f)
    phd = analytic_phase(drv_f)
    dphi = phs - phd

    win = int(win_s * fs)
    step = max(1, int(win * step_frac))

    results = []

    for i0, i1 in sliding_windows(len(sig), win, step):
        w = slice(i0, i1)

        R = order_parameter(dphi[w])
        LI = plv(phs[w], phd[w])
        RMSE = envelope_rmse(sig_f[w], drv_f[w])
        kappa = kappa_sigma(dphi[w])
        dH = delta_entropy(sig_f[w])

        score = (R * LI) / (1.0 + RMSE)

        classification = e_veto(R, LI, dH)

        results.append({
            "t_center": (i0 + i1) / (2 * fs),
            "R": R,
            "LI": LI,
            "RMSE": RMSE,
            "kappaSigma": kappa,
            "deltaH": dH,
            "Q_eff": score,
            "class": classification
        })

    return results


# ============================================================
# Example usage
# ============================================================

if __name__ == "__main__":

    fs = 500
    t = np.arange(0, 10, 1/fs)

    # Example signals
    drv = np.sin(2*np.pi*10*t)
    sig = np.sin(2*np.pi*10*t + 0.2*np.sin(2*np.pi*1*t))

    metrics = compute_sigma_metrics(
        sig=sig,
        drv=drv,
        fs=fs,
        f1=8,
        f2=12,
        win_s=1.0
    )

    for m in metrics[:5]:
        print(m)
