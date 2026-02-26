import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")


def ask_agent(question: str):

    q = question.lower()

    # ===== basic stats =====
    if "average" in q and "fare" in q:
        return f"Average fare: {df['Fare'].mean():.2f}"

    if "survival rate" in q:
        rate = df['Survived'].mean() * 100
        return f"Overall survival rate: {rate:.2f}%"

    if "male" in q and "percentage" in q:
        perc = (df['Sex'].value_counts(normalize=True)['male']) * 100
        return f"Male passengers: {perc:.2f}%"

    if "female" in q and "percentage" in q:
        perc = (df['Sex'].value_counts(normalize=True)['female']) * 100
        return f"Female passengers: {perc:.2f}%"

    if "embark" in q:
        return df['Embarked'].value_counts().to_string()

    if "class" in q and "fare" in q:
        return df.groupby('Pclass')['Fare'].mean().to_string()

    # ===== charts =====
    if "age" in q and ("chart" in q or "plot" in q or "histogram" in q):
        df['Age'].hist()
        plt.title("Age Distribution")
        plt.savefig("age_hist.png")
        return "Age chart created"

    if "fare" in q and ("chart" in q or "plot" in q):
        df['Fare'].hist()
        plt.title("Fare Distribution")
        plt.savefig("fare_hist.png")
        return "Fare chart created"

    if "survival" in q and ("chart" in q or "plot" in q):
        df['Survived'].value_counts().plot(kind="bar")
        plt.title("Survival Count")
        plt.savefig("survival_chart.png")
        return "Survival chart created"

    return "Ask anything about passengers, fare, survival, age, class etc."