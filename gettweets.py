from twitter import *


def getinput_sanitycheck():
#considered only few channels
    news_dict = {1:"cnnbrk", 2:"nytimes", 3:"Reuters", 4:"TIME", 5:"BBCNews", 6:"mashable"}
    for key, val in news_dict.items():
        print(key ,":-> ", val )
    print("Please type the correspong channel Number to get the tweets")
    while True:
        news_val= int(input("Enter the Channel Number or -1 to Stop: "))
        if(news_val == -1):
            break
        else:
            while news_val not in news_dict:
                if(news_val == -1):
                    break
                print("Entered is a Invalid number : Enter nummber between 1 to 6")
                news_val= int(input("Enter the Channel Number 1 to 6 ... or -1 to Stop: "))
            else:
                #print(news_dict[news_val])
                printtweets(news_dict[news_val])


def printtweets(screenname):

    twitter_pass = authentication()
    print("The latest 10 tweets on **",screenname,"** are")
    lis_tweets = twitter_pass.statuses.user_timeline(screen_name=screenname, count=10)
    for tweet in lis_tweets:
        print(tweet["text"]+'\n')
    

def authentication():
    token = "1335829488-wzLHStB2RYDgY9VAXmB2A8OGUlFHsSbLhm6AFcZ"      # info from the Twitter site.
    token_key = "T8Dz2gt3jad1AEyROp7zIKlstd4ZQMfntaQb2RkWehcio"
    con_secret = "nkSgT39MctaDCzqoLKrzhVuno"
    con_secret_key = "YaCmgAYxPxLk04gf4tXAttzcVT4eyhSkPeDqCLdmVntGA05iLm"
                
    twitter_access = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))   # oauth using creds

    return twitter_access
    
getinput_sanitycheck()



