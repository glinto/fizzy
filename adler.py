# In this exercise you have a function adler32(buf) which does not work properly.
# The function takes a bytearray as an argument, and it should return a 32 bit Adler
# checksum of the bytearray, but it obviously does not.
# Please modify the alder32(buf) function to do the computation properly.
# If your algorithm works, the print statement in line 13 should print True

def adler32(buf):
    return 0x00000000

test_bytes = bytearray.fromhex('5b987d106b097ebe5531fbd46756c7a8')
expected_result = 0x3a2807b2

print(expected_result == adler32(test_bytes))