import os
import sys
import pymongo

from PyQt5.QtWidgets import *
from src.Functionality.staticAnalysis import staticAnalysis

# Initializes the connection with our local database
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['project_data']
project_db = db['project']
binary_db = db['binary']
static_db = db['static']
results_db = db['results']
function_db = db['function']
string_db = db['string']
variable_db = db['variable']
dll_db = db['dll']

newdb = client['current_project']
current_db = newdb['current']


# Gets all of the projects that were created from the database
def getProjects():
    # deleteDatabase()
    projects = []
    for p in project_db.find():
        projects.append(QTreeWidgetItem([p.get('name')]))
        child = QTreeWidgetItem(projects[len(projects) - 1])
        for b in binary_db.find():
            if b['_id'] == p.get('binary'):
                child.setText(0, b.get('file'))
    return projects


# Gets all the information of the current project from the database
def getCurrentProject(selected):
    if selected:
        newdb.current.drop()
        item = selected[0].text(0)
        for p in project_db.find():
            if p['name'] == item:
                project_data = {
                    'name': p['name'],

                    'description': p['description'],

                    'binary': p['binary'],

                    'static_analysis': {
                        '01': p.get('static_analysis', {}).get('01')
                    },

                    'dynamic_analysis': {
                        '01': ''
                    }
                }
                current_outcome = current_db.insert_one(project_data)

    text = ""
    binaryPath = ""
    for p in current_db.find():
        for b in binary_db.find():
            if b['_id'] == p.get('binary'):
                text = "<font size=3> <b>Project Description</b>: " + p.get('description') + "<br><br>"
                text += "<b>Binary Properties</b>: <br>"
                text += "<b>" + "File" + "</b>: " + b.get('file') + "<br>"
                text += "<b>" + "Os" + "</b>: " + b.get('os') + "<br>"
                text += "<b>" + "Binary" + "</b>: " + b.get('binary') + "<br>"
                text += "<b>" + "Machine" + "</b>: " + b.get('machine') + "<br>"
                text += "<b>" + "Class" + "</b>: " + b.get('class') + "<br>"
                text += "<b>" + "Bits" + "</b>: " + b.get('bits') + "<br>"
                text += "<b>" + "Language" + "</b>: " + b.get('language') + "<br>"
                text += "<b>" + "Canary" + "</b>: " + b.get('canary') + "<br>"
                text += "<b>" + "Crypto" + "</b>: " + b.get('crypto') + "<br>"
                text += "<b>" + "Nx" + "</b>: " + b.get('nx') + "<br>"
                text += "<b>" + "Relocs" + "</b>: " + b.get('relocs') + "<br>"
                text += "<b>" + "Stripped" + "</b>: " + b.get('stripped') + "<br>"
                text += "<b>" + "Relro" + "</b>: " + b.get('relro') + "<br> </font>"
                binaryPath = b.get('file')

    return text, binaryPath


# Gets and saves Static Analysis results into database
def saveStatic():
    path = ''
    for p in current_db.find():
        for b in binary_db.find():
            if b['_id'] == p.get('binary'):
                path = b.get('file')

    poi = ''
    try:
        # function, string, variable, dll = staticAnalysis(path)
        poi = staticAnalysis(path)
        for p in current_db.find():
            for s in static_db.find():
                if s['_id'] == p.get('static_analysis', {}).get('01'):
                    for r in results_db.find():
                        if r['_id'] == s.get('results').get('01'):
                            for i in range(len(poi[0])):
                                function = {
                                    'results_id': r['_id'],
                                    'comment': '',
                                    'data': poi[0][i]
                                }
                                function_outcome = function_db.insert_one(function)

                                results_db.find_one_and_update(
                                    {'_id': r['_id']},
                                    {'$push': {'function': {str(i): function['_id']}}}, upsert=True)

                            for i in range(len(poi[1])):
                                string = {
                                    'results_id': r['_id'],
                                    'comment': '',
                                    'data': poi[1][i]
                                }
                                function_outcome = string_db.insert_one(string)

                                results_db.find_one_and_update(
                                    {'_id': s['_id']},
                                    {'$push': {'string': {str(i): string['_id']}}}, upsert=True)

                            # for i in range(len(poi[2])):
                            #     variable = {
                            #         'results_id': r['_id'],
                            #         'comment': '',
                            #         'data': poi[2][i]
                            #     }
                            #     function_outcome = variable_db.insert_one(variable)
                            #
                            #     results_db.find_one_and_update(
                            #         {'_id': s['_id']},
                            #         {'$push': {'variable': {str(i): variable['_id']}}}, upsert=True)

                            for i in range(len(poi[2])):
                                dll = {
                                    'results_id': r['_id'],
                                    'comment': '',
                                    'data': poi[2][i]
                                }
                                function_outcome = dll_db.insert_one(dll)

                                results_db.find_one_and_update(
                                    {'_id': s['_id']},
                                    {'$push': {'dll': {str(i): dll['_id']}}}, upsert=True)
    except:
        print("An error occurred inside Radare2")


# Dispalys POIs in the Analysis box
# TODO: make sure the stuff gets properly displayed in the gui!!!!!!!!!!!!!
def getPoi(poi, poiList):
    entries = []
    for x in results_db.find():
        print(x)

    newdb = client['current_project']
    current_db = newdb['current']
    for p in current_db.find():
        for s in static_db.find():
            if s['_id'] == p.get('static_analysis', {}).get('01'):
                for r in results_db.find():
                    if r['_id'] == s.get('results').get('01'):
                        for f in function_db.find():
                            # print(len(r.get(poi.lower())[:]))
                            for i in range(len(r.get(poi.lower())[:])):
                                try:
                                    key = r.get(poi.lower())[0:][i]
                                    print(key[str(i)])
                                    if f['_id'] == key[str(i)]:
                                        self.window.POI_tableWidget.setHorizontalHeaderLabels([poi])
                                        self.window.POI_tableWidget.setColumnCount(1)
                                        content = f.get('data')
                                        print(content)
                                        entries = []
                                        # i = 0
                                        try:
                                            # for j in content:
                                            entries.append(content)
                                            # print(len(entries))
                                            self.window.POI_tableWidget.setRowCount(len(entries))
                                            self.window.POI_tableWidget.setItem(i, 0, QTableWidgetItem(str(content['name'])))
                                            self.window.POI_tableWidget.resizeColumnToContents(0)
                                            # i += 1
                                        except TypeError:
                                            pass
                                except KeyError or IndexError:
                                    pass


def deleteDatabase(self):
    db.project.drop()
    db.binary.drop()
    db.static.drop()
    db.results.drop()
    db.function.drop()
    db.string.drop()
    db.variable.drop()
    db.dll.drop()