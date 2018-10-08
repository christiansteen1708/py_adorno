# py_adorno
Twitterbot to post daily quotes from german philosopher and sociologist Theodor W. Adorno.

No source files included.

# Sourcefiles: 
Put sourcefiles in \./src/ named "1" to "20" (Adorno GS has 20 books).


# API-Access via birdy
twitter-api in api.py:
```
  from birdy.twitter import UserClient
  client = UserClient(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      ACCESS_TOKEN,
                      ACCESS_TOKEN_SECRET)
```                      
                 