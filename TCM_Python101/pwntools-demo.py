#!/bin/python3
# Pwntools
# Meistsec 10/2022

from pwn import *
# the * means all

print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh())
print(hexdump(asm(shellcraft.sh())))

#automating local services
#p = process("/bin/sh")
#p.sendline("echo hello;")
#p.interactive()

##automating remote services
##r = remote("127.0.0.1", 1234)
##r.sendline("hello")
##r.interactive()
##r.close()

print(p32(0x13371337))
print(hex(u32(p32(0x13371337))))

l = ELF('/bin/bash')

print(hex(l.address))
print(hex(l.entry))

print(hex(l.got['write']))
print(hex(l.plt['write']))

for address in l.search(b'/bin/sh\x00'):
	print(hex(address))

print(next(l.search(asm('jmp esp'))))

r = ROP(l)
print(r.rbx)

print(xor(xor("A","B"), "A"))
print(b64e(b"test"))
print(b64d(b"dGVzdA=="))
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))

print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))