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

message = ['UB40 Red Red wine #cheerlights',
           'Orange origina #cheerlights',
	   'Lets follow the yellow brick road #cheerlights',
           'Going rather green #cheerlights',
           'Look at the blue sky #cheerlights',
           'some wonderful violet flowers #cheerlights',
           'white like a ghost #cheerlights',
           'Cyan cat is coming #cheerlights',
           'my face is going purple #cheerlights',
           'magenta, what kinda colour is that #cheerlights',
           'my nan had oldlace #cheerlights',
           'tickle me pink #cheerlights',
           'warmwhite is that such a colour? #cheerlights',]

def send_tweet():
    twitter.update(message(status))
def arp_detect(pkt):
    if pkt[ARP].op == 1: #network request
        if pkt[ARP].hwsrc == 'xx:xx:xx:xx:xx:xx':
            try:
                send_tweet

                sleep 50
