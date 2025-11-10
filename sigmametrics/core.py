import numpy as np
from scipy.signal import butter, filtfilt, hilbert

def bandpass(x, fs, f1, f2, order=4):
    b, a = butter(order, [f1/(fs/2), f2/(fs/2)], btype='band')
    return filtfilt(b, a, x)

def analytic_phase(x):
    return np.unwrap(np.angle(hilbert(x)))

def phdiff(ph_sig, ph_drv):
    return ph_sig - ph_drv

def sliding_windows(n, win, step):
    i = 0
    while i + win <= n:
        yield i, i+win
        i += step

def envelope_rmse(x, y):
    ex = np.abs(hilbert(x)); ey = np.abs(hilbert(y))
    ex = (ex - ex.mean())/(ex.std() + 1e-9)
    ey = (ey - ey.mean())/(ey.std() + 1e-9)
    return float(np.sqrt(np.mean((ex - ey)**2)))

def order_parameter(dphi):
    z = np.exp(1j*(dphi - np.mean(dphi)))
    return float(np.abs(np.mean(z)))

def plv(ph_sig, ph_drv):
    return float(np.abs(np.mean(np.exp(1j*(ph_sig - ph_drv)))))

def kappa_sigma(dphi):
    var = np.var(np.diff(dphi))
    return float(1.0/(var + 1e-6))

def compute_sigma_metrics(sig, drv, fs, f1, f2, win_s, step_frac=0.2):
    sig_f = bandpass(sig, fs, f1, f2)
    drv_f = bandpass(drv, fs, f1, f2)
    phs = analytic_phase(sig_f)
    phd = analytic_phase(drv_f)
    dphi = phdiff(phs, phd)
    win = int(win_s * fs)
    step = max(1, int(win*step_frac))
    times = []
    R_list, LI_list, RMSE_list, kappa_list = [], [], [], []
    for i0,i1 in sliding_windows(len(sig), win, step):
        w = slice(i0,i1)
        times.append((i0+i1)/(2*fs))
        R_list.append(order_parameter(dphi[w]))
        LI_list.append(plv(phs[w], phd[w]))
        RMSE_list.append(envelope_rmse(sig_f[w], drv_f[w]))
        kappa_list.append(kappa_sigma(dphi[w]))
    return {"t": times, "R": R_list, "LI": LI_list, "RMSE_SL": RMSE_list, "kappaSigma": kappa_list}

def re_q_score(R, LI, RMSE):
    R = np.asarray(R); LI = np.asarray(LI); RMSE = np.asarray(RMSE)
    score = (R*LI)/(1.0 + RMSE)
    return score.tolist(), float(np.nanmax(score))
