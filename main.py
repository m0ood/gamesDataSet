import pandas as pd
import seaborn as sns


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    videogames = pd.read_csv("./vgsales.csv")
    print(videogames)
    GenceAndGlobal_Sales = pd.crosstab(videogames["Genre"], videogames["Global_Sales"], margins=True)
    sns.set(rc={"figure.figsize": (15, 4)})
    chart = sns.barplot(x=GenceAndGlobal_Sales["All"][:12].index, y=GenceAndGlobal_Sales["All"][:12])
    print(chart.set(xlabel='Genre', ylabel='Sales(in millions)'))

