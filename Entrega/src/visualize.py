import seaborn as sns
import matplotlib.pyplot as plt

def plot_age_distribution(df):
    sns.histplot(df['age'], kde=True)
    plt.title("Distribución de edad")
    plt.show()

def plot_subscription_rate(df):
    sns.countplot(x='y', data=df)
    plt.title("Tasa de suscripción")
    plt.show()

def plot_correlations(df):
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(numeric_only=True), annot=False, cmap='coolwarm')
    plt.title("Mapa de calor de correlaciones")
    plt.show()
