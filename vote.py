import asyncio
import aiohttp
import random

n=0
async def request(votes):
    global n
    # votes=1000
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }
    url='http://m.yijian.tv/share/newvctopinfo?id=106'
    voteurl='http://m.yijian.tv/project/vote?vid=2&oid=106&token='
    # while True:        
    for i in range (votes):
        sleeptime=int(5*random.random())+5
        await asyncio.sleep(sleeptime)
        print('sleep for ',sleeptime, 'seconds')
        with aiohttp.ClientSession() as session:            
            async with session.get(url, headers=headers) as resp:
                # n=n+1 
                # if n%200 ==0:
                # with open('resp.html','w',encoding='utf-8') as f:
                #     f.write()
                res = await resp.text(encoding='utf-8')
                findstr='var token = "'
                start = res.find(findstr, 240)
                token = res[start+len(findstr):start+len(findstr)+32]

                # print(token, ' the token')

                async with session.get(voteurl+token) as r:
                    print(await r.text(encoding='utf-8'))
                      
    pass

if __name__=='__main__':    
    loop = asyncio.get_event_loop()
    votes=input('你想投几票？:\n')
    votes=int(votes)
    tasks =[request(votes)]     
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 

