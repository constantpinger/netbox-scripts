###################################################################################################
#
#  Simple script to demonstrate netbox script functionality. A text box permits a MAC 
#  address to be submitted which is then output in all the main formats
#
###################################################################################################

from extras.scripts import *
from netaddr import *

class MacFind(Script):
    class Meta:
       name = "Show MAC address formats"
       description = "provides all the different formats for a given MAC address"

    class mac_comware(mac_cisco): pass
    mac_comware.word_sep = '-'
    mac_comware.word_size = 16

    class mac_procurve(mac_pgsql): pass
    mac_procurve.word_sep = '-'
    mac_procurve.word_size = 24

    # input of the MAC address in Netbox GUI. Add regex validation to improve
    mac1 = StringVar(max_length=20, label="Mac Address?", required=True)
    
    def run(self, data, commit):
        mac1 = data['mac1']
        result = printMacs(mac1)
        output = ("original: " + str(mac1))
        output = output + '\n' + ("mac_cisco: " + str(EUI(mac1, dialect = mac_cisco)))
        output = output + '\n' + ("mac_unix_expanded: " + str(EUI(mac1, dialect = mac_unix_expanded)))
        output = output + '\n' + ("mac_bare: " + str(EUI(mac1, dialect = mac_bare)))
        output = output + '\n' + ("mac_pgsql: " + str(EUI(mac1, dialect = mac_pgsql)))
        output = output + '\n' + ("mac_unix: " + str(EUI(mac1, dialect = mac_unix)))
        output = output + '\n' + ("mac_eui: " + str(EUI(mac1)))
        output = output + '\n' + ("mac_comware: " + str(EUI(mac1, dialect = mac_comware)))
        output = output + '\n' + ("mac_procurve: " + str(EUI(mac1, dialect = mac_procurve)))
        try:   #needed because easy to get an exception when a MAC isn't registered in OUI db
          output = output + '\n' + "vendor= " + (EUI(mac1).oui.registration().org)
        except Exception:
          pass
          output = output + '\n' + ("can't find MAC in database")

        return(output)
