# Creating [Simple] Blockchain with Python

This document is to build a blockchain transaction system ( peer-to-peer) interaction with Python Programming.

### Blockchain Theory

The way that blockchain works are that it stores a ledger of transactions from one party to another ( similar to Paypal, Venmo, and etc.. with
currency being crypto) into a block.
The block has the parameters of

block serial number: Ex.. ‘AAA’
transaction 1
transaction 2
....
The block can be hashed with a hashing algorithm, for example a SHA-256 Algo for Blockchain ( https://andersbrownworth.com/blockchain/hash
)

A Hash is a unique fixed-length string, meant to identify a piece of data. They are created as a hash function ..
In computer science / Data structures
A Hash Function is any function that can be used to map data of arbitrary size to a fixed size value. Hashing with the idea, given some key k, we
could come up with a function that could output an integer that ‘represents k’. In mathematics, hash functions have two properties. The first is
required but the second one is not as needed.
1.) Property of Equality : Given two keys k and I , if k == I, h(k) = h(i)
2.) Property of Inequity ( perfect hash function ) : if generate to return different hashes of different keys.
Hashing properties are implied in the use of diff downloaded file original file in Unix to check downloaded files against each other.
By hashing the files, you will be able to find the distinct difference. This is later used in coding theory for example Huffman coding to efficiently e
ncode ( compress ) a file and decode ( decompress a file ) with a loss-less compression Balanced binary tree structure.

No example of Hash function because keys of not equal value as a function is not valid. Breaking the Property of Equality. Therefore a more
valid Hash structure is

Take each character in a string and turn them into unsigned integers to be combined. This fulfills the Property of Equality and Property of
Inequity

### Back to Projects

Usually for Hashing function SHA - 256 function
Note Summary. Encoding: Reversible transformation of data format, used to preserve the usability of data. Hashing: A one-way summary
of data that cannot be reversed and is used to validate the integrity of data. Data encryption is the process that translates the data from
its original form to another form. The main purpose of encrypting data is to protect data confidentiality while it is stored on
computer systems or transmitted to other computers over the network.
As of right now.. let's pretend an example output hash ( Hexidecimal number)

## Example structure of Blockchain ..

## Example Nuel Coin

## T1: Anna sends bob 2 NC

## T2: Bob sends Daniel 4.3 NC

## T3: Mark sends Charlie 3.2 NC..

## Transactions can be stores in block.. ( Bases, transaction) --

## encrypted -- <

## B1 ("AAA", T1, T2, T3) -- hash ( SHA 256) --> 76fd89,

## B2 ("76fd89" ,t4, t5, t6) ---> 8923ff,

## B3 ("8923ff", t7, t8, ..) --->

## NueralHash ( )

Secure transaction and algorithm ( Most advanced Secure Hash Algorithms ( SHA))
1.) What is hashing
2.) What is SHA?
3.) SHA Characteristics
4.) Steps in SHA
5.) Applications in SHA..

### What is Hashing?

It is the process of scrambling a piece of information or data beyond recognition. We use hash functions to convert into hash Digest. These
functions are irreversible by design.

Encryption can be reversible like RSA or Diffie Helman, Hashes are known to be irreversible functions.
No decryption key can convert the digest to original data

### Password Hash storage

If the re-calculated hash matches the hash stored on the servers during the initial sign-up ( password ----> same in server ) the log-in is
allowed.

Notes:

```
No plain text password is stored, preventing the owner from looking at user data and protecting user privacy in a hack or data breach
```

### Integrity Verification

Hashing can also be used for integrity checks to ensure the data isn’t corrupted. The Hash value/digest allows being the same for similar
input.
Upload file to internet --- (hash function) upload digest
Download file --- (Hash function) get contents of the document.

```
Note:
The digest values are compared in the new value and the value uploaded by the user
```

In order to deal with corruption issues in transit, such a hash function makes the values able to check if the transaction was possible.
To turn plain test to digest, we need hash algorithms like SHA...

## What is SHA?

Secure Hahs Algorithm ( SHA) is a family of cryptographic algorithms by the NSA and NIST joint development. https://en.wikipedia.org/wiki
/Secure_Hash_Algorithms
Examples: SHA-0, SHA- 1, ...
Operations of SHA are pretty simple...

The GOAL of any Hash Function is to produce digests that are completely random. To be considered 2 requirements...
1.) Impossible for attackers to generate a message that has the Specific hash value
2.) Impossible for attackers to create two messages producing the exact same hash value ( COLLISION ATTACK https://en.wikipedia.org
/wiki/Collision_attack )

### SHA Characteristics

Properties/Characteristics of the SHA

###1.) Length of the { original Message } should be < 2^64 bits

This is initial to keep plain text compatible with the hash function and to make this as random as digest as possible.

### 2.) The Length of the Digest is always ( for SHA 256) 256 bits in length

This is to deal with the speed and security of the hash function. Bigger digest requires the cost of speed and space..

### 3.) The digest should not be able to produce the original message

All hash functions are irreversible. Digest can’t provide original values.. When the hash function is passed to digest for a second time, gets a
completely different digest. Reduce Bruitforce attacks.

### Steps of SHA Algorthm

### 1.) Padding bits..

Bits are appended to the original input to make it compatible with the hash function..
When getting input string, make sure total bits always be 64 bits short of any multiple of 512.
When padding the bits recommend first bit is '1', and the rest are all zeros.

### 2.) Padding length

```
Length of buts original message has padded the result of step
Length is expressed in the form of 64 bits
The resulting string now is a multiple of 512.
Using to increase the complexity of the function
```

3.) Initialize chaining variables

```
The entire message is broken down into blocks of 512 bits each.
5 buffers are used for 32 bits each. ( A, B, C, D, E)
These registers go through multiple rounds of iteration
```

### 4.) Process Each Block

```
Each 512-bit block is broken down into 16 sub-blocks of 32 bits.
There are 4 rounds of operations each of them utilizing the abcde register the 512-bit block and a const K[t].
Each round has 20 iterations , so total interactions = 4 * 20 = 80 rounds.
The constant value is an array of 80 elements, with 16 elements being used every round.
```

### Implementing in Python...( Insights after programming..)

So far this process. I was able to learn about the intricate interactions, both mathematically, and through python syntax explanation. I want to thank [NeuralNine ](https://www.youtube.com/watch?v=pYasYyjByKI&t=86s) for allowing me to brush up on, and build more knowledge on the background behind cryptographic algorithms. Very nice 1-2 hour project/exploration process in developing this out.
