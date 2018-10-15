import os
from api import client
from nltk import sent_tokenize
from random import choice
import datetime

buch_chosen = ''
path = './src/'
files = []

for filename in os.listdir(path):
    files.append(filename)
files.remove('.gitignore')


# Methoden:
def get_random_satz():
    global buch_chosen
    buch_chosen = str(choice(files))
    with open(path+buch_chosen, 'rt') as fin:
        buchtext_gesamt = fin.read().decode('utf-8')
    sent_tokenize_list = sent_tokenize(buchtext_gesamt)
    ein_random_satz = choice(sent_tokenize_list)
    return ein_random_satz


def check_satz(p_satz):
    if len(p_satz) < 15 or len(p_satz) > 280 or p_satz[0] == ')':
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
    fout.write('\n'+str(datetime.datetime.now())+'\t'+buch_chosen+'\t'+satz)
