'''
Written by Andrew Ravn
Last Updated: Sept132018
'''

import datetime
from cedato.Authenticate import Authenticate as auth
from cedato.IVT_BL_ProtectedMedia.PM_Cedato_Filters import Filter as flt
from cedato.IVT_BL_ProtectedMedia.BL_Alignment_Update import AlignmentUpdate as aln
from cedato.IVT_BL_ProtectedMedia.Protected_Media_Report_Reader import ProtectedMedia as pm

def pm_cedato_main():
    currentDate = datetime.datetime.now().strftime("%Y%m%d")
    previousHour = str(int(datetime.datetime.now().strftime('%H')) - 1)
    report_date = currentDate + "-" + previousHour
    token = auth().authentication()
    with open("sensitive_demand_list.txt", 'r') as data:
        sensitive_list = sorted([row.strip('\n') for row in data])
    pm_data = flt().manipulateProtectedData(pm().read_report(report_date),sensitive_list)
    left_ind = 0
    right_ind = 1
    for vastId in sensitive_list:
        while True:
            if pm_data[right_ind]['l3'] == vastId:
                right_ind += 1
            else:
                black_list = [bundle['l4'] for bundle in pm_data[left_ind:right_ind]]
                aln().updateLists(token,vastId,black_list)
                left_ind=right_ind
                right_ind += 1
                break

if __name__ == '__main__':
    pm_cedato_main()
    print("done")
