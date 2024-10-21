#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tablib

data = tablib.Dataset()

names = ['Kenneth Reitz', 'Bessie Monke']

for name in names:
    # split name appropriately
    fname, lname = name.split()

    # add names to Dataset
    data.append([fname, lname])

print(data)
print(data.dict)

data.headers = ['First Name', 'Last Name']
data.append_col([22, 20], header='Age')

print(data.dict)
print(data.export('csv'))
print(data.export('json'))
data.export('xls')
print(data[0])
print(data['First Name'])
print(data.get_col(1))

# with open('data.csv', 'r') as fh:
#     imported_data = data.load(fh)

daniel_tests = [
    ('11/24/09', 'Math 101 Mid-term Exam', 56.),
    ('05/24/10', 'Math 101 Final Exam', 62.)
]

suzie_tests = [
    ('11/24/09', 'Math 101 Mid-term Exam', 56.),
    ('05/24/10', 'Math 101 Final Exam', 62.)
]

# Create new dataset
tests = tablib.Dataset()
tests.headers = ['Date', 'Test Name', 'Grade']

# Daniel's Tests
tests.append_separator('Daniel\'s Scores')

for test_row in daniel_tests:
   tests.append(test_row)

# Susie's Tests
tests.append_separator('Susie\'s Scores')

for test_row in suzie_tests:
   tests.append(test_row)

# Write spreadsheet to disk
with open('grades.xls', 'wb') as f:
    f.write(tests.export('xls'))