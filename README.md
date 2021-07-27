# Coursera Cryptography I Programming Assignments (Stanford University)

[https://www.coursera.org/learn/crypto]()

## Assignment 1:


Given that all messages are in ASCII format, with readable characters encrypted with the same OTP key, my approach was:

1. For a given encrypted message (A), XOR it with every other encrypted message (B), resulting in C = A XOR B;
2. Create a list for every character in C containing all possible characters combinations that could generate this character;
3. For each list of these lists, get the character which appears the most.

## Assignment 2:


Basic usage of PyCrypto for AES CBC and CTR modes.

## Assignment 3:


Use of PyCrypto SHA256 for hashing file chunks.

## Assignment 4:


Demonstration of a padding oracle attack against an AES CBC encryption with random IV.

The padding oracle attack consists of obtaining bytes of a CT by querying the server about the padding validity of the ciphertext.

The ciphertext has a 16-byte IV and a 48-bytes playload. In CBC encryption the payload is encrypted 16-bytes at a time. My approach was the following:

1. Send c[0] and c[1] with modified c[0] to get m[1];
2. Send c[0], c[1] and c[2] with modified c[1] to get m[2];
3. send c[0] and IV with modified IV to get m[0].

![Pic](https://i.imgur.com/zL6Efxu.png)

## Assignment 5:


Computation of discrete log modulo a prime *p*. The formula <img src="https://render.githubusercontent.com/render/math?math=h = g^x"> was solved by using [gmpy2](https://gmpy2.readthedocs.io/en/latest/mpz.html#mpz-methods) and modular arithmetic.