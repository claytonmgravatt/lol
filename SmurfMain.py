# -*- coding: utf-8 -*-
from googlestuff import GoogleFunction
from riotstuff import RiotFunction

googleFunction = GoogleFunction()
riotFunction = RiotFunction()

# names =('Kreydawg','So Vayne')
###----- Get Names fom Spreadsheet -----###
names = googleFunction.getNames()
print(names)

###----- Get summoner information from Riot -----###
summonerstuff = riotFunction.getData(names)

summonerdata=summonerstuff[0]
accountidlist=summonerstuff[1]

googleFunction.postData(summonerdata)

###------ Run these to get Ranked Games in past X weeks-----###
weeks = 2
moredata = riotFunction.getMoreData(accountidlist,weeks)
googleFunction.postMoreData(moredata)