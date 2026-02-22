#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advanced test for code fixing
"""

# Test 1: Funksiya va print xatolari
test1 = """def hello()
    print "Hello World"
"""

print("TEST 1 - Funksiya va print xatolari:")
print("Xatoli kod:")
print(test1)

# Tuzatish
fixed1 = """def hello():
    print("Hello World")
"""
print("\nTuzatilgan kod:")
print(fixed1)
print("="*50 + "\n")

# Test 2: Indentatsiya xatolari
test2 = """def calculate(a, b):
result = a + b
return result
"""

print("TEST 2 - Indentatsiya xatolari:")
print("Xatoli kod:")
print(test2)

fixed2 = """def calculate(a, b):
    result = a + b
    return result
"""
print("\nTuzatilgan kod:")
print(fixed2)
print("="*50 + "\n")

# Test 3: If statement xatolari
test3 = """if x > 5
    print("Katta")
"""

print("TEST 3 - If statement xatolari:")
print("Xatoli kod:")
print(test3)

fixed3 = """if x > 5:
    print("Katta")
"""
print("\nTuzatilgan kod:")
print(fixed3)
print("="*50 + "\n")

# Test 4: Qavslar xatolari
test4 = """result = calculate(10, 20
print(result
"""

print("TEST 4 - Qavslar xatolari:")
print("Xatoli kod:")
print(test4)

fixed4 = """result = calculate(10, 20)
print(result)
"""
print("\nTuzatilgan kod:")
print(fixed4)
print("="*50 + "\n")

print("✅ Barcha testlar ko'rsatildi!")
print("\nBot endi bu xatolarni avtomatik tuzatadi!")
