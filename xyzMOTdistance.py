with open(file, "r") as f:
    lines = [line.strip() for line in f.readlines()]

num_atoms = int(lines[0])
comment = lines[1]

atoms = []

for line in lines[2:]:
    parts = line.split()
    if len(parts) == 4:
        try:
            symbol = parts[0]
            x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            atoms.append([symbol, x, y, z])
        except ValueError:
            continue
#going to scour every 1000 then stop to do again.

chunk_size = 1000

for start in range(0, len(atoms), chunk_size):
    totaldist = 0
    end = start + chunk_size
    chunk = atoms[start:end]


    for atom in chunk:
        # assume atom = [id, x, y, z]
        x_coord = float(atom[1])
        y_coord = float(atom[2])
        z_coord = float(atom[3])

        # calculate squared distance from origin
        dist = x_coord**2 + y_coord**2 + z_coord**2
        totaldist += dist

    print(f"Average distance of molecules from center of MOT: {totaldist}")
