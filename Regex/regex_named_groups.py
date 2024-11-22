import re

def extract_info_sysdescr_oidval(sysdescr_val):
    """
    This function extracts tokens out of the CPE sysDescr oid value using the following text pattern:
    <<HW_REV: (); VENDOR: (); BOOTR: (); SW_REV: (); MODEL: ()>>
    """
    try:
        sysdescr_val_dict = dict()
        sysdescr_pattern = r".*?<<HW_REV: (?P<hardware_version>.*?); VENDOR: (?P<manufacturer>.*?); BOOTR: (?P<bootr>.*?); SW_REV: (?P<software_version>.*?); MODEL: (?P<model>.*?)>>.*"
        data_match = re.search(sysdescr_pattern, sysdescr_val)
        if data_match:
            sysdescr_val_dict = data_match.groupdict()
    except Exception as e:
        print(f"Error occurred axtracting fields out of sysDescr oid: {e}")
    return sysdescr_val_dict


sys_descr = "ARRIS DOCSIS 3.1 Gateway / Retail <<HW_REV: 1; VENDOR: ARRIS Group, Inc.; BOOTR: 6.2.32.703059; SW_REV: 01.05.020.13.NCS; MODEL: G34>>"

print(extract_info_sysdescr_oidval(sys_descr))