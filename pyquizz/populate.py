import csv

def get_csv_data(csv_file, n_of_files = 0):
    if n_of_files < 1:
        return csv.reader(open("populate/%s.csv" % (csv_file), "rt"))
    else:
        csv_files = []
        for i in range(0, n_of_files):
            csv_files.append(csv.reader(open("populate/%s_%i.csv" % (csv_file, i + 1), "rt")))
        return csv_files
