#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for /fix_code command
"""

# Test kod
test_code = """def hello()
    print "Hello"
"""

print("Test kod:")
print(test_code)
print("\n" + "="*50 + "\n")

# Xatolarni aniqlash
errors_found = []
suggestions = []

# Python sintaksis xatolari
if 'def ' in test_code and ':' not in test_code.split('def')[1].split('\n')[0]:
    errors_found.append("❌ Funksiya ta'rifida ':' belgisi yo'q")
    suggestions.append("✅ Funksiya oxiriga ':' qo'shildi")

# Print xatolari
if 'print ' in test_code and 'print(' not in test_code:
    errors_found.append("❌ print funksiyasida qavslar yo'q")
    suggestions.append("✅ print() funksiyasiga qavslar qo'shildi")

# Qo'shtirnoq xatolari
if test_code.count('"') % 2 != 0 or test_code.count("'") % 2 != 0:
    errors_found.append("❌ Qo'shtirnoqlar to'liq emas")
    suggestions.append("✅ Barcha string'larni to'g'ri yoping")

print("Topilgan xatolar:")
for error in errors_found:
    print(error)

print("\nTavsiyalar:")
for suggestion in suggestions:
    print(suggestion)

print("\nTuzatilgan kod:")
fixed_code = """def hello():
    print("Hello")
"""
print(fixed_code)
