# -*- coding: utf-8 -*-

#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "Leave at 2210 to make it on time"

# your twitter consumer and access information goes here

apiKey = 'mRkfhZVyZuB3VTEnVPh7DAjAH'
apiSecret = 'QJSHUmX7nsb37VMusUmXFprPBxc2kSy7TxoQ8ZU7AWBp8VTHbx'
accessToken = '905804860465041412-S0icGPhe27tksfefzLE31bAffAowl6Y'
accessTokenSecret = 'evvGoo3wwGdiSC5wl1fiZgFJ6VRXxH8qs2zgKvPEcFmUU'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
