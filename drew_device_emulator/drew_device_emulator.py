from bluetooth import *
import os, sys
import tkinter
from PIL import Image, ImageTk
from threading import Thread
import time

ON = bytes([0xCC, 0xAA, 0x03, 0x01, 0x01, 0x01])
OFF = bytes([0xCC, 0xAA, 0x03, 0x01, 0x01, 0x00])
GET_STATE = bytes([0xCC, 0xAA, 0x03, 0x12, 0x01, 0x13])
ON_STATE = bytes([0xCC, 0xAA, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01])
OFF_STATE = bytes([0xCC, 0xAA, 0x03, 0x01, 0x01, 0x00, 0x00, 0x00])

mode = 0

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('+%d+%d' % (100,100))
        self.root.title('DREW Device Emulator')
        self.last = -1
        self.image = None
        self.old_label_image = None
        self.update_image()
        self.root.mainloop()

    def update_image(self):
        global mode
        if (self.last != mode):
            try:
                image = None
                if mode == 0:
                    image = Image.open('light_off.jpg')
                else:
                    image = Image.open('light_on.jpg')
                self.root.geometry('%dx%d' % (image.size[0],image.size[1]))
                tkpi = ImageTk.PhotoImage(image)
                self.image = tkpi
                label_image = tkinter.Label(self.root, image=tkpi)
                label_image.place(x=0,y=0,width=image.size[0],height=image.size[1])
                if self.old_label_image is not None:
                    self.old_label_image.destroy()
                self.old_label_image = label_image         
            except Exception:
                # This is used to skip anything not an image.
                # Image.open will generate an exception if it cannot open a file.
                # Warning, this will hide other errors as well.
                pass
        self.last = mode
        self.root.after(100, self.update_image)


def bt_init():
    global mode

    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "SampleServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )
                       
    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)



    try:
        while True:
            data = client_sock.recv(1024)
            if data == OFF:
                print("OFF")
                mode = 0
                client_sock.send(data)
            elif data == ON:
                print("ON")
                mode = 1
                client_sock.send(data)
            elif data == GET_STATE:
                print("GET_STATE")
                if mode == 1:
                    client_sock.send(ON_STATE)
                    client_sock.send(bytes([0x00]))
                elif mode == 0:
                    client_sock.send(OFF_STATE)
                    client_sock.send(bytes([0x00]))
            
    except IOError:
        print("IOError encountered, passing")
        pass

    print("disconnected")

    client_sock.close()
    server_sock.close()
    print("all done")


print("Executing Bluetooth thread")
t1 = Thread(target=bt_init)
t1.daemon = True
t1.start()

print("Executing Image display thread")
app=App()

#t1.join()