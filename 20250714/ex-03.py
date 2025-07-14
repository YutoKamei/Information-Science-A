import secrets

bitlength = [512, 1024, 2048, 4096]

for b in bitlength:
    rn = secrets.randbits(b)
    print(f'{b}bit: {len(str(rn))}')
