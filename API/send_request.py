import json
import requests
import base64

class send_request(object):
    def get_token(self, url, inner_json, header, cert, cert_key):
        r = requests.post(url, data=json.dumps(inner_json),  headers=header, cert=(cert, cert_key), verify=True)
        print r.text
        print r.status_code
        return r.text

    def parse_json(self, resp):
        data = json.loads(resp)
        return data

    def get_installer_link(self, link_url, link_inner_json, header):
        link = requests.post(link_url, json=link_inner_json, headers=header)
        # print link.text
        print link.status_code
        return link.text


def api_get_token():
    url = 'https://demo-api.one.comodo.com/auth/login'
    cert = '/home/adyachenko/certs_1/itsm-cit_comodo_com_client_bundle.cer'
    cert_key = '/home/adyachenko/certs_1/itsm-cit_comodo_com.key'
    user = 'user'
    password = 'VoCDRcN4ngTu4b5crzmwAYnQbKL42UzrfV01'
    inner_json = {"username": "user", "password": "egGv2XF6hvjOnogSuyNPXClNZFK33d"}
    authentication_data = base64.b64encode(user + ':' + password)
    header = {'content-type': 'application/json',
                'ache-control': 'no-cache',
                'authorization': 'Basic ' + authentication_data}
    conn = send_request()
    response = conn.parse_json(conn.get_token(url, inner_json, header, cert, cert_key))
    print "accessTokenExpiresAt: ", response['accessTokenExpiresAt']
    print "tokenType: ", response['tokenType']
    print "refreshToken: ", response['refreshToken']
    print "accessToken: ", response['accessToken']
    return response['refreshToken']


def api_get_installer_link(access_token):
    link_url = 'https://sprint43cit5msp-msp.itsm-cit.comodo.com'
    api_url = '/api/rest/v1/bulk-installation-package/download'
    header = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'x-auth-type': "4",
        'x-auth-token': "d2a7e65e909e4f0e72f2a7b6f5055fd3809ddde4"
        }
    link_inner_json = {"company_id": 3, "device_group_id": 6, "user_id": 3,
                       "install_ccs": 1, "install_ccc": 0, "windows_profile_id": 24, "os_type": 1}
    link_conn = send_request()
    response = link_conn.parse_json(link_conn.get_installer_link(link_url+api_url, link_inner_json, header))
    print response['download_path']
    return response


def download_installer(download_url):
    url = 'https://sprint43cit5msp-msp.itsm-cit.comodo.com'
    local_filename = download_url['download_path'].split('/')[-1]
    r = requests.get(url+download_url['download_path'], stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print local_filename
    return local_filename


download_installer(api_get_installer_link(api_get_token()))
