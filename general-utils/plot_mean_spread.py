import matplotlib.pyplot as plt
import numpy as np


def plot_aligned_profiles_with_statistics(aligned_profiles, ylabel="Intensity", ax=None):
    """
    Plot aligned profiles together with their mean and spread.

    Args:
        aligned_profiles (np.ndarray): Array of aligned profiles (2D array).
    """
    # Calculate the mean and standard deviation
    mean_profile = np.mean(aligned_profiles, axis=0)
    std_profile = np.std(aligned_profiles, axis=0)

    # Plot all aligned profiles
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    for profile in aligned_profiles:
        ax.plot(
            profile,
            color="blue",
            alpha=0.05,
            label="Aligned Profiles" if "label_shown" not in locals() else "",
        )
        locals()["label_shown"] = True

    # Plot mean profile
    ax.plot(mean_profile, color="red", label="Mean Profile", linewidth=2)

    # Plot shaded area for spread (mean ± std)
    ax.fill_between(
        range(len(mean_profile)),
        mean_profile - std_profile,
        mean_profile + std_profile,
        color="red",
        alpha=0.4,
        label="Spread (±Std)",
    )

    ax.set_title("Aligned Profiles with Mean and Spread")
    ax.set_xlabel("Distance")
    ax.set_ylabel(ylabel)
    ax.legend(loc="upper right")
    ax.grid(True)
