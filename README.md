# simulateInfection

The Center for Disease Control and Prevention is trying to model disease propagation for a particular virus. The virus is known to transmit through human contact and the study aims to simulate how various towns in a region can get infected by the movement of people. The scientists have come up with the following simple model for this scenario:


The whole region is defined as a rectangular grid with dimensions LxH, with each cell representing a single town. 

To begin with, only a small number of towns are infected by the virus. The virus is known to spread when a person moves from any infected town to an adjacent town.

The initial list of infected towns is provided as a list of x and y coordinates. For example, a value of <0, 0> would indicate the bottom-left corner cell in the grid is an infected town.


A person's location is represented by x and y coordinates. Their heading is represented by one of four cardinal compass points. An example position could be <0, 0, N>, which means that the person is at the bottom-left corner and facing up. 

As a person moves through the grid, if they happen to move through a cell which is infected, every subsequent cell they enter will end up being infected. 

A person's movements through the region is represented by a limited set of operations: 

L -- makes the person turn left 90 degrees

R -- makes the person turn right 90 degrees

F -- makes the person move forward 1 square


Assume the square directly north of <x, y> is <x, y+1>.
