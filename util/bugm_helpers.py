# bugm_helpers - Bugmark Helper Methods

# from subprocess import check_output
import subprocess
import json
import sys
import os

# ----- environment variable -----

def env(key, default):
  return os.getenv(key, default)

# ----- command execution -----

# Call the Bugmark CL executable, parse the 
# JSON and return a Python dictionary
#
# valid arguments:
#   string          -> df("host info")
#   string          -> df("bmx host info")
#   array of string -> df(["host", "info"])
#   array of string -> df(["bmx host", "info"])
#   array of string -> df(["bmx", "host", "info"])
 
# generate dictionary from json
def dict_from_json(text):
    return json.loads(text.decode("utf-8"))

# run and return json
def run_json(args):
    mod_args = args if isinstance(args, str) else " ".join(args)
    lcl_args = "bmx " + mod_args
    command  = lcl_args.replace("bmx bmx ", "bmx ")
    msg("Command", command)
    return subprocess.check_output(command, shell=True)

# run and return dictionary
def run_dict(args):
    return dict_from_json(run_json(args))

# ----- debug messages -----

# print a debug msg
def msg(label, text):
  debug = env('DEBUG_MODE', False)
  if debug:
    print(label + ": " + text)

# ----- utility methods -----

# generate a userspec
def userspec(email, pword = "bugmark"):
  return email + ":" + pword

