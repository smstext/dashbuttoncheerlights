#!/usr/bin/env python

import socket
import struct
import binascii
import datetime
from time import sleep
from random import choice
import tweepy

consumer_key        = 'enter here'
consumer_secret     = 'enter here'
access_token        = 'enter here'
access_token_secret = 'enter here'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                          socket.htons(0x0003))
MAC = 'dashmac here'

while True:
    packet = rawSocket.recvfrom(2048)

    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack('!6s6s2s', ethernet_header)

    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack('2s2s1s1s2s6s4s6s4s', arp_header)

    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue

    source_mac = binascii.hexlify(arp_detailed[5])
    dest_ip = socket.inet_ntoa(arp_detailed[8])

    if source_mac == MAC:
        print "Dash button pressed!, IP = " + dest_ip
        api.update_status(my_message)
        print (my_message)



