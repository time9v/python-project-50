#!/usr/bin/env python3
import argparse
import os
from gendiff.task.comparison import generate_diff, input_dicts, open_json_file



parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', metavar='FORMAT',
                        type=str, default='stylish',
                        help='output format (default: "stylish")')
args = parser.parse_args()
work_dir = os.path.join(os.getcwd(), 'files')
file1_path = os.path.join(work_dir, args.first_file)
file2_path = os.path.join(work_dir, args.second_file)
file1_dict = open_json_file(file1_path)
file2_dict = open_json_file(file2_path)


def main():
    generate_diff(input_dicts(file1_dict, file2_dict))


if __name__ == '__main__':
    main()


