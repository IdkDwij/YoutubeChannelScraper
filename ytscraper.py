# A SocialBlade Alternative but bad?

from googleapiclient.discovery import build

# Create YouTube Object
youtube = build('youtube', 'v3',
                developerKey='ima not giving u my id')

print("A SocialBlade Alternative but bad? \n")

whattodo = input("Type (id) to search or type (search) to search channels: ")

if whattodo == "id":
    idis = input("enter channel id: ")
    ch_request = youtube.channels().list(
    part='statistics',
    id=idis)
    ch_response = ch_request.execute()
    global sub  
    global vid  
    global views
    sub  = ch_response['items'][0]['statistics']['subscriberCount']
    vid  = ch_response['items'][0]['statistics']['videoCount']
    views = ch_response['items'][0]['statistics']['viewCount']

    print("Total Subscriber:- ", sub)
    print("Total Number of Videos:- ", vid)
    print("Total Views:- ", views)

elif whattodo == "search":
    search_query = input("channel name: ")
    request = youtube.search().list(q=search_query,part='snippet',type='channel')
    res = request.execute()
    from pprint import PrettyPrinter
    pp = PrettyPrinter()
    print('Total items : ',len(res['items']))
    i = 1
    x = 1
    for item in res['items']:
        print(i,".",item['snippet']['title'])
        i += 1

    for item in res['items']:
        print(x,".",item['snippet']['channelId'])
        x += 1
else:
    print("incorrect option")
