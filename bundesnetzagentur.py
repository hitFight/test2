# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/CHesseling/Datentricks/blob/master/test.ipynb
"""

import pandas as pd

df = pd.read_csv('https://www.bundesnetzagentur.de/_tools/SVG/js2/_functions/csv_export.html?view=renderCSV&id=870296', sep=";", parse_dates=['                    .'], dayfirst=True)

df['lng_anteil'] = df['LNG'] / df['Deutschland Import'] * 100

df

aktuellerwert = round(df.iloc[-1,13], 2)

text = "Gestern lag der LNG-Anteil an allen Gas-Importen bei {} Prozent".format(aktuellerwert) # Fügt den Wert in den Text ein

print(text)

#!pip install pymsteams # Lädt die Bibliothek aus PyPi herunter

import pymsteams # Wrapper Library

myTeamsMessage = pymsteams.connectorcard("https://onndr.webhook.office.com/webhookb2/f8115a08-9c2d-46c9-874a-dfe05ed61759@14231bc8-8718-48a7-88e2-0ac25c6234b4/IncomingWebhook/b10dde54b1fe4c33958a1ce69558566f/d5c49184-530f-4f2f-a3bd-b2b2dee29b5d")

myTeamsMessage.text(text)

myTeamsMessage.send()
