import csv
import glob
import re
import os

current_dir = os.path.dirname(__file__)
file_name = current_dir + '/definition.md'

def run():
    files = glob.glob(current_dir + '/tsv/*_desc.tsv')
    
    for file in files:
        s = re.search(r"^.*(\\|/)(?P<table_name>\w+)_desc\.tsv$", file)
        table_name = s.group('table_name')
        
        write_table_name(table_name)
        write_table_definition(table_name)
        write_index_definition(table_name)

def write_table_name(table_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write('\r')
        f.write('** ' + table_name + '\r')

def write_table_definition(table_name):
    write(table_name, 'テーブル定義', '_desc.tsv')

def write_index_definition(table_name):
    write(table_name, 'インデックス', '_index.tsv')

def write(table_name, md_header, sufix):

    file = current_dir + '/tsv/' + table_name + sufix
    if os.path.getsize(file) > 0:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            table_header = next(reader)
            table_header = '|'.join(table_header)
            table_header = '|' + table_header + '|h'

            rows = list()
            for cols in reader:
                row = '|'.join(cols)
                row = '|' + row + '|'
                rows.append(row)

        write_definition(md_header, table_header, rows)

def write_definition(md_header, table_header, rows):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write("''" + md_header + "''" + '\r')
        f.write(table_header + '\r')
        for row in rows:
            f.write(row + '\r')

if __name__ == '__main__':
    run()