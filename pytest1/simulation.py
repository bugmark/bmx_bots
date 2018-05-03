#!/usr/bin/env python

# ----- simulation -----

import bugm_util as bugm

# ----- simulation parameters -----
unfixed_price = bugm.env('UNFIXED_PRICE', 1)
fixed_price   = bugm.env('FIXED_PRICE'  , 0)

# ----- local variables -----
simulation_days = bugm.run_dict("host info")["day_offset"] * -1
tracker_uuid       = bugm.run_dict("tracker list")[0]["uuid"]
funder          = bugm.run_dict("user list --with_email=test-funder")[0]
workers         = bugm.run_dict("user list --with_email=test-worker")
num_workers     = len(workers)

# ----- utility functions -----
def create_issue(day, idx):
  issue_id = "issue_" + str(day) + "_" + str(idx)
  opts = ["issue sync", issue_id, "--tracker-uuid="+tracker_uuid, "--status=closed"]
  issue_uuid = bugm.run_dict(opts)["uuid"]
  return issue_uuid

def create_buy_offer(issue, side, email):
    price = str(unfixed_price) if side == "unfixed" else str(fixed_price)
    opts  = ["offer create_buy",
             "--side="+side,
             "--volume=100",
             "--price="+price,
             "--issue="+issue,
             "--status=closed",
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

