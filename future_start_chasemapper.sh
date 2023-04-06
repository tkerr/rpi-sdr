#!/bin/bash
# For future use when Chasemapper configuration is complete.
# Note that running Chasemapper as a systemd service will likely
# interfere with the auto_rx service.
systemctl enable chasemapper.service
systemctl start chasemapper.service

