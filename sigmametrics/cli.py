#!/usr/bin/env python3
import argparse, json, pandas as pd
from .core import compute_sigma_metrics

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="inp", required=True)
    p.add_argument("--fs", type=float, required=True)
    p.add_argument("--band", nargs=2, type=float, default=[0.1,5.0])
    p.add_argument("--win", type=float, default=5.0)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    df = pd.read_csv(a.inp)
    res = compute_sigma_metrics(df["signal"].values, df["driver"].values, a.fs, a.band[0], a.band[1], a.win)
    with open(a.out,"w") as f: json.dump(res,f,indent=2)
    print("OK", a.out)

if __name__ == "__main__":
    main()
