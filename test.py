import serial
# ser=serial.Serial(“/dev/ttyUSB0”,9600,timeout=0.5)
ser=serial.Serial('COM3',9600,timeout=0.5)
print( ser.name)    #列印裝置名稱
print(ser.port)     #列印裝置名
ser.close()         #關閉埠
ser.open()          #開啟埠
strInput = 'enter some words:' 
ser.write(strInput)  #向埠寫資料
ser.close()         #關閉埠
# data = ser.read(20) #是讀20個字元

# data = ser.readline() #是讀一行，以/n結束，要是沒有/n就一直讀，阻塞。