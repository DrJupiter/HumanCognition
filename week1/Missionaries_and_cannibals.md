# Implement

- [1] A system for state transitions (movement)
- [2] A system for checking if the state transitions are valid. (movement validity)
- > A state transition is valid, if it doesn't break the rules 
- [3] Time tracker for time spent in each state.
- - [3.1] Barplots of time spent.
- [4] Main loop

## [1] State Transition

```python
def state_transition(state, move):
    # Modifies a state based on a move
```

```Python
start_state = State(Missionary, Cannibal, Boat)
new_state = ...

if start_state - new_state


[Missionary(int), Cannibal(int), Boat(bool)]

start_state: [u8, u8, bool] = [3, 3, 1]
state: [u8, u8, bool] = [3, 3, 1]
<3,3,1> - <0,2,1> = <3,1,0>
<3,1,0> + <0,1,1> = <3,2,1>
<3,2,1> - <0,2,1> = <3,0,0>
<3,0,0> + <0,1,1> = <3,1,1>
<3,1,1> - <2,0,1> = <1,1,0>
<1,1,0>
```


## [2] Valid State

```python
def valid_state(state: [int, int, bool]) -> bool:
    # Check if a state follows the rule s
```

## [3] State-Time dictionary

A statedict with an accumalating timer for each state.


### [3.1] Barplot

```python

def create_bar_plot(time_dict): -> BarPlot:

# Sudo code detailing the barplot
default_dict = defaultdict(lambda: 0)
for keys, vals in default_dict.items():
    plot.add(analyze(keys, vals))

plot.show()

```


## [4] Main loop

```python
def main(current_state):

    move = input("Please input a move")
    new_state = state_transition(current_state, move)

    if valid_state(new_state):
        draw_new_scene(new_state)
        main(new_state)        
    else:
        display_error("Invalid move")
        main(current_state)
```

### Rules
- alle bitches til den anden side
- 3 c og 3 m (starts at wrong side)
- 1 båd (starts at wrong side)
- 2 personer i båden ad gangen. Der skal altid være min. 1 person i båden ad gangen
- aldrig være flere c end m på en given side
- folk i båden gælder som at være på den side, hvor båden står

### TODO

- make actions visible 

### Questions

- Skal man kunne tabe eller skal det være som før, hvor den bare forhindrer dig i at tage et træk?