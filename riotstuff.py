# -*- coding: utf-8 -*-
import requests
import json

class RiotFunction :
    key = 'RGAPI-c59214e1-2a82-4209-baa8-02fdb4034e3a'
    
    def getData (self, summoners) :
        summonerdata = {}
        key = 'RGAPI-c59214e1-2a82-4209-baa8-02fdb4034e3a'
        for summoner in summoners:
            url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + str(summoner) +'?api_key=' +str(key)
            summonerinfo = requests.get(url)
            data = json.loads(summonerinfo.text)
            try:
                summonerid = data['id']
            except:
                break
            summonerlevel = data['summonerLevel']
            
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
            srank = 'not'
            stier = 'found'
            sgames = 0
            fwins = 0
            flosses = 0
            frank = 'not'
            ftier = 'found'
            fgames = 0
            franks = 'null'
            fwr = 0

            if len(rankedsolo)>1:
                swins = rankedsolo['wins']
                slosses = rankedsolo['losses']
                srank = rankedsolo['rank']
                stier = rankedsolo['tier']
                sranks = stier + ' ' + srank
                sgames = swins + slosses
                swr = swins / sgames

            if len(rankedflex)>1:
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
        return summonerdata
summoners = 'Qp34hoyE-YSDJWdMOIwpfJrabifhEsH7swv7stf9CmYXalwB'
test = RiotFunction.getData(0,summoners)