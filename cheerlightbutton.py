#!/usr/bin/env python

from scapy.all import *
import datetime
import logging
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

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

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

my_message = choice(message)

def send_tweet():
    twitter.update(my_message(status))

def button_pressed_dash():
  print 'Dash button pressed at %s' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
  send_tweet
  sleep(60)

def udp_filter(pkt):
  options = pkt[DHCP].options
  for option in options:
    if isinstance(option, tuple) and 'requested_addr' in option:
      mac_to_action[pkt.src]()
      break

mac_to_action = {'FC:65:DE:55:69:C3' : button_pressed_dash}
mac_id_list = list(mac_to_action.keys())

print "Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)

if __name__ == "__main__":
  main()
