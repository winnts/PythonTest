# winrm set winrm/config/service @{AllowUnencrypted="true"}
# winrm set winrm/config/client '@{TrustedHosts ="[0:0:0:0:0:0:0:0]"}'.

from winrm.protocol import Protocol
import os


def download_msi(link):
    p = Protocol(
        endpoint='http://CIT10-WIN7-64:5985/wsman',
        transport='ntlm',
        username=r'admin',
        password='test',
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, 'wget', ['--content-disposition', '--no-check-certificate', link])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    print(std_out, status_code)
    p.close_shell(shell_id)


def install_agent(filename):
    p = Protocol(
        endpoint='http://CIT10-WIN7-64:5985/wsman',
        transport='ntlm',
        username=r'admin',
        password='test',
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, filename, ['/q'])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    print(std_out, status_code)
    p.close_shell(shell_id)


def find_msi():
    p = Protocol(
        endpoint='http://CIT10-WIN7-64:5985/wsman',
        transport='ntlm',
        username=r'admin',
        password='test',
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, 'dir', ['itsm*.msi', '/s', '/b'])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    print(std_out, status_code)
    p.close_shell(shell_id)
    return std_out



download_msi('https://robotauto-msp.itsm-cit.comodo.com:443/enroll/windows/msi/token/107d9a6fb63ff7022acb45f49465c57a')
msi_name = find_msi()
print msi_name
install_agent(msi_name)

# connect_and_run()
