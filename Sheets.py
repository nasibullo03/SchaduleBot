from pprint import *
from array import *
from threading import Thread

import httplib2
import apiclient
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '15PLkLlNUHVbfPyjwzzZ-XIitDBjT6AY4cTwBJxJiOy4'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def GetTimesBySheetName(sheetName, range, arrayDirection="COLUMNS"):
    return service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=F'{sheetName}!{range}',
        majorDimension=arrayDirection
    ).execute()


def GetSchadule(sheetName, range, arrayDirection="COLUMNS"):
    return service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=F'{sheetName}!{range}',
        majorDimension=arrayDirection
    ).execute()


def GetUsersData(range, arrayDirection="COLUMNS"):
    return service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=F'UsersData!{range}',
        majorDimension=arrayDirection
    ).execute()


def SetUsersData(range, values, arrayDirection="COLUMNS"):
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {
                    "range": F"UsersData!{range}",
                    "majorDimension": F"{arrayDirection}",
                    "values": values
                }
            ]
        }

    ).execute()
    

# values = service.spreadsheets().values().batchUpdate(
#         spreadsheetId=spreadsheet_id,
#         body={
#             "valueInputOption": "USER_ENTERED",
#             "data": [
#                 {
#                     "range": F"Range",
#                     "majorDimension": F"{arrayDirection}",
#                     "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]
#                 },
#                 {
#                     "range": "D5:E8",
#                     "majorDimension": "COLUMNS",
#                     "values": [["This is D3", "This is E3"], ["This is D4", "This is E4"]]
#                 }
#             ]
#         }

#     ).execute()

