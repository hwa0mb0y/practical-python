# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, types, delimiter=',', has_headers=True, select=None):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        # read headers
        headers = next(rows) if has_headers else []
            
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    
    return records
