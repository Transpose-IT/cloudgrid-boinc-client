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

class Worker(object):
    def __init__(self, host_info):
        self.id = 0
        self.host_cpid = host_info.host_cpid
        self.cpus = host_info.p_ncpus
        self.memory = host_info.m_nbytes
        self.os_name = host_info.os_name
        self.host_name = host_info.domain_name

    def registration_status(self):
        pass
    
    def set_worker_id(self, id):
        self.id = id

    def get_worker_id(self):
        return self.id

    def get_host_cpid(self):
        return self.host_cpid

    def construct_json(self):
        data = {}
        data['hostCPid'] = self.host_cpid
        data['cpus'] = self.cpus
        data['memory'] = self.memory
        data['osName'] = self.os_name
        data['hostName'] = self.host_name
        return data