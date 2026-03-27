import re
import math
parserbounds = r'\((.*?)\)|\[(.*?)\]' 

with open('vel.txt', 'r') as myfile:
    content = myfile.read()
    matches = re.findall(parserbounds, content)

results = []
for match in matches:
    extracted_text = next(item for item in match if item)
    results.append(extracted_text)
comparison = []
for line in results:
    parts = line.split(',')
    part1 = float(parts[0])
    part2 = float(parts[1])
    part3 = float(parts[2])

    mag_squared = part1**2 + part2**2 + part3**2
    actual_speed = math.sqrt(mag_squared)
    comparison.append(actual_speed)

comparison.sort()

print(comparison[-1])