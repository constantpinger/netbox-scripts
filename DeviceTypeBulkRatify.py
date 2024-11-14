## scripts to modify device type objects in netbox so they are compatible with the default ingestion from IP Fabric

from dcim.models import Device, DeviceType, Manufacturer, Platform
from extras.scripts import Script

class ConvertDeviceTypeNameToLowercase(Script):
    class Meta:
        name = "Convert DeviceType Names to Lowercase"
        description = "Changes the name of every DeviceType object to lowercase."

    def run(self, data, commit):
        for device_type in DeviceType.objects.all():
            # Convert the name to lowercase
            new_name = device_type.model.lower()

            # If the name is already lowercase, skip it
            if device_type.model == new_name:
                continue
            
            # Update the model name and save
            device_type.model = new_name
            device_type.save()
            
            # Log each change made
            self.log_success(f"Updated DeviceType '{device_type}' name to '{new_name}'")
            
class ConvertDeviceTypeSlug(Script):
    class Meta:
        name = "Remove manufacturer from slug"
        description = "Remove the string juniper- from start of every device type slug"
    
    def run(self, data, commit):
        for device_type in DeviceType.objects.all():
            if device_type.slug.startswith("juniper-"):
                self.log_warning(f"{device_type.slug} is wrong should be {device_type.slug[8:]}")
                device_type.slug = device_type.slug[8:]
                device_type.save()
                self.log_success(f"{device_type.slug} is fixed ")
            
