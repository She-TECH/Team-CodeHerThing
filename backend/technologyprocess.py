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

def segregatetechnology() :

    nlp = spacy.load('en_core_web_sm')
    matcher = PhraseMatcher(nlp.vocab)

    # Only run nlp.make_doc to speed things up
    termTechno = ["Cybersecurity", "Security", "vulnerabilities", "malware", "virus","hack","ransomware","Denial of Service", "DoS","SQL Injection","Network Security","Hijack","CSRF","Digital Signature","XSS","Cross Site Scripting","SSL","TLS","OWASP","IEC62443", "Vulnerabilities", "Malware", "Virus", "Hack", "Ransomeware", "hijack",
              "Digital Twin", "Simulation"
              "Analytics", "AI", "Artificial Intelligence", "Machine Learning",
              "IOT", "Cloud", "Edge", "Wireless", "Internet of Things", "IIOT", "Protocol", "IoT",
              "Blockchain", "Cryptography"
              "Robotics",
               "cybersecurity", "security",
              "digital twin", "simulation"
              "analytics", "artificial intelligence", "machine learning",
            "cloud", "edge", "wireless", "internet of things",  "protocol",
              "blockchain", "cryptography"
              "robotics",
              "I/O Module", "Controller", "controller", "Server", "server", "Virtualization", "virtualization", "Virtual", "virtual", "Modular", "modular","Container", "container", "containerization", "Containerization", "IO Module" ]

    termTechno1 = ["Cybersecurity", "Security", "cybersecurity", "security", "vulnerabilities", "malware", "virus","hack","ransomware","Denial of Service", "DoS","SQL Injection","Network Security","Hijack","CSRF","Digital Signature","XSS","Cross Site Scripting","SSL","TLS","OWASP","IEC62443", "Vulnerabilities", "Malware", "Virus", "Hack", "Ransomeware", "hijack"]
    termTechno2 = ["Digital Twin", "digital twin", "Simulation", "simulation"]
    termTechno3 = ["Analytics", "AI", "Artificial Intelligence", "Machine Learning", "analytics",  "artificial intelligence", "machine learning"]
    termTechno4 = ["IOT", "Cloud", "Edge", "Wireless", "IoT","Internet of Things", "IIOT", "Protocols", "cloud", "edge", "wireless", "internet of things",  "protocols"]
    termTechno5 = ["blockchain", "Blockchain", "cryptography", "Cryptography"]
    termTechno6 = ["robotics", "Robotics"]
    termTechno7 = ["I/O Module", "Controller", "controller", "Server", "server", "Virtualization", "virtualization", "Virtual", "virtual", "Modular", "modular","Container", "container", "containerization", "Containerization", "IO Module"]


    # Only run nlp.make_doc to speed things up
    patterns = [nlp.make_doc(text) for text in termTechno]
    matcher.add("TerminologyList", None, *patterns)

    path = r"D:\\Trainings\\Hackathon\\repo\\Team-CodeHerThing\\company\\*.csv"
    for fname in glob.glob(path):
        fileName_absolute = os.path.basename(fname)
        df = pd.read_csv(fname, sep=",")
        xl_sheetname = fileName_absolute[:-4]
        workbookTechno1 = xlwt.Workbook()
        worksheetTechno2 = workbookTechno1.add_sheet(xl_sheetname + "Cyber security")
        worksheetTechno2.write(0, 0, 'Summary')
        worksheetTechno2.write(0, 1, 'URL')
        worksheetTechno2.write(0, 2, 'Snippet')
        worksheetTechno3 = workbookTechno1.add_sheet(xl_sheetname + "Digital Twin")
        worksheetTechno3.write(0, 0, 'Summary')
        worksheetTechno3.write(0, 1, 'URL')
        worksheetTechno3.write(0, 2, 'Snippet')
        worksheetTechno4 = workbookTechno1.add_sheet(xl_sheetname + "Data Analytics and AI")
        worksheetTechno4.write(0, 0, 'Summary')
        worksheetTechno4.write(0, 1, 'URL')
        worksheetTechno4.write(0, 2, 'Snippet')
        worksheetTechno5 = workbookTechno1.add_sheet(xl_sheetname + "ConnectivityEdge")
        worksheetTechno5.write(0, 0, 'Summary')
        worksheetTechno5.write(0, 1, 'URL')
        worksheetTechno5.write(0, 2, 'Snippet')
        worksheetTechno6 = workbookTechno1.add_sheet(xl_sheetname + "blockchain")
        worksheetTechno6.write(0, 0, 'Summary')
        worksheetTechno6.write(0, 1, 'URL')
        worksheetTechno6.write(0, 2, 'Snippet')
        worksheetTechno7 = workbookTechno1.add_sheet(xl_sheetname + "Autonomous Robots")
        worksheetTechno7.write(0, 0, 'Summary')
        worksheetTechno7.write(0, 1, 'URL')
        worksheetTechno7.write(0, 2, 'Snippet')
        worksheetTechno8 = workbookTechno1.add_sheet(xl_sheetname + "Additive manufacturing")
        worksheetTechno8.write(0, 0, 'Summary')
        worksheetTechno8.write(0, 1, 'URL')
        worksheetTechno8.write(0, 2, 'Snippet')

        row_final = 1
        for i in range(1, len(df.index)):
            doc = nlp(df['Snippet'][i])
            matches = matcher(doc)
            for match_id, start, end in matches:
                span = doc[start:end]
                print(span.text)
                if (span.text in termTechno1):
                    col = 0
                    worksheetTechno2.write(row_final, col, df['Summary'][i])
                    worksheetTechno2.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno2.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termTechno2):
                    col = 0
                    worksheetTechno3.write(row_final, col, df['Summary'][i])
                    worksheetTechno3.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno3.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termTechno3):
                    col = 0
                    worksheetTechno4.write(row_final, col, df['Summary'][i])
                    worksheetTechno4.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno4.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termTechno4):
                    col = 0
                    worksheetTechno5.write(row_final, col, df['Summary'][i])
                    worksheetTechno5.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno5.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termTechno5):
                    col = 0
                    worksheetTechno6.write(row_final, col, df['Summary'][i])
                    worksheetTechno6.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno6.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termTechno6):
                    col = 0
                    worksheetTechno7.write(row_final, col, df['Summary'][i])
                    worksheetTechno7.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno7.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1
                elif (span.text in termTechno7):
                    col = 0
                    worksheetTechno8.write(row_final, col, df['Summary'][i])
                    worksheetTechno8.write(row_final, col + 1, df['URL'][i])
                    worksheetTechno8.write(row_final, col + 2, df['Snippet'][i])
                    row_final += 1

        workbookTechno1.save("..\\technologyCompany\\" + xl_sheetname + ".xls")