# Gallon-Bucket-Problem
The objective of this project is to develop a program that can solve the problem of 2 kids fetching 4 gallons of water from a stream, using only an unmarked 3-gallon bucket, and an unmarked 5-gallon bucket, in less than 15 steps.

I set my code up to use three different functions in order to solve this problem. You can either fill one bucket fully, dump it out, or pour it into the other bucket and keep the remaining water.

The output shows each step as well as tracking how much water each bucket has at each step.

### Output
```
Fill bucket 5 fully
Bucket 3: 0    Bucket 5: 5

Pour Bucket 5 into bucket 3, keeping 2 gallons in bucket 5
Bucket 3: 3    Bucket 5: 2

Dump out bucket 3
Bucket 3: 0    Bucket 5: 2

Pour the 2 gallons from bucket 5, into bucket 3
Bucket 3: 2    Bucket 5: 0

Fill bucket 5 back up
Bucket 3: 2    Bucket 5: 5

Pour bucket 5 into bucket 3, filling it up, leaving 4 gallons in bucket 5
Bucket 3: 3    Bucket 5: 4
```
