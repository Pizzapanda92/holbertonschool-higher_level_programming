#!/usr/bin/env python3
import json
import csv


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r',) as Nfile:
            csv_data = csv.DictReader(Nfile)
            data_list = list(csv_data)

        with open('data.json', 'w') as j_file:
            json.dump(data_list, j_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except:
        return False
