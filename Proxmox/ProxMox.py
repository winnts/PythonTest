from proxmoxer import ProxmoxAPI
import time


class ProxMox(object):

    def pm_connect(self, host, user, passwd):
        return ProxmoxAPI(host, user=user, password=passwd, verify_ssl=False)

    def pm_get_node(self, connect, node_name):
        return connect.nodes(node_name)

    def pm_get_vm(self, node, vm_id):
        return node.qemu(vm_id)

    def pm_clone_vm(self, target_node, clone_vm, new_id, new_hostname):
        target_vm = self.pm_get_vm(target_node, clone_vm)
        response = target_vm.clone.create(newid=new_id, full=1, name=new_hostname, format='qcow2', storage='local')
        # print response
        status = target_node.tasks(response).status.get()
        while status['status'] == 'running':
            status = target_node.tasks(response).status.get()
            print 'Creating VM process: ' + status['status']
            time.sleep(3)
        if status['exitstatus'] == 'OK':
            print 'VM Created Successfully'
        else:
            print 'VM Creation FILED!'

    def pm_start_vm(self, target_node, vm_id):
        print 'Trying to start...'
        startup_response = target_node.qemu(vm_id).status.start.post()
        startup_status = target_node.tasks(startup_response).status.get()
        while startup_status['status'] == 'running':
            startup_status = target_node.tasks(startup_response).status.get()
            print 'Starting VM process: ' + startup_status['status']
            time.sleep(3)
        if startup_status['exitstatus'] == 'OK':
            print 'VM Started Successfully'
        else:
            print 'Starting VM FILED!'

    def pm_stop_vm(self, target_node, vm_id):
        print 'Trying to stop...'
        stop_response = target_node.qemu(vm_id).status.stop.post()
        stop_status = target_node.tasks(stop_response).status.get()
        while stop_status['status'] == 'running':
            stop_status = target_node.tasks(stop_response).status.get()
            print 'Stopping VM process: ' + stop_status['status']
            time.sleep(3)
        if stop_status['exitstatus'] == 'OK':
            print 'VM Stopped Successfully'
        else:
            print 'Stopping VM FILED!'

    def pm_delete_vm(self, target_node, vm_id):
        print 'Trying to delete...'
        delete_response = target_node.qemu(vm_id).delete()
        delete_status = target_node.tasks(delete_response).status.get()
        while delete_status['status'] == 'running':
            delete_status = target_node.tasks(delete_response).status.get()
            print 'Delete VM process: ' + delete_status['status']
            time.sleep(3)
        if delete_status['exitstatus'] == 'OK':
            print 'VM Deleted Successfully'
        else:
            print 'Delete VM FILED!'


def pm_test():
    node_name = 'pve03'
    new_id = 3043
    template_id = 254
    new_hostname = 'CIT45-WIN7-64'

    proxmox = ProxMox()
    connect = proxmox.pm_connect('', '', '')
    target_node = proxmox.pm_get_node(connect, node_name)

    proxmox.pm_clone_vm(target_node, template_id, new_id, new_hostname)
    proxmox.pm_start_vm(target_node, new_id)
    time.sleep(30)
    proxmox.pm_stop_vm(target_node, new_id)
