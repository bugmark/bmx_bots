#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# (C) Copyright 2018
# Georg Link <linkgeorg@gmail.com>
#
# SPDX-License-Identifier: MPL-2.0

#####
# bot.mozfest2017.py
#
# At MozFest 2017, Andy Leak developed a bot that would randomly create
# buy offers on Bugmark.
# This bot is a recreation in Python and using the Bugmark CLI.
#
#####

from subprocess import check_output
import json
import random
# import time
import datetime

# possible maturation dates: array of dates determine by ???
maturations = json.loads(check_output(["bmx", "host", "next_week_ends",
                                      "--strftime=%Y%m%d_%H%M"])
                         .decode("utf-8"))
# possible users: manually enter array of users and passwords
users_obj = json.loads(check_output(["bmx", "user", "list",
                                    "--with_email=test"])
                       .decode("utf-8"))
users = [x['email'] for x in users_obj]
password = "bugmark"
# possible issues: arrary of first three issues from Bugmark
issues_obj = json.loads(check_output(["bmx", "issue", "list",
                                     "--limit=3"])
                        .decode("utf-8"))
issues = [x['uuid'] for x in issues_obj]
# pssible volumes: array of increments of 5 from 30 to 50
volumes = [x*5 for x in range(6, 11)]
# possible prices: array of increments of .05 from .05 to 0.95
prices = [round(x*.05, 2) for x in range(1, 20)]
# possible sides: array with values 'fixed' and 'unfixed'
sides = ['fixed', 'unfixed']


# function buy
# random combination of user, issue, volume, price, and side
def buy():
    secure_random = random.SystemRandom()
    new_offer = check_output(["bmx", "offer", "create_buy",
                              "--side="+secure_random.choice(sides),
                              "--volume="+str(secure_random.choice(volumes)),
                              "--price="+str(secure_random.choice(prices)),
                              "--issue="+str(secure_random.choice(issues)),
                              "--maturation=" +
                              secure_random.choice(maturations),
                              "--userspec="+secure_random.choice(users) +
                              ":"+password])
    new_offer_uuid = json.loads(new_offer.decode("utf-8"))["offer_uuid"]
    check_output(["bmx", "contract", "cross", new_offer_uuid,
                 "--commit-type=expand"])


# output
ttime = datetime.time()
print("----- BUGMARK OFFER BOT -------------------------------------------")
print("START "+ttime.strftime("%H:%M:%S")+" | C-c to exit")
print("Process Name: bot_buy")
print("Loading Environment...")

for x in range(1, 100):
    ttime = datetime.time()
    buy()
    open_offers = json.loads(check_output(["bmx", "offer", "list"])
                             .decode("utf-8"))
    contracts = json.loads(check_output(["bmx", "contract", "list"])
                           .decode("utf-8"))
    escrows = json.loads(check_output(["bmx", "escrow", "list"])
                         .decode("utf-8"))
    print("Cycle: "+str(x)+" | " +
          ttime.strftime("%H:%M:%S")+" | " +
          len(open_offers)+" open offers | " +
          len(contracts)+" contracts | " +
          len(escrows)+" escrows")
    # if x < 50:
    #     time.sleep(5)
    # else:
    #     time.sleep(20)
    #
ttime = datetime.time()
print("Terminating after 99 cycles "+ttime.strftime("%H:%M:%S"))
