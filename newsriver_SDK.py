import sys, os, json, time, requests
from flask import Flask, jsonify, request
import numpy as np
homeDir = os.getcwd() if os.getcwd().split('/').pop() == "vision-sdk" else os.path.join(os.getcwd(),'vision-sdk')


api_path = 'https://api.newsriver.io'
token = 'sBBqsGXiYgF0Db5OV5tAwzzfEVTj2i3frBYzgL2ELCDP1HhywHCamL5RUqFTkUF9'

# private helpers
# these are private helpers used across the api wrappers. These are private and should not be called
# directly by users
def _query (endpoint, query_params):
        return requests.get(_url(endpoint),
                            headers={'Authorization': token},
                            params='query_params'
                            )

def _url(endpoint):
    ''' _url() constructs the path for the api endpoint. It starts with api_path which is the root mattermark url
        and then concatenate with / any additional url parameters from *params '''
    url = '/'.join([api_path, endpoint])
    return  url

def _handle(resp):
    #print(resp)
    if resp.status_code != 200:
        if resp.status_code == 400:
            raise Exception('400 Bad Request – Your request was not properly sent')
        elif resp.status_code == 403:
            raise Exception('403 Unauthorized – Your API key is wrong, is no longer valid, or you do not have access to the given resource.')
        elif resp.status_code == 404:
            raise Exception('404 Not Found – The specified endpoint could not be found.')
        elif resp.status_code == 429:
            raise Exception('429 Rate Limit Exceeded – You have temporarily exceeded your rate limit. Refer to Rate Limits for more details.')
        elif resp.status_code == 500:
            raise Exception('500 Internal Server Error – We had a problem with our server. Try again later.')
        elif resp.status_code == 503:
            raise Exception('503 Service Unavailable – We’re temporarily offline for maintenance. Please try again later.')
        else:
            raise Exception('error :' + resp.status_code)

    return resp.json()


# Public Helpers
def checkHeartbeat():
    endpoint = ""
    query_params = {}
    response = _handle(_query(endpoint, query_params))
    return response

def search(queryParams):
    # debug

    # setup
    endpoint = "v2/search/"
    response = _handle(_query(endpoint, queryParams))
    return response

if __name__ == '__main__':
    # Status Check
    #pulseStatus = checkHeartbeat()
    #print(pulseStatus)
    # Search
    '''
    queryParams = {'language': 'AEN',
                    'text': 'Aethereum',
                    'sortBy': '_score',
                    'sortOrder': 'DESC'
                    }
    '''
    queryParams = {'text': 'Aethereum'}

    search = search(queryParams)
    print(search)
