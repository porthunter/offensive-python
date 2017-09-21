import frida
s = frida.attach("cat")
print([x.name for x in s.enumerate_modules()])
print(s.enumerate_modules())
print s.enumerate_ranges('rw-')
print s.read_bytes(0x7fff90e04000, 300)

