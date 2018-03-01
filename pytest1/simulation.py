#!/usr/bin/env python

# ----- simulation -----

import bugm_util as bugm

# ----- local variables -----
simulation_days = bugm.run_dict("host info")["day_offset"] * -1
repo_uuid       = bugm.run_dict("repo list")[0]["uuid"]
funder          = bugm.run_dict("user list --with_email=funder")[0]
workers         = bugm.run_dict("user list --with_email=worker")
num_workers     = len(workers)

# ----- utility functions -----
def create_issue(day, idx):
  issue_id = "issue_" + str(day) + "_" + str(idx)
  opts = ["issue sync", issue_id, "--repo-uuid="+repo_uuid]
  issue_uuid = bugm.run_dict(opts)["uuid"]
  return issue_uuid

def create_buy_offer(issue, side, email):
    price = "0" if side == "unfixed" else "1"
    opts  = ["offer create_buy",
             "--side="+side,
             "--volume=100",
             "--price="+price,
             "--issue="+issue,
             "--maturation_offset=hours-4",
             "--userspec="+bugm.userspec(email)]
    offer_uuid = bugm.run_dict(opts)["offer_uuid"]
    return offer_uuid

def take_offer(offer_uuid, email):
    opts          = ["offer take", offer_uuid, "--userspec="+bugm.userspec(email)]
    contract_uuid = bugm.run_dict(opts)["contract_uuid"]
    return contract_uuid

# ----- main simulation -----
for day in range(simulation_days):
  for idx in range(num_workers):
    issue_uuid    = create_issue(day, idx)
    offer_uuid    = create_buy_offer(issue_uuid, "unfixed", funder["email"])
    contract_uuid = take_offer(offer_uuid, workers[idx]["email"])
  bugm.run_json("host increment_day_offset")
  contracts = bugm.run_dict("contract list")
  for contract in contracts:
      bugm.run_json(["contract resolve", contract["uuid"]])

