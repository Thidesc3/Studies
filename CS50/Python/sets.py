# create an empty sete

s = set()

# Add elements to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # Ele não mostra dois do mesmo

# Remove the element "2"
s.remove(2)

# len can be use to see the number os elemnts on the set

print(f"The set has {len(s)} elements")
