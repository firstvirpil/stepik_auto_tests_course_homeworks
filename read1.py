with open(r"c:\amd\dataset_24465_4.txt", 'r') as file:
    data = file.readlines()
    result = data[::-1]
    with open(r"c:\amd\dataset.txt", 'w') as fil:
        writer = fil.writelines(result)

