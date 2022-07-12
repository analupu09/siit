# sa se scrie un program care contine urmatoarele functionalitati:
# citeste datele de intrare dintr-un fisier aflat in fisierul inpus.csv
import argparse
from homeworks import AVAILABLE_FILE_TYPES
from stats.base import Stats


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Enumerating cars list.')
    parser.add_argument(
        '-i',
        '--input_type',
        help=f'CSV file where we read from. {AVAILABLE_FILE_TYPES}',
        dest='input_type',
        default='csv'
    )
    parser.add_argument(
        '-o',
        '--output_type',
        help=f'JSON file where we write to. {AVAILABLE_FILE_TYPES}',
        dest='output_type',
        default='json'
    )

    args = parser.parse_args()
    args = vars(args)

    stats = Stats(**args)
    stats.run()
