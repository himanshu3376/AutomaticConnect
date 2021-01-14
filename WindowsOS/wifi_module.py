"""
@Author: GNG2101 Group 5 - Accessible WiFi
This code is used to connect to wifi-connection 
and automatically reconnect to host Spot 
"""

"""
Import pre-built libraries into python algorithm to allow the program to
call enter commands into windows Command Prompt.
"""
"""
The argparse module also automatically generates help and usage messages,
and issues errors when users give the program invalid arguments.
The os and sys libraries allow the code to interact with the command
prompt
The time library allows the code to include time variations into the code
The algorithm imports another python file which allows the algorithm to
accept the terms and conditions of from the HTML link
"""

import os 
import sys
import argparse     
import time 
from auto_reconnect import auto_reconnect

def wifi_pipeline(FLAGS):
    """
    show the list of available networks
    and generate full pipeline
    The XML file contains the security information of the Guest-WiFi connection
    such as the password, which is extracted into the main function
    """
    ### The path to the XML file is generated in this command ###
    xml_file_path = os.path.join(os.getcwd(), "Wi-Fi-GuestWifi.xml")      
    ### The os and system libraries work together to input commands into the command prompt ###
    os.system("netsh wlan add profile filename=%s user=all"%xml_file_path)
    time.sleep(4)
    while(True):
        ### show the list of available networks ###
        os.system("netsh wlan show profiles")
        print("The current Profile chosen : %s"%FLAGS.interface_name)
        ####  show the chosen network to connect ###
        os.system("netsh wlan show profiles name=%s key=clear"%FLAGS.interface_name)
        ### disconnect to previous connected wifi ###
        os.system("netsh wlan disconnect")
        time.sleep(2)
        #### connect to specified network ###
        os.system("netsh wlan connect name=%s"%FLAGS.interface_name)
        time.sleep(5)
        #### calls the function called auto_reconnect in the auto_reconnect.py file and
        #### enforces 10 second time delay ####
        auto_reconnect()
        time.sleep(10)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface_name', type = str, 
                        default = "GuestWifi", help="Interface Name for the WIFI to be connected")
    #### The statement above specifies the SSID that the algorithm connects to ####
    FLAGS = parser.parse_args()
    #### wifi module sequence #####
    wifi_pipeline(FLAGS)
