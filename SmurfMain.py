# -*- coding: utf-8 -*-
from googlestuff import GoogleFunction
from riotstuff import RiotFunction

googleFunction = GoogleFunction()
riotFunction = RiotFunction()

# names =('Kreydawg','So Vayne')
names = googleFunction.getNames()
summonerdata = riotFunction.getData(names)
print(names)
print(summonerdata)
yikes = googleFunction.postData(summonerdata)

