'''
Created on 2016/06/21

@author: samejima
'''
import re

'''

Return "False" when the "line" in the logfile is not corresponding to
the specified "container_list".
'''
def extractCPU(logline, container_list, cpu_list):
    
    find_flag = False
    
    for i in range(len(container_list)):
        # The line is corresponding to the container.
        if logline.startswith(container_list[i]):
            log = logline.split()
            cpu = log[1]
            cpu_list[i].append(cpu)
            return True 
        
def showCPUinTime(time_list, web_cpu, db_cpu, memcached_cpu):

    # Show header
    print "time, ",
    for i in range(len(web_cpu)):
        print "web" + str(i) +", ",
    for i in range(len(db_cpu)):
        print "db" + str(i) +", ",
    for i in range(len(memcached_cpu)):
        print "memcached" + str(i) +", ",
    
    
    
if __name__ == "__main__":
    db_container = ["6fcb7d6556d0"]
    memcached_container =["a807a17d1bd8"]
    web_container = ["942b37b9b20c"]
    
    db_cpu = [[]] * len(db_container)
    memcached_cpu = [[]] * len(memcached_container)
    web_cpu = [[]] * len(web_container)
    time_list = []
    
    logfile = open('./data/log.data')
    logline = logfile.readline() 
     
    while logline:
        sec = re.match('(^\d+)\sseconds', logline)
        if sec:
            time_list.append(sec.group(1))
        else:
            if extractCPU(logline, db_container, db_cpu):
                if extractCPU(logline, memcached_container, memcached_cpu):
                    if extractCPU(logline, web_container, web_cpu):
                        break
        logline = logfile.readline()
    logfile.close

    showCPUinTime(time_list, web_cpu, db_cpu, memcached_cpu)

