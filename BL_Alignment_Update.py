'''
Written by Andrew Ravn
Last Updated: Sept132018
'''
import requests, json, itertools

class AlignmentUpdate(object):

    def __init__(self):
        super().__init__()

    def updateLists(self, token, demand_id, new_list):

        def getdemandListID(token, demand_id):
            payload = {}
            header = {
                'accept': 'application/json',
                'api-version': '1',
                'authorization': 'Bearer {0}'.format(token)
            }
            report_url = 'https://api.cedato.com/api/demand/{0}?group_by=domain_lists'.format(demand_id)
            response = requests.get(report_url, data=payload, headers=header)
            data = json.loads(response.text)['data']['demand']['domain_lists']
            return data

        def combineLists(token, list_id, new_list):
            payload = {}
            header = {
                'accept': 'application/json',
                'api-version': '1',
                'authorization': 'Bearer {0}'.format(token)
            }
            report_url = 'https://api.cedato.com//api/lists/{0}/domains'.format(list_id)
            response = requests.get(report_url, data=payload, headers=header)
            data = json.loads(response.text)['data']['domains']
            return list(set(itertools.chain(data, new_list)))

        def patchList(token, list_id,list_name, black_list):
            payload = {
                'name': list_name
            }
            for i in range(len(black_list)):
                payload['list_items'+'['+str(i)+']'] = black_list[i]
            header = {
                'accept': 'application/json',
                'api-version': '1',
                'authorization': 'Bearer {0}'.format(token)
            }
            report_url = 'https://api.cedato.com/api/lists/{0}'.format(list_id)
            response = requests.patch(report_url, data=payload,headers=header)
            if response.status_code != 200:
                print("List id " + str(list_id) + " didn't update as expected, returned http code " + str(response.status_code))
            return response

        demand_list_info = getdemandListID(token, demand_id)
        return patchList(token,demand_list_info[0]['id'],demand_list_info[0]['name'],combineLists(token,demand_list_info[0]['id'],new_list))

