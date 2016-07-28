"""
Elastic service script.

"""

# from resource_management import *
# import resource_management
from resource_management.libraries.script import Script
from resource_management.core.resources.system import Execute
from slave import slave


class Elasticsearch(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Slave'
        Execute('rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch')
        Execute("echo \"[elasticsearch-2.x]\n"
                "name=Elasticsearch repository for 2.x packages\n"
                "baseurl=https://packages.elastic.co/elasticsearch/2.x/centos\n"
                "gpgcheck=1\n"
                "gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch\n"
                "enabled=1\" > /etc/yum.repos.d/elasticsearch.repo")
        Execute("yum -y install elasticsearch")
        # self.install_packages(env)

    def configure(self, env):
        import params
        env.set_params(params)
        slave()

    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("service elasticsearch stop")
        Execute(stop_cmd)
        print 'Stop the Slave'

    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("service elasticsearch start")
        Execute(start_cmd)
        print 'Start the Slave'

    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("service elasticsearch status")
        Execute(status_cmd)
        print 'Status of the Slave'


if __name__ == "__main__":
    Elasticsearch().execute()
