

def CART(dataset, attribute, y):
    selection = list(set(dataset[attribute]))
    selection2 = list(set(dataset[y]))
    dataset_len = len(dataset)
    # 분류
    for i in selection:
        result = []
        result2 = []
        data1 = dataset[dataset[attribute] == i]
        data2 = dataset[dataset[attribute] != i]
        data1_len = len(data1)
        data2_len = len(data2)
        # 생존 분류
        for j in selection2:
            data1_2 = data1[data1[y] == j]
            data2_2 = data2[data2[y] == j]
            data1_2_len = len(data1_2)
            data2_2_len = len(data2_2)
            result.append((data1_2_len/data1_len)**2)
            result2.append((data2_2_len/data2_len)**2)
        Gini1 = 1 - sum(result)
        Gini2 = 1 - sum(result2)
        final = (data1_len/dataset_len)*Gini1 + (data2_len/dataset_len)*Gini2
        print(i, ' : ', final)