#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# csv operations

import csv

def csv_read(file, ignore_header=True):
    ret = []
    with open(file) as fp:
        reader = csv.reader(fp)
        i = 0
        for row in reader:
            if ignore_header and i == 0:
                continue
            i += 1
            ret.append(row)
            
    return ret
            
            
            
