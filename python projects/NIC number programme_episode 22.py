nic="20051234567"
if len(nic)==9:
    print(f'Your NIC has {len(nic)} digits.Your NIC card number is vaild.')
else:
    if len(nic)==11:
        print(f'Your NIC has {len(nic)} digits.Your NIC card number is valid.')
    else:
        print(f'Your NIC has {len(nic)} digits.Your NIC card number is invaild!')

nic1="123456789"
if len(nic1) == 9 or len(nic1) == 11:
    print(f'Your NIC has {len(nic1)} digits.Your NIC card number is vaild.')
else:
    print(f'Your NIC has {len(nic1)} digits.Your NIC card number is invaild!')