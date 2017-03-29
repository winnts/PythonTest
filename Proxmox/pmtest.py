from proxmoxer import ProxmoxAPI
import time

node_name = 'pve03'
vm_id = 3042
template_id = 254
new_hostname = 'CIT45-WIN7-64'

proxmox = ProxmoxAPI('', user='', password='', verify_ssl=False)
# for node in proxmox.nodes.get():
#     print node
#     print node['node']
# if node.get('node') == 'pve02':
# for vm in proxmox.nodes(node['node']).qemu.get():
# print "{0}. {1} => {2}" .format(vm['vmid'], vm['name'], vm['status'])
# print ('-----------')

# node = proxmox.nodes('pve01').qemu.get()
# print node
#for vm in node:
#    print "{0}. {1} => {2}" .format(vm['vmid'], vm['name'], vm['status'])

# node.qemu.create(template='local:vztmpl/debian-6-turnkey-core_12.0-1_i386.tar.gz',
#                    hostname='turnkey',
#                    storage='local',
#                    memory=512,
#                    swap=512,
#                    cpus=1,
#                    disk=4,
#                    password='secret',
#                    ip_address='10.0.0.202')
# for node in proxmox.nodes.get():
#     print node
target_node = proxmox.nodes(node_name)
target_qemu = target_node.qemu(template_id)

response = target_qemu.clone.create(newid=vm_id, full=1, name=new_hostname, format='qcow2', storage='local')
print response
status = target_node.tasks(response).status.get()

while status['status'] == 'running':
    status = target_node.tasks(response).status.get()
    print 'Creating VM: ' + status['status']
    time.sleep(3)
if status['exitstatus'] == 'OK':
    print 'VM Created Successfully'
    print 'Trying to start...'
    startup_response = target_node.qemu(vm_id).status.start.post()
    startup_status = target_node.tasks(startup_response).status.get()
    while startup_status['status'] == 'running':
        startup_status = target_node.tasks(startup_response).status.get()
        print 'Starting VM: ' + startup_status['status']
        time.sleep(3)
    if startup_status['exitstatus'] == 'OK':
        print 'VM Started Successfully'
else:
    print 'VM Creation FILED!'
