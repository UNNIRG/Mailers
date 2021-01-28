#!/usr/bin/env python3
import psutil

def check_cpu():
    """Checks Cpu percentage"""
    return psutil.cpu_percent(1) > 70
 