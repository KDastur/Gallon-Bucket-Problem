# Gallon bucket problem

bucket3 = 0
bucket5 = 0

# Fills the specified bucket up fully
def fill(x):
    global bucket3, bucket5
    if x == "bucket3":
        bucket3 = 3
    elif x == "bucket5":
        bucket5 = 5

# Dumps the specified bucket out
def dump(y):
    global bucket3, bucket5
    if y == "bucket3":
        bucket3 = 0
    elif y == "bucket5":
        bucket5 = 0

# Pours the content of one bucket(x) into the other
def pour(x, bucket3, bucket5):
    if x == "bucket3":
        bucket5 += bucket3
        if bucket5 > 5:
            bucket3 = bucket5-5
            bucket5 = 5
        else:
            bucket3 = 0
    elif x == "bucket5":
        bucket3 += bucket5
        if bucket3 > 3:
            bucket5 = bucket3-3
            bucket3 = 3
        else:
            bucket5 = 0
    return bucket3, bucket5

print("Fill bucket 5 fully")
fill("bucket5")
print("Bucket 3:", bucket3, "   Bucket 5:", bucket5)

print("\nPour Bucket 5 into bucket 3, keeping 2 gallons in bucket 5")
bucket3, bucket5 = pour("bucket5", bucket3, bucket5)
print("Bucket 3:", bucket3, "   Bucket 5:", bucket5)

print("\nDump out bucket 3")
dump("bucket3")
print("Bucket 3:", bucket3, "   Bucket 5:", bucket5)

print("\nPour the 2 gallons from bucket 5, into bucket 3")
bucket3, bucket5 = pour("bucket5", bucket3, bucket5)
print("Bucket 3:", bucket3, "   Bucket 5:", bucket5)

print("\nFill bucket 5 back up")
fill("bucket5")
print("Bucket 3:", bucket3, "   Bucket 5:", bucket5)

print("\nPour bucket 5 into bucket 3, filling it up, leaving 4 gallons in bucket 5")
bucket3, bucket5 = pour("bucket5", bucket3, bucket5)
print("Bucket 3:", bucket3, "   Bucket 5:", bucket5)
