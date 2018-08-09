from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv
import re

API_KEY = "aVTa2dOaSVCLR3zlJFI1DDbrP"
API_SECRET = "SQJFFvtkibPz4OxAcLH0YQBCDWSVGTl7PbwG1OQSDR3S51TXq7"
ACCESS_TOKEN = "2220632238-FoeRegXJWmi1leCqXhc8xv9H2HeuRORXrgMyGrc"
ACCESS_TOKEN_SECRET = "OpBJBOtRMVYPNU1lyT19kOy2tE2KlWbH5c7LIRKTNjg7S"


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        all_data  = json.loads(data)
        if 'text' in all_data:
            tweet         = all_data["text"]
            created_at    = all_data["created_at"]
            retweeted     = all_data["retweeted"]
            username      = all_data["user"]["screen_name"]
            user_tz       = all_data["user"]["time_zone"]
            user_location = all_data["user"]["location"]
            user_coordinates   = all_data["coordinates"]
		  
            print(tweet)
            polaridade = ["","positivo", "negativo", "neutro"]
            print(polaridade)
            x = int(input())
            if x!=0:
                
                tweet = self.preprocessamento(tweet)
                inserir = [tweet,created_at,retweeted,username,user_tz,user_location,user_coordinates, polaridade[x]]
                with open(r'TweetsPoliticos.csv', 'a') as data:
                    writer = csv.writer(data)
                    writer.writerow(inserir)
            return True
        else:
            return True

    def on_error(self, status):
        print(status)

    def preprocessamento(self, instancia):
        #remove links, pontos, virgulas,ponto e virgulas dos tweets
        #coloca tudo em minusculo        
        instancia = re.sub(r"http\S+", "", instancia).lower().replace(',',' ').replace('.','').replace(';','').replace('-','').replace(':','').replace('!','').replace('?','').replace('"','')
        #instancia = re.sub(r"@\S+", "", instancia)
        #instancia = re.sub(r"#\S+", "", instancia)
        instancia =instancia.replace('rt','')

        instancia =instancia.replace('á','a')
        instancia =instancia.replace('à','a')
        instancia =instancia.replace('â','a')

        instancia =instancia.replace('é','e')
        instancia =instancia.replace('è','e')
        instancia =instancia.replace('ê','e')

        instancia =instancia.replace('í','i')
        instancia =instancia.replace('ì','i')
        instancia =instancia.replace('î','i')

        instancia =instancia.replace('ó','o')
        instancia =instancia.replace('ò','o')
        instancia =instancia.replace('ô','o')

        instancia =instancia.replace('ú','u')
        instancia =instancia.replace('ù','u')
        instancia =instancia.replace('û','u')

        instancia =instancia.replace('ç','c')

        instancia =instancia.replace('ã','a')
        instancia =instancia.replace('õ','o')
        
        

        
        return (instancia)
    

    

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, l, tweet_mode='extended')
    stream.filter(track=['Lula'], languages = ["pt"])