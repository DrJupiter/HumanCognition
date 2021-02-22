# Implement

- Define how big a tile should be from resolution. (%)
- Generate a grid of tiles
- [Tile,Tile], [Points] -> tiles
- 




# Implementation


```python
from itertools import defualtdict

resolution = (w, h)

n = number_of_tiles

tile_resolution = (floor(w/(n+1)),floor(h/(n+1)))

offsets = np.randomlike((2,), 1..n+1)

bool_target = np.random()


target = 0

if bool_target >= 0.5:
    bool_type = np.random()
    if bool_type >= 0.5:
        target = 1 # Where one is a blue x fx 

type_dict = defaultdict(lambda: 0)

miss_counter = 0

def assignment(offsets, type_dict, fill_type):
    miss_counter = 0
    for o in offsets:
        if type_dict[o] != 0:
            type_dict[o] = fill_type # where 3 is a red cross
        else:
            miss_counter += 1
    if miss_counter == 0:
        return None
    else:
        assignment(np.randomlike(miss_couinter), type_dict, fill_type)

assignment(offsets, type_dict, red_cross)
assignment(offsets, type_dict, blue_circle)
```

Depending on resolution we go some steps up.

```python
draw_x(cord, resolution, color) -> Draws an x at the given position with some color and size based on the resolution.
draw_o(cord, resolution, color) -> Draws cirlce at the given position with some color and size based on the resolution.
```


# Notes


    
# Extra Time