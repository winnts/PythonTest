import WindowsRemote


class WindowsRemoteMethods(object):
    @staticmethod
    def download_agent_to_host(hostname, link):
        agent = WindowsRemote()
        protocol = agent.protocol(hostname, '', '')
        agent.download_msi(protocol, link)

    @staticmethod
    def install_agent_on_host(hostname):
        agent = WindowsRemote()
        protocol = agent.protocol(hostname, '', '')
        file_name = agent.find_msi(protocol)
        agent.install_agent(protocol, file_name)
