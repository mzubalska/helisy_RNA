#!/usr/bin python
# -*- coding: utf-8 -*-

import os


# Konwersja zapisu na:
# zasada nr_polozenia nazwa_lancucha zasada nr_polozenia nazwa_lancucha parowanie

def zapis(plik_in, plik_out):
#    list_a = ['/', '"', ',', 'WW_cis', 'WW_tran', 'WH_cis', 'HW_cis', 'WH_tran', 'HW_tran', 'WS_cis', 'SW_cis',
#              'WS_tran', 'SW_tran', 'HH_cis', 'HH_tran', 'HS_cis', 'SH_cis', 'HS_tran', 'SH_tran', 'SS_cis', 'SS_tran']
#    list_b = [' ', '', ' ', 'cWW', 'tWW', 'cWH', 'cHW', 'tWH', 'tHW', 'cWS', 'cSW', 'tWS', 'tSW', 'cHH', 'tHH', 'cHS',
#              'csH', 'tHS', 'tSH', 'cSS', 'tSS']

    with open(plik_in, 'r') as in_put:
        with open(plik_out + '.bp', 'w') as output:
            for line in in_put:
                c = line.replace('/',' ').replace('"','').replace(',',' ').replace('WW_cis','cWW').replace('WW_tran', 'tWW').replace('WH_cis','cWH').replace('HW_cis','cHW').replace('WH_tran','tWH').replace('HW_tran','tHW').replace('WS_cis','cWS').replace('SW_cis','cSW').replace('WS_tran','tWS').replace('SW_tran','tSW').replace('HH_cis','cHH').replace('HH_tran','tHH').replace('HS_cis','cHS').replace('SH_cis','cSH').replace('HS_tran','tHS').replace('SH_tran','tSH').replace('SS_cis','cSS').replace('SS_tran','tSS')
                c = c.rsplit()
                print(c)
                if c[6] in ['cWW','tWW','cWH','cHW','tWH','tHW','cWS','cSW','tWS','tSW','cHH','tHH','cHS','cSH','tHS','tSH', 'cSS', 'tSS']:
                    output.write(c[1] + ' ' + c[2] + ' ' + c[0] + ' ' + c[4] + ' ' + c[5] + ' ' + c[3] + ' ' + c[6] + "\n")


def zasady(plik1, plik2):
    with open(plik1, 'r') as pl1:
        with open(plik2 + '.txt', 'w') as pl2:
            for line in pl1:
                a = line.split()
                if a[0] == 'A' and a[3] == 'U':
                    continue
                elif a[0] == 'U' and a[3] == 'A':
                    continue
                elif a[0] == 'G' and a[3] == 'C':
                    continue
                elif a[0] == 'C' and a[3] == 'G':
                    continue
                else:
                    pl2.write(a[0] + ' ' + a[1] + ' ' + a[2] + ' ' + a[3] + ' ' + a[4] + ' ' + a[5] + ' ' + a[6] + "\n")


# Wczytywanie plikow csv z parowaniami

def wczytaj(dirpath):
    for plik in os.listdir(dirpath):
        if os.path.splitext(plik)[1] == '.csv':
            name = os.path.splitext(plik)[0]
            zapis(plik, name)


wczytaj('./')


def wczytaj2(path):
    for i in os.listdir(path):
        if os.path.splitext(i)[1] == '.bp':
            name = os.path.splitext(i)[0]
            zasady(i, name)


wczytaj2('./')
