"""
inout.py

The turkey problem.
"""

import sys;

pounds = int(input("How many pounds does the turkey weigh? "))
minutes = int(input("How many minutes per pound? "))

total = pounds * minutes
h = total // 60
m = total % 60

print(f"That's {total} minutes, or {h} hours and {m} minutes.")
sys.exit(0)
