import pandas as pd

def load_data():
    df = pd.read_csv(r"C:\Users\HP V\PycharmProjects\Placementpredictionsystem\data\placement_data.csv")
    return df

def get_summary(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "target": "PlacementStatus"
    }

if __name__ == "__main__":
    df = load_data()

    print("First 5 Rows of the Dataset:")
    print(df.head())      # Prints first 5 rows

    print("\nDataset Summary:")
    print(get_summary(df))