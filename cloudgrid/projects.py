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

class Project(object):
    def __init__(self, project_info):
        self.id = 0
        self.project_name = project_info.project_name
        self.project_credits = project_info.user_total_credit
        
    def set_project_id(self, id):
        self.id = id

    def get_project_id(self):
        return self.id

    def get_project_name(self):
        return self.project_name

    def construct_json(self):
        data = {}
        data['projectName'] = self.project_name
        data['projectCredits'] = self.project_credits
        return data