# Data Structures and Algorithms

## Hash tables

The different ways to calculate the hash for a list of items:
  - Folding method- Divides item into equal size pieces and then adds them together for the hash value.
    -  Ex. Phone # 436-555-4601 
      - Groups of 2 (42,65,55,46,01)
      - Add them together: 42 + 65 + 55 + 46+ 01 = 210
      - Hash table of 11 slots, need to divide by 11 and keep the reminder
      - 210 % 11 = 1
      - So 436-555-4601 hashes to slot 1.
      
  - Mid-square method- Squares the item then extracts the middle section
    - Ex. 44
      - 44^2 = 1,936
      - Extract the middle digits of 1936 = 93
      - Get remainder: 93 % 11 = 5
  
  - Character based method- Uses ord() number of each letter
    -Ex. "

