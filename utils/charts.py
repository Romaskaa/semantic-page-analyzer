import matplotlib.pyplot as plt

def plot_seo_score(score):

    labels = ["SEO Score"]
    values = [score]

    plt.bar(labels, values)

    plt.title("SEO Optimization")

    plt.savefig("storage/temp/seo_score.png")

    return "storage/temp/seo_score.png"