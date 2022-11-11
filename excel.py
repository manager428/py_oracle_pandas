import sys
import pandas as pd
import numpy as np

def main(service_count, record_count):
    kpi = ["manageability", "termination", "fullfillment", "dataplaneavailability"]
    data = []
    for i in range(1, int(service_count) + 1):
        for item in kpi:
            for j in range(1, int(record_count) + 1):
                t = int(record_count) * int(service_count)
                k = ((int(record_count) * 3)/10)
                p = int(k)
                data1 = []
                if j <= p:
                    data1.append("service" + str(i))
                    data1.append(item)
                    data1.append("NONE")
                    data1.append("service" + str(i) + "." + "item" + "." + "NONE" + str(j))
                    data1.append("service" + str(i) + "." + "item" + "." + str(j))
                    data1.append(str(1))
                    data1.append(str(0))
                    data1.append(str(0))
                    data1.append(str(0))
                    print(data1)
                    data.append(data1)
                else:
                    data1.append("service" + str(i))
                    data1.append(item)
                    data1.append("NONE")
                    data1.append("service" + str(i) + "." + "item" + "." + "NONE" + str(j))
                    data1.append("service" + str(i) + "." + "item" + "." + str(j))
                    data1.append(str(0))
                    data1.append(str(1))
                    data1.append(str(0))
                    data1.append(str(0))
                    print(data1)
                    data.append(data1)
        df1 = pd.DataFrame(data,  columns=[ 'Service_name', 'KPI', 'Sub_KPI', 'MQL', 'Alias', 'ERROR_COUNT_KPI','TOTAL_REQUEST_KPI', 'ERROR_COUNT_SUB_KPI','TOTAL_REQUEST_SUB_KPI'])
        # df1.to_excel("output.xlsx")
        print(df1)

if __name__ == "__main__":

    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('error please correct parameter')
