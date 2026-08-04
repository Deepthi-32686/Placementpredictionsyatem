from src.data.load_data import load_data
import matplotlib.pyplot as plt
def basic_eda(df):
    print("First 5 rows")
    print(df.head())
    print("Last 5 rows")
    print(df.tail())
    print("25 to 35 rows")
    print(df.iloc[25:35])
    print("column names")
    print(df.columns)
    print("data types")
    print(df.dtypes)
    print("complete information")
    print(df.info())

    print("min")
    print(df.min())
    print("max")
    print(df.max())
    print("duplicates")
    print(df.duplicated())
    print("null values")
    print(df.isnull().sum())
    print(df["PlacementStatus"].value_counts())
    count = df["PlacementStatus"].value_counts()
    plt.figure(figsize=(6,5))
    plt.bar(count.index,count.values)
    plt.bar(count.index,count.values)
    plt.xlabel("Placement Status")
    plt.ylabel("Count")
    plt.savefig(r"C:\Users\HP V\PycharmProjects\Placementpredictionsystem\results\barchart.png")
    plt.show()
def univariate(df):
    plt.figure(figsize=(6,5))
    plt.hist(df["CGPA"],bins=10)
    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    plt.savefig(r"C:\Users\HP V\PycharmProjects\Placementpredictionsystem\results\histogram.png")
    plt.show()
    gendercount = df["Gender"].value_counts()
    plt.figure(figsize=(6,5))
    plt.pie(gendercount.values,labels=gendercount.index,autopct="%1.1f%%",startangle=90)
    plt.title("Gender Distribution piechart")
    plt.savefig(r"C:\Users\HP V\PycharmProjects\Placementpredictionsystem\results\piechart.png")
    plt.show()
def bivariate(df):
    plt.figure(figsize=(6,5))
    plt.scatter(df["CGPA"], df["AptitudeTestScore"])
    plt.title("CGPA vs Aptitude Test Score")
    plt.xlabel("CGPA")
    plt.ylabel("Aptitude Test Score")
    plt.savefig(r"C:\Users\HP V\PycharmProjects\Placementpredictionsystem\app\static\charts\cgpa_aptitudescore_scatter.png")
    plt.show()
    plt.close()
    plt.figure(figsize=(6,5))
    placed=df[df["PlacementStatus"] == 1]["CGPA"]
    not_placed=df[df["PlacementStatus"] == 0]["CGPA"]
    plt.boxplot([placed, not_placed], label=["placed", "not placed"])
    plt.title("CGPA vs PlacementStatus")
    plt.xlabel("CGPA")
    plt.ylabel("PlacementStatus")
    plt.savefig(r"C:\Users\HP V\PycharmProjects\Placementpredictionsystem\app\static\charts\boxplot.png")
    plt.show()
    plt.close()









if __name__ == "__main__":
    df=load_data()
    #basic_eda(df)
    #univariate(df)
    bivariate(df)


