#!/usr/bin/python3

#-----------------------------------------------------------------------
# *** This script is for renewing the cloud vhmc lease time ***
#
#
#  Created On: 09/Nov/2022
#  Created By: Saikumar Srigiriraju (ssrigiriraju@rocketsoftware.com)
#-----------------------------------------------------------------------


import requests, sys, json
from datetime import date
import getopt
import time
import urllib3
urllib3.disable_warnings()
sys.tracebacklimit=0
from datetime import datetime


## colour codes
BLUE        = '\033[94m'
GREEN       = '\033[92m'
RED         = '\033[91m'
BOLD        = '\033[1m'
UNDERLINE   = '\033[4m'
END         = '\033[0m'


def print_help():
    """Prints command line options and exits"""

    print("""
Usage:
------
        ./renew_vhmc_lease_time.py -u <IBM id> -p <Password> -n <vhmc name> [-h]

Short Options:
--------------
        -u : Provide the IBM id
        -p : Provide the IBM id password
        -n : Provide the vhmc name
        -h : help

Additional Info:
----------------
        Contact :- Saikumar Srigiriraju (ssrigiriraju@rocketsoftware.com)
""")
    sys.exit()



def renew_vhmc_lease_time(USERNAME, USERPASS, HMC_NAMES):
    """
    This function is for renewing the cloud vhmc lease time.
    """
    # API end points.
    AUTH_ENDPOINT = "https://vhmccloud.isst.aus.stglabs.ibm.com/services/ldap/login"
    RENEW_VHMC_ENDPOINT = "https://vhmccloud.isst.aus.stglabs.ibm.com/services/renew"

    headers = {"Content-Type":"application/json"}

    DATA = {'email': USERNAME, 'password': USERPASS}
    JD = json.dumps(DATA)

    print()
    print(str(datetime.now()).split('.')[0], ": Validating the given credentials ...", end=" ")

    def generate_session_id():

        # post request for validating the given credentials
        AUTH_RES = requests.post(AUTH_ENDPOINT, headers=headers, data=JD, verify=False)

        # Verifying/validating the API response
        if AUTH_RES.json()['success'] == True:
            return AUTH_RES.json()['sessionid']
        else:
            print("Failed")
            print(AUTH_RES.json())
            sys.exit(-1)


    SESSION_ID = generate_session_id()
    print("Passed")

    API_INPUT_DATA = {"vm_name": None,"email": None,"sessionid": None}

    for i in HMC_NAMES.split(','):

        print(str(datetime.now()).split('.')[0], ": Renewing the relase time for" , i, "...", end=" ")

        API_INPUT_DATA['vm_name']   = i
        API_INPUT_DATA['email']     = USERNAME
        API_INPUT_DATA['sessionid'] = SESSION_ID

        test_jd = json.dumps(API_INPUT_DATA)

        # post request for generating the  pesh password(s)
        RENEW_RES = requests.post(RENEW_VHMC_ENDPOINT, headers=headers, verify=False, data=test_jd)

        if RENEW_RES.json()['error'] == False:
            print("Passed")
        else:
            print("Failed")
            print(RENEW_RES.json())

    else:
        print(str(datetime.now()).split('.')[0], ": Finished.")
        sys.exit(0)

def main(argv):

    # Global variables
    global USER_NAME, USER_PASSWORD, HMC_NAMES

    USER_NAME       = ""
    USER_PASSWORD   = ""
    HMC_NAMES       = ""

    opts, args = getopt.getopt(argv, "hu:p:n:")

    for opt, arg in opts:

        if opt == '-h':
            print_help()
        if opt == '-u':
            USER_NAME = arg
        if opt == '-p':
            USER_PASSWORD = arg
        if opt == '-n':
            HMC_NAMES = arg


    if USER_NAME == "":
        print()
        print("Option: -u is missing.")
        print_help()

    if USER_PASSWORD == "":
        print()
        print("Option: -p is missing.")
        print_help()

    if HMC_NAMES == "":
        print()
        print("Option: -n is missing.")
        print_help()


    # If all the required values received calling the functon
    if USER_NAME and USER_PASSWORD and HMC_NAMES:
        renew_vhmc_lease_time(USER_NAME, USER_PASSWORD, HMC_NAMES)
    else:
        print_help()
        sys.exit(-1)


if __name__ == "__main__":
    main(sys.argv[1:])
