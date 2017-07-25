"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
from ambari_commons.os_family_impl import OsFamilyImpl
from ambari_commons import OSConst
from resource_management.core.logger import Logger
from presto_client import smoketest_presto, PrestoClient

class PrestoServiceCheck(Script):
    pass

@OsFamilyImpl(os_family=OsFamilyImpl.DEFAULT)
class PrestoServiceCheckDefault(PrestoServiceCheck):
    def service_check(self, env):
        from params import config_properties, \
            host_info, coordinate_master_host
        if 'presto_worker_hosts' in host_info.keys():
            all_hosts = host_info['presto_worker_hosts'] + \
                        host_info['presto_coordinator_hosts']
            Logger.info("check work hosts " + ",".join(all_hosts))
        else:
            all_hosts = host_info['presto_coordinator_hosts']
            Logger.info("check  hosts " + ",".join(all_hosts))

        smoketest_presto(
            PrestoClient(coordinate_master_host,'root',
                         config_properties['http-server.http.port']),
            all_hosts)

@OsFamilyImpl(os_family=OSConst.WINSRV_FAMILY)
class PrestoServiceCheckWindows(PrestoServiceCheck):
    def service_check(self, env):
        pass

if __name__ == "__main__":
    PrestoServiceCheck().execute()
