def build_pc(cpu, memory, ssd, chipset, **parts):
    print(f'- CPU: {cpu}')
    print(f'- Memory: {memory}')
    print(f'- SSD: {ssd}')
    print(f'- ChipSet: {chipset}')
    for part_name in parts.keys():
        part_value = parts[part_name]
        print(f'- {part_name}: {part_value}')

def build_server():
    print(f'- CPU: Intel XEON E5 2478')
    print(f'- Memory: DDR4 2600 128G')
    print(f'- SSD: Samsung 990 PRO 4TB')
    print(f'- ChipSet: Intel C266 Chipset')

def build_nas():
    print(f'- CPU: Intel XEON E3 2124')
    print(f'- Memory: DDR4 2600 65G')
    print(f'- SSD: Samsung 990 PRO 2TB')
    print(f'- ChipSet: Intel C256 Chipset')
    print(f'- HDD: IRON Wolf 16TB x 4')