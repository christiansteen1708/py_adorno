# py_adorno
Twitterbot to post daily quotes from German philosopher and sociologist Theodor W. Adorno.
No source files included.

## dependency:
py_adorno depends on [nltk](https://github.com/nltk/nltk) for sentence segmentation.

## Sourcefiles:
Put sourcefiles in \./src/.

## API-Access via birdy
twitter-api in api.py:
```
  from birdy.twitter import UserClient
  client = UserClient(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      ACCESS_TOKEN,
                      ACCESS_TOKEN_SECRET)
```                      
