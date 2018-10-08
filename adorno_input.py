from api import client
from nltk import sent_tokenize
from random import choice
from random import randint
import datetime

buch = ''


# Methoden:
def get_random_satz():
    global buch
    buch = str(randint(1, 20))
    with open('./src/'+buch, 'rt') as fin:
        buchtext_gesamt = fin.read().decode('utf-8')
    sent_tokenize_list = sent_tokenize(buchtext_gesamt)
    ein_random_satz = choice(sent_tokenize_list)
    return ein_random_satz


def check_satz(p_satz):
    if len(p_satz) < 15 or len(p_satz) > 280:
        return False
    else:
        return True


def tweet(p_satz):
    response = client.api.statuses.update.post(status=p_satz)


# Main
satz = get_random_satz().encode('utf-8')
while not(check_satz(satz)):
    satz = get_random_satz().encode('utf-8')

tweet(satz)

# log
with open('log', 'at') as fout:
    fout.write(str(datetime.datetime.now())+'\t'+buch+'\t'+satz+'\n')
