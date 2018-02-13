#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# (C) Copyright 2018
# Georg Link <linkgeorg@gmail.com>
#
# SPDX-License-Identifier: MPL-2.0

#####
# run.py
#
# Trivial Case 1 - no variables
#####

from subprocess import check_output
import json
# import issuetracker
import person
import datetime

# Step 1: define the simulation parameters
# number_of_people = 10  # how many people we start with
# number_of_issues = 10  # how many issues we start with
# rate_of_new_issues = 3  # create x new issues every day
worker_starting_funds = 100  # how much money a worker starts with
funder_starting_funds = 999999999  # how much money a funder starts with
# file_for_issue_tracker_oracle = "./issues.csv"  #where to export the issue...
# ... tracker information to
simulation_time = 100  # how many days to simulate
# ...
# rebuild server in the past
check_output(["bmx", "host", "rebuild",
              "--affirm=destroy_all_data",
              "--with_day_offset=-"+str(simulation_time)])

# Step 2: load issue tracker
# tracker = issuetracker.IssueTracker()
# for i = 1 to number of issues
# tracker.open_issue()  # (x10)
issues = 0
# create simulation repository
print("reset bugmark")
repo_name = "TrivialCase1Repo"
repo_rtn = check_output(["bmx", "repo", "create",
                         repo_name,
                         "--type=Test"])
repo_obj = json.loads(repo_rtn.decode("utf-8"))
repo_uuid = repo_obj["uuid"]

# Step 3: instantiate people (agents)
# Trivial Case 1 only has one funder
print("create funder")
email = "funder@bugmark.net"
funder = person.PTrivialCase1Funder(email)

# list of workers = new worker (x10)
print("create workers")
workers = []
for w in range(10):
    email = "worker"+str(w)+"@bugmark.net"
    workers[w] = person.PTrivialCase1Worker(email)


# Step 4: run simulation
# First: create 10 issues, create an unfixed offer, match by a worker
# Second: advance time by one day and pay out contracts
# end after simulation_time is expired
# return to First.
for x in range(simulation_time):
    print("simulation step "+str(x))
    # get current system time
    host_rtn = check_output(["bmx", "host", "info"])
    host_obj = json.loads(host_rtn.decode("utf-8"))
    server_time = host_obj["host_time"][:-3]+host_obj["host_time"][-2:]
    host_time = datetime.datetime.strptime(server_time, "%Y-%m-%dT%H:%M:%S%z")
    maturation_datetime = host_time + datetime.timedelta(days=1)
    maturation = maturation_datetime.strftime("%y%m%d_%H%M")

    # create 10 of each: new issues, unfixed offers, and fixed offers
    for i in range(10):
        # new issue
        issues = issues + 1
        issue_rtn = check_output(["bmx", "issue", "sync",
                                  str(issues),
                                  "--type=Test",
                                  "--repo-uuid="+repo_uuid])
        issue_obj = json.loads(issue_rtn.decode("utf-8"))
        issue_uuid = issue_obj["uuid"]

        # funder
        funder.trade_bugmark(issue_uuid, maturation)

        # worker
        workers[i].trade_bugmark(issue_uuid, maturation)

    # Advance server time by one day
    check_output(["bmx", "host", "increment_day_offset"])
    # This should pay out maturing contracts
