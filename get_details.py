def details(Id):
    import pandas as pd
    df = pd.read_csv("valid_person_data/data.csv")
    data = df.values
    print(data)
    unique_ids = list(data[:, 0])
    print("ID ", Id)
    print(unique_ids)
    print(unique_ids)
    row_index = unique_ids.index(Id)
    return data[row_index]
# check=details(312)
# print(check)
