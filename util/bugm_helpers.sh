#!/usr/bin/env bash

# BUGMARK BOT RUNNER FRAMEWORK

# STEP1) ADD THESE LINES TO YOUR BOT RUNNER
#
# BASEDIR=$(dirname "$0")
# source $BASEDIR/../util/bugm_helpers.sh
# 
# STEP 2) DEFINE A PARAMS FUNCTION THAT LISTS EVERY SIMULATION PARAMETER
# 
# STEP 3) DEFINE A SEPARATE FUNCTION FOR EACH TRIAL 
# - must use the 'function' notation !!
# - include one-line trial docco as a comment after the function name
# - define the trial parameters in the function
# 
# STEP 4) DEFINE A BOT FUNCTION
# - runs the simulation trial
# - caches results for the trial
# 
# STEP 5) DEFINE A RESULTS FUNCTION
# - shows the cached results for each trial
# 
# STEP 6) CALL THE SIMULATION RUNNER
# `run_simulation_and_show_results $@`
# 
# COMMAND-LINE RUNNER USAGE:
# $ run help                  -> list each simulation trial with one-line docco
# $ run                       -> run the simulation with default parameters
# $ run <trial1>              -> run trial1
# $ run <trial1> ... <trialN> -> run multiple trials...
#
# -------------------------------------------------------------------------

reset_params() {
  unset TRIAL_NAME
  for var in params
  do
    unset $var
  done
}

# -------------------------------------------------------------------------

abort() {
  echo "Usage: run <trial1 | trial2 | long_trial>"
  exit 1
}

error() {
  echo "ERROR: unrecognized option ($1)"
}

# -------------------------------------------------------------------------

show_help() {
  [ "$1" == "help" ] || return
  echo "USAGE: run [<option1> .. <optionN>]"
  echo "trial options:"
  grep "^function" $0 | sed -e "s/function /  - /g" | sed -e "s/()//g" | column -t -s '#'
  exit
}

# -------------------------------------------------------------------------

has_func() {
  grep "^function" $0 | cut -f 2 -d ' ' | sed -e "s/()//g" | grep "^$1$"
}

validate_arguments() {
  for trial_name in "$@"
  do
    if [ ! $(has_func $trial_name) ]; then
      echo "ERROR: not recognized ($trial_name)"
      show_help help
    fi
  done
}

run_bot() {
  reset_params
  if [ "$#" == "0" ]; then
    export TRIAL_NAME=default
    echo "----- Running Default Bot -----"
    bot   # run bot
  else
    for trial_name in "$@"
    do
      export TRIAL_NAME="$trial_name"
      echo "----- Running Bot for $TRIAL_NAME -----"
      $trial_name   # setup simulation parameters
      bot           # run bot
    done
  fi
}

show_results() {
  reset_params
  if [ "$#" == "0" ]; then
    export TRIAL_NAME=default
    echo "----- Default Simulation Results -----"
    results
  else
    for trial_name in "$@"
    do
      export TRIAL_NAME="$trial_name"
      echo "----- Simulation Results for $TRIAL_NAME -----"
      $trial_name   # setup simulation parameters
      results       # show results
    done
  fi
}

# -------------------------------------------------------------------------

run_simulation_and_show_results() {
  show_help          $1
  validate_arguments $@
  bmx cache clear
  run_bot            $@
  show_results       $@
}

