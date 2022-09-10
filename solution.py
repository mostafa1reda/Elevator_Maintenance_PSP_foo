def solution(l):
    sorted_list = sorted(l, key=lambda x:tuple(map(int, x.split('.'))))
    return sorted_list

#####################
#I/O
#####################

# solution(['3.0.8','3.0','3.7.0','1.0.0','0.0.5','2.0.52'])
# solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])

#### OLD (NON Optimized) Solutions #### 
#1 --Can't handle all float numbers
"""
def solution(l):
    l.sort()
    print(l)  
"""

#2 --Handling strings just like IPV4 does, BUT does NOT return the full correct order
"""
import socket
l=['3.0.8','3.0','3.7.0','1.0.0','0.0.5','2.0.52']
def solution(l):
    sorted_list = sorted(l, key=lambda x: socket.inet_aton(x[0]))
    return sorted_list
"""    
