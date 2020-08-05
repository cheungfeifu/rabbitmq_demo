

from RabbitmqHandler import RabbitmqHandler

push_handle = RabbitmqHandler('你的虚拟主机名称')


for i in range(10):
    '''
    do something 
    '''
    push_handle.push(i)



push_handle.close()