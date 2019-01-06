#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2019 Jorn Argelo, <jorn@transpose-it.nl>
#
# Cloudgrid is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cloudgrid is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cloudgrid.  If not, see <http://www.gnu.org/licenses/>.

import requests
import json
import sys

class RestService(object):
    def __init__(self, host):
        self.response = ""
        self.host = host
        self.api_version = '/v1'

    def get(self, path):
        url = self.host + self.api_version + path
        data = {}
        try:
            response = requests.get(url)
            data = json.loads(json.dumps(response.json()))
        except ValueError as e:
            print "Got ValueError: {0}".format(e)
            raise
        except:
            print sys.exc_info()[0]
            raise
        if (response.status_code != requests.codes.ok and response.status_code != requests.codes.not_found):
            raise Exception("Got error status: {0}, {1}".format(response.status_code, response.text))
        return data

    def post(self, path, jsondata):
        url = self.host + self.api_version + path
        try:
            response = requests.post(url, json=jsondata)
            data = json.loads(json.dumps(response.json()))
        except ValueError as e:
            print "Got ValueError: {0}".format(e)
            raise

        if response.status_code != requests.codes.created:
            raise Exception("Got error status: {0}, {1}".format(response.status_code, response.text))

        return data

    def put(self, path, jsondata):
        url = self.host + self.api_version + path
        try:
            response = requests.put(url, json=jsondata)
            data = json.loads(json.dumps(response.json()))
        except ValueError as e:
            print "Got ValueError: {0}".format(e)
            raise
            
        if response.status_code != requests.codes.ok:
            raise Exception("Got error status: {0}, {1}".format(response.status_code, response.text))

        return data





