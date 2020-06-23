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

# if Azure version less that 1.0 un-install previous versions
pip uninstall azure

# remove all previous Azure and re-install
sudo pip uninstall -y $(pip freeze | grep azure)

# Reference
https://docs.python.org/3.5/installing/index.html
https://pypi.org/project/azure-iot-device/
https://docs.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device?view=azure-python
