#!/usr/bin/env python3.6
import json
import sys
import requests
import os
from optparse import OptionParser

def listRepos(url):
    # Query registry for catalog
    response = requests.get(url + "/v2/_catalog", verify=False)
    # Handle errors
    if response.status_code != 200:
        print("Error: Catalog not available")
        exit(1)
    # Filter repositories info from previous query
    repos = response.json()['repositories']

    # Prints repositories list beautifully
    print(json.dumps(repos, indent=4, sort_keys=True))

def listTags(url, repo):
    # Query registy for repo tags list
    response = requests.get(url + "/v2/" + repo + "/tags/list", verify=False)
    # Handle errors
    if response.status_code != 200:
        print("Error: Repository not available")
        exit(1)
    # Filter tags info from previous query
    tags = response.json()['tags']

    # Prints tags beautifully
    print(json.dumps(tags, indent=4, sort_keys=True))

def userArgs():
    # Handles command line options
    help = OptionParser(usage="Usage: %prog")
    
    help.add_option("-s", "--server", dest="userServer", action="store", help="Specify docker registry URL", metavar="http://SERVER:5000")
    help.add_option("-r", "--repository", dest="userRepo", action="store", help="Specify repository to list", metavar="REPOSITORY")

    (options, args) = help.parse_args()

    return options

def main():

    # Registry URL
    url = os.getenv("DOCKER_REGISTRY")

    # Sanity check
    if not userArgs().userServer and not url:
        print("Missing server URL")
        print("Set DOCKER_REGISTRY or use '-s'")
        exit(1)

    if userArgs().userServer and not userArgs().userRepo:
        listRepos(userArgs().userServer)
    elif not userArgs().userRepo:
        listRepos(url)

    if userArgs().userRepo and userArgs().userServer:
        listTags(userArgs().userServer, userArgs().userRepo)
    elif userArgs().userRepo and not userArgs().userServer:
        listTags(url, userArgs().userRepo)

if __name__ == "__main__":
    main()