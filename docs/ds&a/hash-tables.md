# Hash Tables

[md5 Hash Generator](http://www.miraclesalad.com/webtools/md5.php)

## What is a Hashtable?

- _Hash:_ A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. A hashtable is used to determine the index of the array.
- _Buckets:_ are what is contained in each index of the array of the hastable. Each index is a bucket. An index could potentially contain multiple key/value pairs if a collision occurs.
- _Collisions:_ A collision is what happens when more than one key gets hashed to the same location of the hastable. [Check out the wiki collision resolution](https://en.wikipedia.org/wiki/Hash_table#Collision_resolution)

## Why do we use them?

## What are they?

- data structure that utilize key value pairs; every **Node** or **Bucket** has both a key, and a value
- the basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value
- this is done through a _hash_
- a hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value
- uses **_hash maps_** that take advantage of an array's O(1) read access
- a hash map uses a **_hash function_** to place each item at a precise index location, based off its key.
- the hash function takes a key and returns an integer
- we use the integer to determine where the key/value pair should be placed in the array
- the hash code is calculated in **_constant time (O(1))_** and writing

## Structure

### Hashing

- a hash code turns a key into an integer. **_It's very important that hash codes are deterministic: their output is determined only by their input._**
- Hash codes should never have randomness to them. The same key should always produce the same hash code.

### Creating a Hash Table
- A hash table is a collection of items which are stored in such a way as to make it easy to find them later.
- Each position of the hash table, _buckets_ (some folks call them slots), can hold an item and is anmed by an integer value starting at zero
  - Meaning if I implemented a hash table, I'd have a bucket named 0, 1, 2, etc.
  - Initially, the hash table contains no items so every slot is empty
- After creating array of appropriate size (a good size is 1024), write logic to turn that key into a numeric value
- Possible suggestion:
  - add or multiply all the ASCII values together
  - Multiply it by a prime number such as 599
  - Use modulo to get the remainder of the result, when divided by the total size of the array
  - Insert into the array at the index
- Implementing in Python, I can use a list with each element initialized to the special Python value `None`
- The mapping between an item and the slot where that item belongs in teh hash table is called a _hash function_
  - The hash function will take any item in the collection and return an integer in the range of the bucket names, between 0 and m-1
  - A hash function that maps each item into a unique slot is referred to as a _perfect hash function_
    - No collisions
- A few techniques to attain perfect hash functions
  - The **folding method** 
    - is used for constructing hash functions begins by dividing the item into equal-size pieces (the last piece may not be of equal size)
    - These pieces are added together to give the resulting hash value
  - The **mid-square method**
    - You would square the item, then extract some portion of the resulting digits
    - For example, if the item were 44, I would first compute 44^2=1,936
    - By extracting the middle two digits, 93, and performing the remainder step, I'd get 93%11 = 5
- One hash function options to use is the remainder method
  - When presented with an item, the hash function is the item divided by the table size, this is then its bucket number
  - When searching for an item, we call the hash function to compute the bucket name for the item and then check the hash table to see if it is present
  - Searching operation is O(1), since a constant amount of time is required to compute the hash value and then index the hash table at that location
  - 

### Collisions

- A collision occurs when more than one key hashes to the same index in an array.

- Collisions are resolved by changing the initial state of the buckets. Instead of starting them all as **null**, we can initialize a **LinkedList** in each one.
- Now if two keys resolve to the same index in the array their key/value pairs can be stored as a node in a linked list.
- Each index in the array is called a **_"bucket" because it can store multiple key/value pairs_**

## Internal Methods

### add()

- send the key to _getHash()_
- once you determine the index of where it should be placed, go to that index
- check if something exists at that index already, if it doesn't, add it with the key/value pair.
- if something does exist, add the new key/value pair to the data structure within the bucket

### find()

- takes in a key, gets the _hash()_, and indexes location specified. Once the index location is found in the array, the algorithm iterates through the bucket to see if the key exists and return the value

### contains()

- will accept a key, return a boolean on of the key exists inside the hashtable. Have _contains()_ call the _getHash()_ method and check the _hashtable_ if the key exists in the table given the index returned.

### getHash()

- Accepts a key as a string, conducts the hash, and then return the index of the array where the key/value pair should be placed

### Resources
- [What is a Hastable?](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)
- [Tutorial video](https://www.youtube.com/watch?v=MfhjkfocRR0)
- [Basics of Hash Tables](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
- [Hash table wiki](https://en.wikipedia.org/wiki/Hash_table)

[Table of Contents](../index.md)
