


wires = [
    ['R8','U5','L5','D3'],
    ['U7','R6','D4','L4']
]

lines = []

for wire in wires:

    previous_point = {
        'x': 1,
        'y': 1
    }

    for point in wire:
        new_point = None
        if 'R' in point:
            new_point = {
                'x1': previous_point['x'],
                'y1': previous_point['y'],
                'x2': previous_point['x'] + int(point.split('R')[1]),
                'y2': previous_point['y']
            }
        if 'L' in point:
            new_point = {
                'x1': previous_point['x'],
                'y1': previous_point['y'],
                'x2': previous_point['x'] - int(point.split('L')[1]),
                'y2': previous_point['y']
            }
        if 'U' in point:
            new_point = {
                'x1': previous_point['x'],
                'y1': previous_point['y'],
                'x2': previous_point['x'],
                'y2': previous_point['y'] + int(point.split('U')[1])
            }
        if 'D' in point:
            new_point = {
                'x1': previous_point['x'],
                'y1': previous_point['y'],
                'x2': previous_point['x'],
                'y2': previous_point['y'] - int(point.split('D')[1])
            }
        lines.append(new_point)
        previous_point = {'x':new_point['x2'], 'y':new_point['y2']}
print(lines)


"""
    for line in lines:
        for line in lines:
            if line != line:
                if lines intersect:
                    add to intersection

    for intersection in intersection:
        calcl dist from x,1, y;1


"""

