# config_my_station.py
# Python script to configure radiosonde_auto_rx and chasemapper
# Designed for use on a Raspberry Pi

import os
import re
import sys

# Custom station configuration text file.
my_config_file = 'my_station.txt'

# Regular expression for key=value
config_param_re = re.compile('(\w+)\s*\=\s*(.+)')

# Dictionary of configuration parameters.
config_params = {}


##############################################################################
# Functions.
############################################################################## 

#-----------------------------------------------------------------------------
def close_file(fd):
    """
    Unconditionally close a file and ignore errors.
    """
    try:
        fd.close()
    except Exception:
        pass

#-----------------------------------------------------------------------------
def open_file(file_name, open_type='r'):
    """
    Open a file and return a file object.
    """
    fd = None
    open_type_str = 'writing' if open_type == 'w' else 'reading'
    try:
        fd = open(file_name, open_type)
    except Exception as err:
        print('Error opening {} for {}: {}'.format(file_name, open_type_str, str(err)))
        close_file(fd)
    return fd

#-----------------------------------------------------------------------------
def update_config_file(config_file):
    """
    Update the application configuration file.
    """
    global config_params
    
    config_lines = []
    
    # Make sure configuration file exists.
    if not os.path.isfile(config_file):
        print('Config file {} not found.'.format(config_file))
        return
    
    # Open the configuration file and read it into memory.
    # Look for configuration parameters in dictionary and set them if found.
    print('File: {}'.format(config_file))
    fd = open_file(config_file)
    if fd is None: return
        
    for line in fd:
        line = line.strip()
        
        # Look for keyword in configuration file line.
        m = config_param_re.match(line)
        if m:
            key = m.group(1)
            if key in config_params.keys():
            
                # Configuration keyword found.  Set it.
                line = '{}={}'.format(key, config_params[key])
                print('  {}'.format(line))
                
        config_lines.append(line)
    close_file(fd)
    
    # Write the altered file back.
    fd = open_file(config_file, 'w')
    if fd is None: return
        
    for line in config_lines:
        fd.write('{}\n'.format(line)) 
    close_file(fd)
    return


##############################################################################
# Main program.
############################################################################## 
if __name__ == "__main__":

    # Make sure configuration file exists.
    if not os.path.isfile(my_config_file):
        print('Config file {} not found.'.format(my_config_file))
        sys.exit(1)
        
    # Read the configuration file.
    # Create a dictionary of config parameters.
    fd = open_file(my_config_file)
    if fd is None:
        sys.exit(1)
        
    for line in fd:
        m = config_param_re.match(line.strip())
        if m:
            key = m.group(1)
            value = m.group(2)
            config_params[key] = value
    close_file(fd)
    
    # Update the radiosonde_auto_rx configuration file.
    update_config_file(r'./radiosonde_auto_rx/auto_rx/station.cfg')
    
    # Update the chasemapper configuration file.
    update_config_file(r'./chasemapper/horusmapper.cfg')
            
    