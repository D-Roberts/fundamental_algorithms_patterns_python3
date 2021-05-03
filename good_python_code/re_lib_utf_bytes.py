"""
The re library.
"""

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)

print(match.group())

# \w matches word chars a-zA-Z0-9_
# \W matches  non-word chars

# meta-characters do not match themselves ?[]()^$ + { | \ .

str = 'purple alice-b@google.com monkey dishwasher'

# ^ match beg; $ match end
match = re.search(r'$fo', 'foo')
# print(match.group())

# + : 1 or more characters to its left
# re.search((r'o+', 'foo'))

# *: 0 or more charas to its left

# ?: 1 or 0 chars to its leeft

match = re.search(r'f?', 'foo')
print(match.group()) # f


# \s one or more espacese

# . any char but \n

# 3 digits with zero or more spaces
re.search(r'\d\s*\d\s*\d', '1   2 3')

# r'[\w.]' matchs any cahr in the []; . is itself now
# r'([\w.])@([\w.])'  froms logical groups you can get

# [a-z] chars in range
# [^ab] except ab

# re.findall(r'pat', str) finds all 

# subsittituion
re.sub(r'pat', replacement, str)

"""
Big, little and native endianness.
Python depends on the machine it is run on.

Bytes

Encoding
"""

import struct

import sys

print(sys.byteorder) #little on my PC

# endianness > or ! for big; < for little and ~ for native; applies for byte sequences

# struct perfroms conversions from C types to Python objects (structs from C represented as seq of bytes in Python)
# note that an int can take 2, 4 or 8 bytes in Python depending on the type in C
# endianness matters in this case

print(struct.pack('hhl', 1, 2, 3))
# b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
# what does this mean?

print(struct.pack('l', 3)) #8 long; native endianness
# b'\x03\x00\x00\x00\x00\x00\x00\x00'
print(struct.pack('h', 3))
# b'\x03\x00'
print('big endina unsigned int', struct.pack('>I', 3)) #4 long; 03 comes last
print('little endina unsigned int', struct.pack('<I', 3)) #4 long; 03 comes first

# on C must write different code when dealing with sequences of bytes for BE and LE systems (big-endian; little-endian)

# big endian: the most significant byte of a word (fixed-sized unit of data in computer storage)
# stored at the lowest memory address;
# LE - least signifc byte at lowest memory address

# Big endian: network protocoles
# little endians x86 archit, ARM; 
# file formats are mixed
# matters when memory dump


# 32 bits = 4 bytes
# 1 byte = 8 bits

# 1 byte has a memory location allocated; so groups of 8 bits are stored at 1 memory location

# ASCII char in Python takes 1byte
# int in Python takes 4 bytes (32bits)

print(len(('hello').encode('UTF-8'))) #5 bytes
#this matters when serialize in strings of char; for example when compactness is required

# word size for the computer processor is the number of bits that the processor can process at a time


#----------------------
# Text vs bytes Fluent Python book

#Python3: str returns a seq of Unicode characters (different from Python 2 where the keyoword unicode was needed)

# code point is a number bet 1 and 1,114,111 assigned to a unicode character showed in unicode standard as 4 to 6 hexa digits with U+
# the conversion from code point to byts is called encoding;
# the encoding depends on the standard for eg UTF-8 but others exist such as UTF-LE16

# UTF = Unicode Transformation Format

s = 'AB$'
print(str(s))
b = s.encode('utf_8')
print(bytes(b)) # bytes are for storage or transmission
print(len(b))
print(b.decode('utf_8'))

s = 'çafé'
cafe = bytes(s, encoding='utf_8')
print(cafe)
print(cafe[0])
# each item in bytes or bytearray in Python 3 is int from 0 to 255 (in Python2 it was a character)
# a slice produces a binary seq of the same type
print(cafe[:1])

# seems that Python3.7 and later may be working differently from how Fluent Python 3.4 might be doing
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# can use re; and other str methods on binary sequences

# binary seq can use fromhex
print(bytes.fromhex('31 4B CE A9'))

# To create binary sequences:
# uexamples above
# str and encode
# iterable with values from 0 to 255
# an object that implements the buffer protocol: bytes, bytearray, array.array, memoryview
# bytes and bytearray copy bytes from source object while memoryview allows sharing memory
# between binary sequences


# --------------------------
# Structs and Memory View
# goal is to prevent copying bytes
# eg use memoryview to access header (slices) from PIL images 

import struct
# with open('filter.gif', 'rb') as fp:
	# img = memoryview(fp.read())

# header = img[:10]
# bytes(header) # only for display
fmt = '<3s3sHH' # little endian; 2 seq of 3 bytes each and two 16-bit ints
# struct.unpack(fmt, header) unpack tuple of type, version, width, height for the image.
# no bytes copying

# --------------
# Basic Encoders/Decoders
city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('cp437', errors='replace')) # error replaces with ? This is UnicodeEncodeError

# UnicodeDecodeError in UTF-8 but other codecs can silently decode garbage (different things dep on
#codec intended for latin, greek, russion etc)

# can't detect codec; must be told
# chardet is a package that does that

# BOM = byte order mark may be prepended by UTF formats to binary sequences (BOM)
# big-endian little endian indicators 

# default encoding on Luinux, Mac OSX machines is UTF-8
# not on Windows -1252 (different ops differ)

# !always pass an encoding argument when reading or writing a text file!!

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)
fp.write('café')
fp.close()
import os
print(os.stat('cafe.txt').st_size)
fp4=open('cafe.txt', 'rb') #BufferedReader and not TextIOWrapper; open file for reading in binary mode
# print(fp4.encoding) # has no attribute encoding
print(fp4)
print(fp4.read())
fp3=open('cafe.txt', encoding='utf_8') # Text; has attribute encoding; don't rely on defaults
print(fp3.read())

print(sys.stdin.encoding) #same with stderr, stdout
# print(sys.getfilesyste)
import locale
print(locale.getpreferredencoding(do_setlocale=True))

# ------------------
# text normalization and sorting are difficult in Unicode world
from unicodedata import normalize
s1 = 'café'
# 'NFC', 'NFD', 'NFKC', 'NFKD'
print(len(normalize('NFD', s1))) # 4 for NFC 5 for NFD
# diacritic can be written two different ways and python will not know wame word so use normalize with a format
# canonical equivalents - should compare to be same - can do with normalization

# the K formats are stronger forms of normalization; compatibility characters; the example with 1/2 and 
# the other writing - and micro and micro_kc - useful for search and indexing to find different possible representations

# casefold() and lower() returns different thiings in 0.11% of 110,122 named characters (like micro) - eszett

# to compare: can do normalize(str1).casefold() 
# other normalization :shave_marks take all diac out etc - better handled by the nlp lib i think
# import pyuca
# unicoda collation algorithm to be able to sort words like for mportuq

# Unicode database contains mapping code oints and characters and metadata;
# that s how .isdigit(), isidentifier() etc work

# need to learn more about re and regex
print(sys.maxunicode) #1114111 seems to be related to code points range (16 or 32 bits per code point in RAM) narrow or wide build - how CPython could be compiled

# ------------
import re
# dual mode str and byte api
# eg in re and os

re_numbers_str = re.compile(r'\d+')
re_numbers_byts = re.compile(rb'\d+')

re_words_str = re.compile(r'\w+')
re_words_byte = re.compile(rb'\w+')

text_str = ("Ramanujan \u0be7 as 145.")
text_bytes = text_str.encode('utf_8')

print(repr(text_str)) #some weird symbol
print(re_numbers_str.findall(text_str))
print(re_numbers_byts.findall(text_bytes))

print(re_words_byte.findall(text_bytes))
print(re_words_str.findall(text_str))

# note how must compile the re object for numbers, words and str vs bytes







