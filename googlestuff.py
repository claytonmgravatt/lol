# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

class GoogleFunction :

    def getNames(self) :
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Smurf Check").sheet1
        # Extract and print all of the values
        summoners = sheet.col_values(12)
        summoners = summoners[1:]
        return summoners
    
    def getListIndex(nrow, ncol,row_pos, col_pos):
        list_pos = row_pos*ncol + col_pos
        return(list_pos)
    
    
    def postData(self, summonerdata):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Smurf Check").sheet1
        df = pd.DataFrame.from_dict(summonerdata, orient='index',columns=['Total Games','Total Win Rate','Solo Rank','Solo Games','Solo Win Rate','Flex Rank','Flex Games','Flex Win Rate','Summoner Level','Metric'])
        
        sheet.update([df.columns.values.tolist()]+df.values.tolist())


        return df
        # return 1
     
    def postMoreData(self, moredata):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Smurf Check").get_worksheet(2)
        df = pd.DataFrame(moredata,columns=['Ranked Games']) 
        
        sheet.update([df.columns.values.tolist()]+df.values.tolist())


        return df
