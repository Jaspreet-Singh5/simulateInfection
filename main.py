from grid import Grid
from person import Person
from disease_propagation_model import DiseasePropagationModel


def main():
    # Define the initial infected cells in the grid
    infected_cells = [(1, 1), (2, 3)]

    # Create the grid and display its initial state
    grid = Grid(5, 5, infected_cells)
    print("Initial Grid State:")
    print(grid)

    # Define the list of persons with their initial position and movements
    persons = [
        Person((1, 0, 'N'), "FFRFFRF"),
        Person((1, 3, 'S'), "LFFLFRFRFF"),
    ]

    # Create the disease propagation model and simulate the infection
    model = DiseasePropagationModel(grid, persons)
    model.simulate_infection()

    # Display the final state of the grid
    print("Final Grid State:")
    print(grid)


if __name__ == '__main__':
    main()
