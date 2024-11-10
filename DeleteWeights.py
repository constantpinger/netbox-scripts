######################
## Deletes all the weight field from every device type in Netbox
## Could be adjusted to remove any other field or bulk set to the same value
######################
from dcim.models import Device, DeviceType, Manufacturer, Platform
from extras.scripts import *

class BulkDeviceTypeUpdater(Script):
    class Meta:
        name = "Device Type Weight Remover"
        description = "removes the weight entry from every device type object"
    
    def run(self, data, commit):
        for deviceType in DeviceType.objects.all():
            if deviceType.weight != None:
                self.log_warning(f"{deviceType} weight was {deviceType.weight} - turning to null")
                deviceType.weight=None
                deviceType.save()
