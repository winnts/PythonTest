# winrm set winrm/config/service @{AllowUnencrypted="true"}
# winrm set winrm/config/client '@{TrustedHosts ="[0:0:0:0:0:0:0:0]"}'.

from winrm.protocol import Protocol
import os


class WindowsRemote(object):
    def protocol(self, endpoint, username, passwd):
        return Protocol(
            endpoint='http://' + endpoint + ':5985/wsman',
            transport='ntlm',
            username=username,
            password=passwd,
            server_cert_validation='ignore')

    def download_msi(self, link, protocol):
        shell_id = protocol.open_shell()
        command_id = protocol.run_command(shell_id, 'wget', ['--content-disposition', '--no-check-certificate', link])
        std_out, std_err, status_code = protocol.get_command_output(shell_id, command_id)
        protocol.cleanup_command(shell_id, command_id)
        print(std_out, status_code)
        protocol.close_shell(shell_id)


    def install_agent(self, protocol, filename):
        shell_id = protocol.open_shell()
        command_id = protocol.run_command(shell_id, filename, ['/q'])
        std_out, std_err, status_code = protocol.get_command_output(shell_id, command_id)
        protocol.cleanup_command(shell_id, command_id)
        print(std_out, status_code)
        protocol.close_shell(shell_id)


    def find_msi(self, protocol):
        shell_id = protocol.open_shell()
        command_id = protocol.run_command(shell_id, 'dir', ['itsm*.msi', '/s', '/b'])
        std_out, std_err, status_code = protocol.get_command_output(shell_id, command_id)
        protocol.cleanup_command(shell_id, command_id)
        print(std_out, status_code)
        protocol.close_shell(shell_id)
        return std_out


link = 'https://robotauto-msp.itsm-cit.comodo.com:443/enroll/windows/msi/token/107d9a6fb63ff7022acb45f49465c57a'
remote = WindowsRemote()
p = remote.protocol()
remote.download_msi(p, link)
msi_name = remote.find_msi(p)
print msi_name
remote.install_agent(p, msi_name)
