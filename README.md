# Coursera Cryptography I Programming Assignments (Stanford University)

[https://www.coursera.org/learn/crypto]()

## Assignment 1:


Given that all messages are in ASCII format, with readable characters encrypted with the same OTP key, my approach was:

1. For a given encrypted message (A), XOR it with every other encrypted message (B), resulting in C = A XOR B;
2. Create a list for every character in C containing all possible characters combinations that could generate this character;
3. For each list of these lists, get the character which appears the most.

## Assignment 2:


Basic usage of PyCrypto for AES CBC and CTR modes.