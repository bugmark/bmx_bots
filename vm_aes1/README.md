# VmAes1 Prospectus

This is simulation a Vulnerability Market which trades on the quesion "Will an
open AES critical vulnerability issue exist at the end of the week?"

This simulation trades a contract series called "VmAes".  Contracts in the
series may be referred to by name: "VmAes-YYWW", where YY is the contract year,
and WW is the sequential contract week numer ranging from 01 to 52.  Contracts
mature every Sunday at Midnight, and also at Jan 31 at midnight.  So as of this
writing (Mar 02, 2018), the next active contract in the series is VmAes-1805,
which matures on Sunday March 4 at midnight.

For years, AES has been a stable and secure algorithm, at the foundation of the
computer security pyramid. AES is trusted as a standard by the US Government
and numerous organizations.  The collective wisdom says that no critical
vulnerabilities will be discovered in AES.  But if the collective wisdom is
wrong, there will be billions upon billions in economic consequences.  In this
unlikely event, it will be important that the vulnerability be uncovered and
mitigated rapidly.

## The Primary Actors

The VmAes market simulation involves the following actors:

* The _Fund Manager_ (referred to as the _Manager_) is a government employee
  entrusted with investing the capital of the AES Stability Foundation, a
  public/private partnership with a mission to monitor and mitigate AES
  vulnerabilities.  

* The _Information Source_ is a renowned hacker (referred to as the _Hacker_) and a
  quasi-criminal mastermind.  

* The _Council of Experts_ (collectively known as the _Council_) is a group of
  computer security experts who review issues in the AES vulnerability tracker
  and rule on the issue severity.  

## Market Mechanisms

The Manager posts the same set of buy-unfound offers week after week, with the
expectation that the offers will not be matched because there will be no
software vulnerabilities.

But from time-to-time, the hacker *will* discover a vulnerability.  In this
case, the workflow is:

- post a matching buy-found offer to form a contract
- publish an issue to the AES vulnerability tracker
- get it classified as Critical by the Council
- wait to the end of the week
- profit

The Manager starts with a budget of 1B, and the Hacker starts with a budget of
10M.

## Trading Routine

Every Monday, all open issues are closed, all matured contracts are resolved,
and a new contract is added to the series.

Every Tuesday, the Manager will post a series of buy-unfound offers:
- tier1: 10K  @ 0.9
- tier2: 100K @ 0.7
- tier3: 1M   @ 0.5
- tier4: 10M  @ 0.3
- tier5: 100M @ 0.1

Every Wednesday, the Hacker(s) will post an offer that has a random price that
varies on a linear scale from 0.0 to 1.0, and a random volume that varies on a
logrithmic scale from 10K to 100M.

Every Thursday, new issues are posted by the Hacker.

Every Friday, the Council will classify open issues.  On average 75% of the
issues will be marked as critical, using a random-selection algorithm.

## Simulation Parameters

- SIMULATION_WEEKS
- MANAGER_OPENING_BALANCE
- HACKER_OPENING_BALANCE
- NUMBER_OF_HACKERS
- TIER1_VOLUME
- TIER1_PRICE
- TIER2_VOLUME
- TIER2_PRICE
- TIER3_VOLUME
- TIER3_PRICE
- TIER4_VOLUME
- TIER4_PRICE
- TIER5_VOLUME
- TIER5_PRICE
- ISSUE_PCT_CRITICAL

## Results Data

- End-of-Simulation DepthChart (CSV, GnuPlot Graph)
- TimeSeries Crossing Price (InfluxDataSet, Grafana Graph)
- TimeSeries Crossing Volume (InfluxDataSet, Grafana Graph)
- TimeSeries Open/Unfound by Vol/Price (InfluxDataSet, Grafana Graph)
- TimeSeries Open/Found by Vol/Price (InfluxDataSet, Grafana Graph)
- Manager and Hacker closing balances

## Simulation Questions

- How do partial offers perform?
- How does price and volume matching perform?
- How does the number of hackers change the market dynamics?
