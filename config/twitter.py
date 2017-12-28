from tweepy import OAuthHandler, StreamListener, Stream
import time

ckey = 'ynzofTNureE7RhFMZxAwNy89d'
csekret = '56Ri5GNjVhtbSTHg0L7A9hGwQrfYviopL1P1c6YbIcUMNfjpjS'
atoken = '946264936447016960-BUv2UjokDf0CL5VxUzSprvpZ8TqLLwV'
asecret = 'KzTx15ngGDLh1Tlf0W86Ni08paEvftU6ia8s7vTbYI9Te'


class Listener(StreamListener):
    def on_data(self, data):
        try:
            tweeter = data.split(',"text":"')[1].split('","source')[0]
            print(tweeter)
            saveThis = str(time.time()) + '::' + tweeter
            saveFile = open("data.csv", 'a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print("failed on_data, {}".format(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csekret)
auth.set_access_token(atoken, asecret)
tweet = Stream(auth, Listener())
tweet.filter(track=["Bali"])
