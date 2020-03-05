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

# Training additional entity types using spaCy
import pickle
import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
def segregateCompanyData():
    keywords = {"Siemens", "Schneider", "Rockwell", "ABB"}  # all your keywords
    with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\Siemens.csv', 'a', newline='',
    encoding="utf-8") as fd:
        newFileWriter = csv.writer(fd)
        newFileWriter.writerow(['Summary', 'URL', 'Snippet'])
    with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\ABB.csv', 'a', newline='',
    encoding="utf-8") as fd:
        newFileWriter = csv.writer(fd)
        newFileWriter.writerow(['Summary', 'URL', 'Snippet'])
    with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\Schneider.csv', 'a', newline='',
    encoding="utf-8") as fd:
        newFileWriter = csv.writer(fd)
        newFileWriter.writerow(['Summary', 'URL', 'Snippet'])
    with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\Rockwell.csv', 'a', newline='',
    encoding="utf-8") as fd:
        newFileWriter = csv.writer(fd)
        newFileWriter.writerow(['Summary', 'URL', 'Snippet'])

    path = r"D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\NewData\\*.csv"
    for fname in glob.glob(path):
        df = pd.read_csv(fname, sep=",")
        for i in range(1, len(df.index)):
            for keyword in keywords:
                if int(keyword in df['Summary'][i]) == 1:
                    if keyword == "Siemens":
                        with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\Siemens.csv', 'a',
                        newline='', encoding="utf-8") as fd:
                            newFileWriter = csv.writer(fd)
                            newFileWriter.writerow([df['Summary'][i], df['URL'][i], df['Snippet'][i]])
                    elif keyword == "ABB":
                        with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\ABB.csv', 'a', newline='',
                        encoding="utf-8") as fd:
                            newFileWriter = csv.writer(fd)
                            newFileWriter.writerow([df['Summary'][i], df['URL'][i], df['Snippet'][i]])
                    elif keyword == "Schneider":
                        with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\Schneider.csv', 'a',
                        newline='', encoding="utf-8") as fd:
                            newFileWriter = csv.writer(fd)
                            newFileWriter.writerow([df['Summary'][i], df['URL'][i], df['Snippet'][i]])
                    elif keyword == "Rockwell":
                        with open('D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\Rockwell.csv', 'a',
                        newline='', encoding="utf-8") as fd:
                            newFileWriter = csv.writer(fd)
                            newFileWriter.writerow([df['Summary'][i], df['URL'][i], df['Snippet'][i]])

def processnewproductdata():
    path = r"D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\*.csv"
    keywords_new = {"new", "introduce", "announced", "launched", "acquire", "implement", "Implements"}  # all your keywords

    workbook = xlwt.Workbook()
    nlp = spacy.load('en_core_web_sm')
    matcher = PhraseMatcher(nlp.vocab)
    terms = ["new", "introduce", "announced", "launched", "acquire", "implement", "Implements"]
    # Only run nlp.make_doc to speed things up
    patterns = [nlp.make_doc(text) for text in terms]
    matcher.add("TerminologyList", None, *patterns)

    nlp = en_core_web_sm.load()

    for fname in glob.glob(path):
        fileName_absolute = os.path.basename(fname)
        df = pd.read_csv(fname, sep=",")
        col =0
        worksheet1 = workbook.add_sheet(fileName_absolute)
        worksheet1.write(0, col, 'Summary')
        worksheet1.write(0, col + 1, 'URL')
        worksheet1.write(0, col + 2, 'Snippet')
        row = 1
        for i in range(1, len(df.index)):
            doc = nlp(df['Snippet'][i])
            matches = matcher(doc)
            if (len(matches) >= 1):
                col = 0
                worksheet1.write(row, col, df['Summary'][i])
                worksheet1.write(row, col + 1, df['URL'][i])
                worksheet1.write(row, col + 2, df['Snippet'][i])
                row += 1

    workbook.save("..\\new\\NewKeywords.xls")

def newdomaindrill():
    # for Domain drill down in keyword
    nlp = spacy.load('en_core_web_sm')
    matcher = PhraseMatcher(nlp.vocab)

    # Only run nlp.make_doc to speed things up
    terma = ["Digital Transformation", "digital transformation", "Manufacturing", "Process Automation", "SCADA", "Water", "Pharmaceuticals",
         "Asset Performance Management", "Factory Automation"
                                         "Smart City", "Building Technology",  "Smart Home",
         "Mobility", "Railway",
         "Wind Turbines", "photovoltaic", "Energy", "DCS", "Oil & Gas", "Solar", "Power",
         "Healthcare", "Paper", "manufacturing", "process automation", "scada", "water", "pharmaceuticals",
         "asset performance management", "factory automation"
                                         "smart city", "building technology", "smart home",
         "mobility", "railway",
         "wind turbines", "photovoltaic", "energy", "dcs", "oil & gas", "solar", "power",
         "healthcare", "paper"]

    terms1 = ["Digital Transformation", "Manufacturing", "Process Automation", "SCADA", "Water", "Pharmaceuticals",
          "Asset Performance Management", "Factory Automation", "digital transformation", "manufacturing",
          "process automation","scada", "water", "pharmaceuticals",
          "asset performance management", "factory automation", "Paper", "paper"]
    terms2 = ["Building Technology", "Smart City", "Smart Home", "building technology", "smart city", "smart home"]
    terms3 = ["Mobility", "Railway", "mobility", "railway"]
    terms4 = ["Wind Turbines", "Photovoltaic", "Energy", "DCS", "Oil & Gas", "Solar", "Power",
          "wind turbines", "photovoltaic", "energy", "dcs", "oil & gas", "solar", "power"]
    terms5 = ["Healthcare", "healthcare"]

    # Only run nlp.make_doc to speed things up
    patterns = [nlp.make_doc(text) for text in terma]
    matcher.add("TerminologyList", None, *patterns)

    for i in range(0, 4):
        df = pd.read_excel('..\\new\\NewKeywords.xls', sheet_name=i)
        book = xlrd.open_workbook('..\\new\\NewKeywords.xls')
        sheet_names = book.sheet_names()
        sheet_names = book.sheet_names()
        xl_sheet = book.sheet_by_name(sheet_names[i])
        xl_sheetname = xl_sheet.name[:-4]
        workbook1 = xlwt.Workbook()
        worksheet2 = workbook1.add_sheet(xl_sheetname + "DI");
        worksheet2.write(0, 0, 'Summary')
        worksheet2.write(0, 1, 'URL')
        worksheet2.write(0, 2, 'Snippet')
        worksheet3 = workbook1.add_sheet(xl_sheetname + "SI");
        worksheet3.write(0, 0, 'Summary')
        worksheet3.write(0, 1, 'URL')
        worksheet3.write(0, 2, 'Snippet')
        worksheet4 = workbook1.add_sheet(xl_sheetname + "MO");
        worksheet4.write(0, 0, 'Summary')
        worksheet4.write(0, 1, 'URL')
        worksheet4.write(0, 2, 'Snippet')
        worksheet5 = workbook1.add_sheet(xl_sheetname + "Engg");
        worksheet5.write(0, 0, 'Summary')
        worksheet5.write(0, 1, 'URL')
        worksheet5.write(0, 2, 'Snippet')
        worksheet6 = workbook1.add_sheet(xl_sheetname + "Healthcare");
        worksheet6.write(0, 0, 'Summary')
        worksheet6.write(0, 1, 'URL')
        worksheet6.write(0, 2, 'Snippet')
        worksheet7 = workbook1.add_sheet(xl_sheetname + "paper");
        worksheet7.write(0, 0, 'Summary')
        worksheet7.write(0, 1, 'URL')
        worksheet7.write(0, 2, 'Snippet')
        row_final = 1
        for i in range(1, len(df.index)):
            doc = nlp(df['Snippet'][i])
            matches = matcher(doc)
            for match_id, start, end in matches:
                span = doc[start:end]
                print(span.text)
                if (span.text in terms1):
                    col = 0
                    worksheet2.write(row_final, col, df['Summary'][i])
                    worksheet2.write(row_final, col + 1, df['URL'][i])
                    worksheet2.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                if (span.text in terms2):
                    col = 0
                    worksheet3.write(row_final, col, df['Summary'][i])
                    worksheet3.write(row_final, col + 1, df['URL'][i])
                    worksheet3.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                if (span.text in terms3):
                    col = 0
                    worksheet4.write(row_final, col, df['Summary'][i])
                    worksheet4.write(row_final, col + 1, df['URL'][i])
                    worksheet4.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                if (span.text in terms4):
                    col = 0
                    worksheet5.write(row_final, col, df['Summary'][i])
                    worksheet5.write(row_final, col + 1, df['URL'][i])
                    worksheet5.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                if (span.text in terms5):
                    col = 0
                    worksheet6.write(row_final, col, df['Summary'][i])
                    worksheet6.write(row_final, col + 1, df['URL'][i])
                    worksheet6.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1

        workbook1.save("..\\DrillDownCompany\\" + xl_sheetname + ".xls")

def getNumberOfRows(file_name,sheet_name):
    xl_workbook = xlrd.open_workbook(file_name)
    xl_sheet = xl_workbook.sheet_by_name(sheet_name)
    return int(xl_sheet.nrows)

def getCSV(file_name):
    df=pd.read_csv(file_name, sep=",")

    return df['Summary']+"||"+df['URL']


def getFileData(file_name,sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    return df['Summary']+"||"+df['URL']



