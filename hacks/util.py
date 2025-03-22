import matplotlib.pyplot as plt
import numpy as np

def plot_survival_function(time_points, surv_points, label):
    """Plot the survival function"""
    plt.figure(figsize=(5, 3))
    plt.step(time_points, surv_points, where="post", label=f"{label}")
    plt.ylabel("Survival probability")
    plt.xlabel("Time in days")
    plt.legend()
    plt.grid(True)

def normalize(values):
    """Nomralize the values to be in the range [0, 1]"""
    min_val = np.min(values)
    max_val = np.max(values)
    return (values - min_val) / (max_val - min_val)
