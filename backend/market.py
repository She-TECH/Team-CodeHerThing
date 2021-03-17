from __future__ import unicode_literals, print_function
import pandas as pd
import sys, glob
import xlwt
import os
import csv
import en_core_web_sm
import xlrd
import spacy
from spacy.matcher import PhraseMatcher

def markettrendprocessing():
    nlp = spacy.load('en_core_web_sm')
    matcher = PhraseMatcher(nlp.vocab)

    # Only run nlp.make_doc to speed things up
    termMarket = ["new", "introduce", "announced", "launched", "acquire", "implement", "Implements","release",
              "collab", "acquire"]

    termMarket1 = ["new", "introduce", "announced", "launched", "acquire", "implement", "Implements", "release"]
    termMarket2 = ["collab", "acquire"]

    # Only run nlp.make_doc to speed things up
    patterns = [nlp.make_doc(text) for text in termMarket]
    matcher.add("TerminologyList", None, *patterns)
#"D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\*.csv"
    path = r"..//company//*.csv"
    for fname in glob.glob(path):
        fileName_absolute = os.path.basename(fname)
        df = pd.read_csv(fname, sep=",")
        xl_sheetname = fileName_absolute[:-4]
        workbookMarket1 = xlwt.Workbook()
        worksheetMarket2 = workbookMarket1.add_sheet(xl_sheetname + "security")
        worksheetMarket2.write(0, 0, 'Summary')
        worksheetMarket2.write(0, 1, 'URL')
        worksheetMarket2.write(0, 2, 'Snippet')
        worksheetMarket3 = workbookMarket1.add_sheet(xl_sheetname + "Collaboration")
        worksheetMarket3.write(0, 0, 'Summary')
        worksheetMarket3.write(0, 1, 'URL')
        worksheetMarket3.write(0, 2, 'Snippet')

        row_final = 1
        for i in range(1, len(df.index)):
            doc = nlp(df['Snippet'][i])
            matches = matcher(doc)
            for match_id, start, end in matches:
                span = doc[start:end]
                print(span.text)
                if (span.text in termMarket1):
                    col = 0
                    worksheetMarket2.write(row_final, col, df['Summary'][i])
                    worksheetMarket2.write(row_final, col + 1, df['URL'][i])
                    worksheetMarket2.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termMarket2):
                    col = 0
                    worksheetMarket3.write(row_final, col, df['Summary'][i])
                    worksheetMarket3.write(row_final, col + 1, df['URL'][i])
                    worksheetMarket3.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1

        workbookMarket1.save("..\\market\\" + xl_sheetname + ".xls")