"""
.. module:: csv
   :platform: Linux, Windows
   :synopsis: Get data from CSV files.

.. moduleauthor:: Quentin Marlats

"""

import csv
from pyquizz import settings

def get_csv_data(csv_file, n_of_files = 0):
    """Get data from CSV file(s).

    :param csv_file: CSV file name
    :type csv_file: str
    :param n_of_files: number of CSV files (files format: %filename_%file_number)
    :type n_of_files: str
    :returns: CSV data

    """

    if n_of_files == 0:
        try:
            with open("%s.csv" % (csv_file), "rt") as f:
                return list(csv.reader(f))
        except IOError:
            print(settings.errors['CANT_OPEN_FILE'])
    else:
        # Initialize list of data
        csv_data = []
        # Create the list of CSV data
        for i in range(0, n_of_files):
            try:
                with open("%s_%i.csv" % (csv_file, i + 1), "rt") as f:
                    csv_data.append(list(csv.reader(f)))
            except IOError:
                print(settings.errors['CANT_OPEN_FILE'])
        return csv_data
