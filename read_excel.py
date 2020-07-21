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
    count = 0
    is_valid = 0
    for col in row:
        # Si la columna 15 tiene valor y es 9 entonces el registro debe ser contado
        if count == 15:
            if col.ctype != 0 and col.value == 9:
                is_valid = 1
        else:
            if col.ctype == 1:
                if len(col.value) > 0:
                    # se agrega el valor
                    row_value = row_value + ',\'' + col.value + '\''
                else:
                    # se agrega como null
                    row_value = row_value + ',null'
            elif 2 <= col.ctype <= 4:
                row_value = row_value + ',' + str(int(col.value))
            else:
                row_value = row_value + ',null'
        count = count + 1
    if is_valid:
        print(row_value[1:])
