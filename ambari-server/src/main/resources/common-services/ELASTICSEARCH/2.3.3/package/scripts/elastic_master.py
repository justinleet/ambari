"""
Elastic master file
"""


from elastic import elastic
from resource_management.core.resources.system import Execute
from resource_management.libraries.script import Script


class Elasticsearch(Script):
    def install(self, env):
        import params
        env.set_params(params)

        print 'Install the Master'
        Execute('rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch')
        Execute("echo \"[elasticsearch-2.x]\n"
                "name=Elasticsearch repository for 2.x packages\n"
                "baseurl=https://packages.elastic.co/elasticsearch/2.x/centos\n"
                "gpgcheck=1\n"
                "gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch\n"
                "enabled=1\" > /etc/yum.repos.d/elasticsearch.repo")
        Execute("yum -y install elasticsearch")

        # TODO ACTUALLY FIGURE OUT HOW TO USE THIS WITH RPM
        # self.install_packages(env)

    def configure(self, env):
        import params
        env.set_params(params)

        print 'Install plugins'
        # TODO Actually install appropriate plugins.
        # Execute("/usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head" % java_home)
        # print output
        elastic()

    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("service elasticsearch stop")
        print 'Stop the Master'
        Execute(stop_cmd)

    def start(self, env):
        import params
        env.set_params(params)

        self.configure(env)
        start_cmd = format("service elasticsearch start")
        print 'Start the Master'
        Execute(start_cmd)

    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("service elasticsearch status")
        print 'Status of the Master'
        Execute(status_cmd)


if __name__ == "__main__":
    Elasticsearch().execute()
