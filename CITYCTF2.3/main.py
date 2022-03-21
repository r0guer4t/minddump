from machine import UART
import machine
import _thread
import time
uart = UART(1,115200)
print('-- UART Serial --')
print('>', end='')
def uartSerialRxMonitor(command):
    recv=bytes()
    while uart.any()>0:
        recv+=uart.read(1)
    res=recv.decode('utf-8')
    erase_len=len(command)+5
    res = res[erase_len:]
    return res#configure as SoftAP+station mode
send='AT+CWMODE=3'
uart.write(send+'\r\n')
time.sleep(1)
#Set SoftAP name
send='AT+CWSAP="CITYCTF 2","",11,0,3'
uart.write(send+'\r\n')
time.sleep(1)
res=uartSerialRxMonitor(send)
print(res)
#enable multi connection mode
send='AT+CIPMUX=1'
uart.write(send+'\r\n')
time.sleep(1)
res=uartSerialRxMonitor(send)
print("Configured as Dual mode ->" + res)
# Enable the TCP server with port 80,
send='AT+CIPSERVER=1,80'
uart.write(send+'\r\n')
time.sleep(2)
res=uartSerialRxMonitor(send)
print("Server configured successfully-> "+res)
#temperature reading
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)#Here the code runs indefinitely 
while True:
    #temperature reading
    reading_temp = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading_temp - 0.706)/0.001721
    #Place basic code for HTML page display
    val='<head><title>CITY CTF 2.3 <a href="file:///flag.py">THE CHALLENGE</a></title></head><body><p>Temperature is: '+str(int(temperature))+' deg'+'</p></body>'
    print(val)
    length=str(len(val))
    
    send='AT+CIPSEND=1,'+length
    uart.write(send+'\r\n')
    time.sleep(2)
    res=uartSerialRxMonitor(send)
    print("Data sent-> "+res)
    send=val
    uart.write(send+'\r\n')
    time.sleep(10)