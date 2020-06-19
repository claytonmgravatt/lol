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
count = 0
while count < 2 :
    postinput = input('Post additional data? (careful not to exceed rate limits!) y/n:\n')
    if postinput == 'y':
        weeks = 3
        moredata = riotFunction.getMoreData(accountidlist,weeks)
        googleFunction.postMoreData(moredata)
        count = 2
    elif postinput == 'n':
        print('Exiting..')
        count = 2
    elif postinput !=('y' or 'n'):
        print('invalid input you dunce')
        count = count+1