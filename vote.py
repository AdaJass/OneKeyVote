import asyncio
import aiohttp
import random

n=0
async def request(votes, radius):
    global n
    # votes=1000
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Cookie': 'Hm_lvt_7c7df1a66b4676c14801e0451caf5d0e=1464858746,1464859310,1464860713,1465962410; Hm_lpvt_7c7df1a66b4676c14801e0451caf5d0e=1465962918',
        'Referer': 'http://m.yijian.tv/share/newvctopinfo?id=106'
        }
    url='http://m.yijian.tv/share/newvctopinfo?id=106'
    voteurl='http://m.yijian.tv/project/vote?vid=2&oid=106&token='
    # while True:        
    for i in range (votes):
        sleeptime=int(radius*random.random())
        
        print('sleep for ',sleeptime, 'seconds')
        with aiohttp.ClientSession() as session:            
            async with session.get(url, headers=headers) as resp:
                # n=n+1 
                # if n%200 ==0:
                # with open('resp.html','w',encoding='utf-8') as f:
                #     f.write()
                res = await resp.text(encoding='utf-8')
                findstr='oid&token='
                start = res.find(findstr, 240)
                token = res[start+len(findstr):start+len(findstr)+32]
                print(token, ' the token')
                await asyncio.sleep(sleeptime)
                async with session.get(voteurl+token) as r:
                    print(await r.text(encoding='utf-8'))
                    await asyncio.sleep(sleeptime)
                    async with session.get('http://m.yijian.tv/share/newvctop') as rss:
                        await asyncio.sleep(sleeptime)

                      
    pass

if __name__=='__main__':    
    loop = asyncio.get_event_loop()
    votes= 1000 # input('你想投几票？:\n')
    votes=int(votes)
    radius= 5   #input('程序需要通过随机的睡眠时间模仿人类随机投票，请输入睡眠时间的大致时长，以秒为单位（建议在5~10秒之间）：\n')
    radius=int(radius)    
    tasks =[request(votes, radius)]     
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 

