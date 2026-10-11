"""Encode a binary record

Concepts: struct, bytes, endianness, hashlib
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Pack an unsigned 16-bit sensor ID and signed 32-bit reading into a six-byte
network-order record. Return the bytes and their SHA-256 hex digest. Decode
only exact six-byte records. Out-of-range numbers should raise struct.error.
A plain hash detects changes but does not authenticate a sender.

HINT
The ! prefix selects network byte order and standard sizes.

STRETCH
Add a record version and compare hashing with keyed HMAC authentication.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import struct
import hashlib

RECORD = struct.Struct('!Hi')

def encode_record(sensor_id, reading):
    data = RECORD.pack(sensor_id, reading)
    return data, hashlib.sha256(data).hexdigest()

def decode_record(data):
    return RECORD.unpack(data)


def check():
    data, digest = encode_record(7, -20)
    assert len(data) == 6 and len(digest) == 64
    assert decode_record(data) == (7, -20)
    assert encode_record(7, -20) == (data, digest)
    try:
        decode_record(data + b'x')
    except struct.error:
        pass
    else:
        raise AssertionError('incorrect record size accepted')


if __name__ == "__main__":
    check()
    print("PASS: Encode a binary record")
