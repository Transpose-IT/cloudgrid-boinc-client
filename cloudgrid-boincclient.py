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


from client import BoincClient
from cloudgrid.boincservice import RestService
from cloudgrid.workers import Worker
from cloudgrid.projects import Project
from cloudgrid.tasks import Task

import sys

def connect_to_boinc(host, password):
    bc = BoincClient(host, password)
    bc.get_cc_status() # Needed to setup the connection properly
    return bc

def verify_worker_registration(rest, worker):
    response = rest.get('/client/workers/' + worker.get_host_cpid())

    if response['results'] == 0:
        response = rest.post('/workers/', worker.construct_json())
        worker.set_id(response['id'])

def update_tasks_stats(bc, rest):
    tasks = bc.get_results()
    for t in tasks:
        task = Task(t)

        get_response = rest.get('/client/tasks/' + task.get_wu_name())
        if get_response['results'] == 0:
            response = rest.post('/tasks/', task.construct_json())
            print "Registered new task: " + task.get_wu_name()
        else:
            response = rest.put('/client/tasks', task.construct_json())
            print "Updated stats for task: " + task.get_wu_name()

def update_project_stats(bc, rest):
    projects = bc.get_project_status()
    for p in projects:
        project = Project(p)
        response = rest.put('/client/projects', project.construct_json())
        print "Updated project stats for: " + project.get_project_name()


if __name__ == '__main__':
    host = sys.argv[1]
    password = sys.argv[2]
    rest_endpoint = sys.argv[3]

    bc = connect_to_boinc(host, password)
    rest = RestService(rest_endpoint)

    host = bc.get_host_info()
    worker = Worker(host_info=host)
    verify_worker_registration(rest, worker)

    update_tasks_stats(bc, rest)
    update_project_stats(bc, rest)