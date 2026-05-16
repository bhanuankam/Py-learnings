import re

sitename = input("Enter region : ").upper()
pod = input("Enter podlet name : ").upper()
rack_start_raw = input("Enter Rack Range Start (e.g., r1): ").upper()
rack_end_raw = input("Enter Rack Range End (e.g., r10): ").upper()

start_num = int(re.search(r'\d+', rack_start_raw).group())
end_num = int(re.search(r'\d+', rack_end_raw).group())

prefix = re.match(r'[a-zA-Z]+', rack_start_raw).group()

for i in range(start_num, end_num + 1):
    print(f"{sitename}-{pod}-{prefix}{i}")