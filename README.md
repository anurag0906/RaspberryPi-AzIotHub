# RaspberryPi-IotHub

# check if any azure package already installed or not. Run below commands in Terminal

pip list|grep azure
pip --version
# pip version used-  9.0.1

# To check all installed packages
pip freeze

# install IoT Package
     
|package| Command | Result|Reference|
|--|--|--|--|
|azure Iot |python -m pip install azure-iot-device |failed ||
| azure| pip install azure-mgmt-iothub==0.2.2 | failed|https://github.com/Azure/azure-sdk-for-python/blob/38b3ce0fe3fdd6dd1e607627c611b8a9c97c2372/ChangeLog.rst#2017-05-16-azure-200|
| azure mgt | pip install azure-mgmt-iothub | failed| https://pypi.org/project/azure-mgmt-iothub/0.2.2/ |
|azure device client| pip install azure-iothub-device-client | installed | https://pypi.org/project/azure-iothub-device-client/|

##azure-iot-device-2.1.3  version installed
# Install asynco for Async programming
pip install asyncio

## asynco does not works in python 2.7, upgrade to python 3.5- https://stackoverflow.com/questions/41839344/update-python-on-linux-2-7-to-3-5
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python

python --version
## python version 3.5.3

# Clean Up

## if Azure version less that 1.0 un-install previous versions
pip uninstall azure

## remove all previous Azure and re-install
sudo pip uninstall -y $(pip freeze | grep azure)


# Error - 
##AttributeError: module 'asyncio' has no attribute 'run'
## do not use Run method. use other alternatives- https://stackoverflow.com/questions/52796630/python3-6-attributeerror-module-asyncio-has-no-attribute-run

# Reference
https://docs.python.org/3.5/installing/index.html
https://pypi.org/project/azure-iot-device/
https://docs.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device?view=azure-python
