#!/usr/bin/env python

from scapy.all import *
from time import sleep
from random import choice
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = ['UB40 Red Red wine',
           'Orange origina',
	   'Lets follow the yellow brick road',
           'Going rather green',
           'Look at the blue sky',
           'some wonderful violet flowers',
           'white like a ghost',
           'Cyan cat is coming',
           'my face is going purple',
           'magenta, what kinda colour is that',
           'my nan had oldlace',
           'tickle me pink',
           'warmwhite is that such a colour?',]

def send_tweet():
    twitter.update(message(status))
def arp_detect(pkt):
    if pkt[ARP].op == 1: #network request
        if pkt[ARP].hwsrc == 'xx:xx:xx:xx:xx:xx'
                return send_tweet
