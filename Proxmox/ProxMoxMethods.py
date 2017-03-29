from ProxMox import *


class ProxMoxMethods(object):

    @staticmethod
    def proxmox_clone_vm_from_template(node_name, template_id, new_id, new_hostname):
        proxmox = ProxMox()
        connect = proxmox.pm_connect('', '', '')
        target_node = proxmox.pm_get_node(connect, node_name)
        proxmox.pm_clone_vm(target_node, template_id, new_id, new_hostname)

    @staticmethod
    def proxmox_start_vm(node_name, vm_id):
        proxmox = ProxMox()
        connect = proxmox.pm_connect('', '', '')
        target_node = proxmox.pm_get_node(connect, node_name)
        proxmox.pm_start_vm(target_node, vm_id)

    @staticmethod
    def proxmox_stop_vm(node_name, vm_id):
        proxmox = ProxMox()
        connect = proxmox.pm_connect('', '', '')
        target_node = proxmox.pm_get_node(connect, node_name)
        proxmox.pm_stop_vm(target_node, vm_id)

    @staticmethod
    def proxmox_delete_vm(node_name, vm_id):
        proxmox = ProxMox()
        connect = proxmox.pm_connect('', '', '')
        target_node = proxmox.pm_get_node(connect, node_name)
        proxmox.pm_delete_vm(target_node, vm_id)
