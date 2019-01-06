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

class Task(object):
    def __init__(self, task_info):
        self.id                 = 0
        self.wu_name            = task_info.wu_name
        self.project_url        = task_info.project_url
        self.report_deadline    = task_info.report_deadline
        self.received_time      = task_info.received_time
        self.ready_to_report    = task_info.ready_to_report
        self.final_elapsed_time = task_info.final_elapsed_time
        self.state              = task_info.state 
        self.estimated_time     = task_info.estimated_cpu_time_remaining
        self.elapsed_time       = task_info.elapsed_time
        self.completed_time     = task_info.completed_time
       
    def set_task_id(self, id):
        self.id = id

    def get_task_id(self):
        return self.id

    def get_wu_name(self):
        return self.wu_name

    def construct_json(self):
        data = {}
        data['wuName'] = self.wu_name
        data['projectUrl'] = self.project_url
        data['reportDeadline'] = self.report_deadline
        data['receivedTime'] = self.received_time
        data['readyToReport'] = self.ready_to_report
        data['finalElapsedTime'] = self.final_elapsed_time
        data['state'] = self.state
        data['estimatedTime'] = self.estimated_time
        data['elapsedTime'] = self.elapsed_time
        data['completedTime'] = self.completed_time
        return data