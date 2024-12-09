def maksimal(a, b):
    if a < b: return b
    else: return a

def minimal(a, b):
    if a > b: return b
    else: return a

batas = 0
maks = -100000
minim = 100000
bilangan = int(input())

while batas < bilangan:
    nilai = int(input())
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)
    batas += 1

print(maks, minim) 
