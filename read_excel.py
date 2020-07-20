#!/usr/bin/env python
# -*- coding: 850 -*-
# read file excel
# @utor: Leonardo Marcos Santiago
# library: pip install xlrd
# execute: python read_excel.py

import os
import xlrd

loc = ('/Users/lmarcoss/workspace-sura/documentos/GMM/CATALOGO_PARA_COMPROBANTE_GASTOS_MEDICOS.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for row in sheet.get_rows():
    row_value = ''
    for col in row:
        if col.ctype == 1:
            if len(col.value) > 0:
                row_value = row_value + ',\'' + col.value + '\''
            else:
                row_value = row_value + ',null'
        elif 2 <= col.ctype <= 4:
            row_value = row_value + ',' + str(int(col.value))
        elif col.ctype == 0:
            row_value = row_value + ',null'

    print(row_value[1:])
