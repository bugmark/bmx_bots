#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# (C) Copyright 2018
# Georg Link <linkgeorg@gmail.com>
#
# SPDX-License-Identifier: MPL-2.0

#####
# person.py
#
# Developer, investor, maintainer
# Simulates behavior of different types of people in an open source project
# Agent in this Agent-Based-Modeling simulation
#####

from subprocess import check_output
import json


class Person:
    # The most generic person, defining the interface
    # person characteristics:
    productivity = 1  # how much work this person can do in a day
    non_active_days = 0  # how many days before coming back to the community
    skills = None  # skills this person has

    def __init__(self, email, bugmark_user=None, pwd="bugmark",
                 issue_tracker=None):
        # bugmark related variables
        self.bugmark_email = email  # user account email on bugmark
        self.bugmark_password = pwd  # password on bugmark
        self.bugmark_uuid = bugmark_user  # USER_UUID on bugmark
        self.tracker = issue_tracker  # reference to the issue tracker

    def community_work(self):
        # decides to do work in community
        # e.g. close bugs
        return None

    def trade_bugmark(self):
        # decide what to trade on bugmark
        # e.g. make buy offer
        return None


class PTrivialCase1Worker(Person):
    # Worker for Trivial Case 1
    # Persona:
    #  - finds an UNFIXED offer and matches it
    def __init__(self, email, bugmark_user=None, pwd="bugmark",
                 issue_tracker=None):
        super(self.__class__, self).__init__(email, pwd, bugmark_user,
                                             issue_tracker)
        self.productivity = 10
        self.non_active_days = 0
        self.skills = 'all'
        self.bugmark_email = email  # user account email on bugmark
        self.bugmark_password = pwd  # password on bugmark
        self.bugmark_uuid = bugmark_user  # USER_UUID on bugmark
        self.tracker = issue_tracker  # reference to the issue tracker

        check_output(["bmx", "user", "create",
                      "--usermail="+email,
                      "--password=bugmark"])

    def community_work(self):
        # only do work, if has fixed position on an issue
        # eg:
        # get issues id bugmark id
        # self.tracker.issue.do_work(productivity)
        # if issue.complete >= 1.00 then issue.close()
        return None

    def trade_bugmark(self, issue, maturation, volume="20", price="1.00",
                      side="fixed"):
        # Trivial Case 1: find an open UNFIXED offer and buy it
        offer_obj = json.loads(check_output(["bmx", "offer", "list",
                                             "--with-type=Offer::Buy::Unfixed",
                                             "--limit=1"])
                               .decode("utf-8"))
        if len(offer_obj) > 0:
            # get offer ID to 'show' details and get match parameters
            offer_uuid = offer_obj[0]['uuid']
            offer_obj2 = check_output(["bmx", "offer", "show", offer_uuid])
            offer = json.loads(offer_obj2.decode("utf-8"))
            # check_output(["bmx", "offer", "create_buy",
            #               "--side=fixed",
            #               "--volume=20",
            #               "--price=0",
            #               # TODO: wait for bmx show offer to expose the issue
            #               "--issue="+offer["issue"],
            #               "--maturation=" + offer["maturation"],
            #               "--userspec="+self.bugmark_email +
            #               ":"+self.bugmark_password])
            return 1
        return None


class PTrivialCase1Funder(Person):
    # Funder for Trivial Case 1
    # Persona:
    #  - funds an issue with an UNFIXED offer
    def __init__(self, email, bugmark_user=None, pwd="bugmark",
                 issue_tracker=None):
        super(self.__class__, self).__init__(email, pwd, bugmark_user,
                                             issue_tracker)
        self.productivity = 10
        self.non_active_days = 0
        self.skills = 'all'
        self.bugmark_email = email  # user account email on bugmark
        self.bugmark_password = pwd  # password on bugmark
        self.bugmark_uuid = bugmark_user  # USER_UUID on bugmark
        self.tracker = issue_tracker  # reference to the issue tracker

        check_output(["bmx", "user", "create",
                      "--usermail="+email,
                      "--password=bugmark"])

    def community_work(self):
        # not implemented in Trivial Case 1
        return None

    def trade_bugmark(self, issue, maturation, volume="20", price="1.00",
                      side="unfixed"):
        # Trivial Case 1: create an UNFIXED offer
        offer = check_output(["bmx", "offer", "create_buy",
                              "--side=unfixed",
                              "--volume=20",
                              "--price=0",
                              "--issue="+issue,
                              "--maturation=" + maturation,
                              "--userspec="+self.bugmark_email +
                              ":"+self.bugmark_password])
        return json.loads(offer.decode("utf-8"))


class PProfitMaxizer(Person):
    # Example instantiation of a person
    # Persona:
    #  - tries to make a living with open source and bugmark
    #  - cares most about profit
    def __init__(self, email=None, pwd=None, bugmark_user=None,
                 issue_tracker=None):
        super(self.__class__, self).__init__(email, pwd, bugmark_user,
                                             issue_tracker)
        self.productivity = 10
        self.non_active_days = 0
        self.skills = 'all'

    def community_work(self):
        # only do work, if has fixed position on an issue
        # eg:
        # get issues id bugmark id
        # self.tracker.issue.do_work(productivity)
        # if issue.complete >= 1.00 then issue.close()
        return None

    def trade_bugmark(self):
        # buy largest possible contract that person has skills to fix
        # look for bugmark offers and compare to workload required on issue
        # trade on the most favorable issue
        return None
