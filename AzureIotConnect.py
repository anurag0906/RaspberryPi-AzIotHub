import os,uuid
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient


## uncomment below line to read documentation of this package
#help(IoTHubDeviceClient)

# Code for IoT Hub integration

async def main():

    # connection string
    conn_str = "HostName=surveillance-pi.azure-devices.net;DeviceId=Rasp-pi-device01;SharedAccessKey=Xc48DrtVlFUTyGLRcmtfwQ1Jxhvj7JzjATkPV7PTxQY="

    # Create instance of the device client using the ashagun provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message("This is a message that is being sent from Raspberry Pi")
    print("Message successfully sent!")

    # finally, disconnect
    await device_client.disconnect()


if __name__ == "__main__":
    #asyncio.run(main())
    ## above line of code works for python 3.6 or higher

 # If using Python 3.6 or below, use the following code instead of asyncio.run(main()):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


