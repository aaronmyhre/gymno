import sys, os, json, time, requests
from flask import Flask, jsonify, request
import numpy as np
homeDir = os.getcwd() if os.getcwd().split('/').pop() == "vision-sdk" else os.path.join(os.getcwd(),'vision-sdk')

class FalconSDK (object):

    def __init__ (self):
        self.api_path = 'https://api.cityfalcon.com'
        self.token = '1e10536d1f045cd9706ed5e583c24a443573a6d4e67dda06b31d48fb4bdefc20'

    # private helpers
    # these are private helpers used across the api wrappers. These are private and should not be called
    # directly by users
    def _query (self, endpoint, query_params):
            query_params = dict({'access_token': self.token}, **query_params)
            r =  requests.get(self._url(endpoint),
                                params=query_params
                                )
            print(r.url)
            print(r.status_code)
            return r

    def _url(self, endpoint):
        ''' _url() constructs the path for the api endpoint. It starts with api_path which is the root mattermark url
            and then concatenate with / any additional url parameters from *params '''
        url = '/'.join([self.api_path, endpoint])
        print(url)
        return  url

    def _handle(self, resp):
        print(resp)
        if resp.status_code != 200:
            if resp.status_code == 400:
                raise Exception('400 Bad Request – Your request was not properly sent')
            elif resp.status_code == 401:
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
                raise Exception('error :' + str(resp.status_code))

        return resp

    # Public Helpers
    def checkHeartbeat(self):
        endpoint = ""
        query_params = {}
        response = self._handle(self._query(endpoint, query_params))
        return response

    def stories(self,queryParams):
        # debug

        # setup
        endpoint = "v0.2/stories"
        response = self._handle(self._query(endpoint, queryParams))
        return response.json()

if __name__ == '__main__':

    fdk = FalconSDK()
    # Status Check
    pulseStatus = fdk.checkHeartbeat()
    print(pulseStatus)

    # Search
    queryParams = {'identifier_type': 'assets',
                    'identifiers':'bitcoin',
                    'categories': 'mp',
                    'time_filter': 'd1',
                    }
    stories = fdk.stories(queryParams)
    print(stories)
