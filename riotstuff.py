# -*- coding: utf-8 -*-
import requests
import json
import time


class RiotFunction :
    key = 'RGAPI-d4f6dd7d-8ba6-447a-954d-43a6773309ef'
    
    def getData (self, summoners) :
        summonerdata = {}
        accountidlist=[]
        key = RiotFunction.key
        for summoner in summoners:
            summoner = summoner.replace(' ','%20')
            print('summoner is '+str(summoner))
            url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + str(summoner) +'?api_key=' +str(key)
            summonerinfo = requests.get(url)
            data = json.loads(summonerinfo.text)
            #print('data is '+str(data))
            try:
                summonerid = data['id']
            except:
                print('Summoner invalid! \n\n\n')
                break
            summonerlevel = data['summonerLevel']
            accountid=data['accountId']
            accountidlist.append(accountid)
            print('The account ID is '+str(accountid)+'\n')
            
            ###---------Ranked Stats---------###
            url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+str(summonerid) +'?api_key=' +str(key)
            r = requests.get(url)
            rdata = json.loads(r.text)
            rankedsolo = ''
            rankedflex = ''
            for i in rdata :
                if i['queueType']=='RANKED_SOLO_5x5' :
                    rankedsolo = i
                if i['queueType']=='RANKED_FLEX_SR' :
                    rankedflex = i
            #res
            swins = 0
            slosses = 0
            sgames = 0
            fwins = 0
            flosses = 0
            fgames = 0
            franks = 'null'
            sranks='null'
            fwr = 0
            swr = 0
            if len(rankedsolo)>2:
                swins = rankedsolo['wins']
                slosses = rankedsolo['losses']
                srank = rankedsolo['rank']
                stier = rankedsolo['tier']
                sranks = stier + ' ' + srank
                sgames = swins + slosses
                swr = swins / sgames

            if len(rankedflex)>2:
                fwins = rankedflex['wins']
                flosses = rankedflex['losses']
                frank = rankedflex['rank']
                ftier = rankedflex['tier']
                franks = ftier + ' ' + frank
                fgames = fwins + flosses
                fwr = fwins / fgames
            
            tgames = fgames + sgames
            try:
                twr = (swins + fwins)/tgames
            except:
                twr = 0
            metric = summonerlevel + tgames
            summonerdata[summoner]=((tgames,twr,sranks,sgames,swr,franks,fgames,fwr,summonerlevel,metric))
        return summonerdata,accountidlist
# summoners = 'Qp34hoyE-YSDJWdMOIwpfJrabifhEsH7swv7stf9CmYXalwB'
# test = RiotFunction.getData(0,summoners)
    def getMoreData(self,accountidlist,weeks) :
        key = RiotFunction.key
        currenttime = int(round(time.time()*1000))
        oldtime=currenttime - (604800000*weeks)
        gamesdata = []
        for account in accountidlist :
            try :
                url = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' +str(account)+'?beginTime=' + str(oldtime) +'&api_key=' +str(key)
                matchinfo = requests.get(url)
                data = json.loads(matchinfo.text)
                print('the account id is '+str(account))
                totalgames = data['totalGames']
                print('total games played in last '+str(weeks)+' week(s): ' +str(totalgames)+'\n')
                gamesdata.append(totalgames)
            except:
                print('no games found!')
                gamesdata.append(0)
        return gamesdata