import matplotlib.pyplot as plt
import os

def plot_seo_report(seo_report, path="storage/temp/seo_report.png"):
    """
    Визуализация issues / warnings / passed
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    counts = [len(seo_report["issues"]), len(seo_report["warnings"]), len(seo_report["passed"])]
    labels = ["Issues", "Warnings", "Passed"]
    colors = ["red","orange","green"]

    plt.figure(figsize=(6,4))
    plt.bar(labels, counts, color=colors)
    plt.title("SEO Analysis Report")
    plt.ylabel("Количество")
    plt.savefig(path)
    plt.close()
    return path