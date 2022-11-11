import sys
import pandas as pd
import numpy as np
import cx_Oracle

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
                    
                    data.append(("service" + str(i), item, "NONE", "service" + str(i) + "." + "item" + "." + "NONE" + str(j), "service" + str(i) + "." + "item" + "." + str(j), 1, 0, 0, 0))
                else:
                    
                    data.append(("service" + str(i), item, "NONE", "service" + str(i) + "." + "item" + "." + "NONE" + str(j), "service" + str(i) + "." + "item" + "." + str(j), 0, 1, 0, 0))
    
    #### to generate Excel file
    df1 = pd.DataFrame(data,  columns=[ 'Service_name', 'KPI', 'Sub_KPI', 'MQL', 'Alias', 'ERROR_COUNT_KPI','TOTAL_REQUEST_KPI', 'ERROR_COUNT_SUB_KPI','TOTAL_REQUEST_SUB_KPI'])
    df1.to_excel("output.xlsx")

    #### connect oracle database
    connection = cx_Oracle.connect(
        user="PYTHON",
        password="Testing123",
        dsn="localhost/orcl")

    print("Successfully connected to Oracle Database")

    cursor = connection.cursor()

    # Create a table

    cursor.execute("""
        begin
            execute immediate 'drop table excel_data';
            exception when others then if sqlcode <> -942 then raise; end if;
        end;""")
    cursor.execute("""
        create table excel_data (
            id number generated always as identity,
            Service_name varchar2(4000),
            KPI varchar2(4000),
            Sub_KPI varchar2(4000),
            MQL varchar2(4000),
            Alias varchar2(4000),
            ERROR_COUNT_KPI varchar2(2),
            TOTAL_REQUEST_KPI varchar2(2),
            ERROR_COUNT_SUB_KPI varchar2(2),
            TOTAL_REQUEST_SUB_KPI varchar2(2),
            primary key (id))""")

    cursor.executemany("insert into excel_data (Service_name, KPI, Sub_KPI, MQL, Alias, ERROR_COUNT_KPI, TOTAL_REQUEST_KPI, ERROR_COUNT_SUB_KPI, TOTAL_REQUEST_SUB_KPI) values(:1, :2, :3, :4, :5, :6, :7, :8, :9)", data)
    print(cursor.rowcount, "Rows Inserted")

    connection.commit()
    connection.close()


if __name__ == "__main__":

    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('error please correct parameter')
