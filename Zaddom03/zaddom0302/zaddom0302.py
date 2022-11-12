# Maciej Cieszyński

def unique_ip_addresses():
    with open('apache_logs', 'r') as fopen:
        lines = fopen.readlines()

    IP_list=[]

    for l in lines:
        IP_line = l.split()[0]
        if IP_line not in IP_list:
            IP_list.append(l.split()[0])
        continue

    return IP_list
    #list_IP = []
    #IP_row = lines.split()

if __name__ == '__main__':
    print(unique_ip_addresses())
