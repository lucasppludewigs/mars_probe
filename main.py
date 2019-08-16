"""Case for Elo7 programming."""
import sys

from utils.logging import logging_setup
log = logging_setup()

def read_input():
    """Read data input."""
    with open('input.txt','r') as f:
        input = f.read()
        lines = input.split('\n')
    return lines

def get_max_sizes(lines):
    """Data input ingestion"""
    rectangle_size = lines[0].split(' ')
    max_x = int(rectangle_size[0])
    max_y = int(rectangle_size[1])
    return max_x, max_y

def get_input_info(lines):
    lin = 1
    positions_list = ['Positions:']
    main_command_list = ['Commands:']
    while lin < len(lines):
        """Get probes positions."""
        position = lines[lin].split(' ')
        position[0] = int(position[0])
        position[1] = int(position[1])
        positions_list.extend(position)
        """Get probes commands."""
        main_command_list.append(lines[lin+1])
        lin = lin+2
    
    return positions_list, main_command_list

def execute_commands(positions_list,main_command_list, max_x, max_y):
    """Executes the content within command list."""
    c = 1
    while c < len(main_command_list):
        command_list = list(main_command_list[c])
        for command in command_list:
            if command == 'M':
                if positions_list[3*c] == 'N':
                    positions_list[(3*c)-1] = positions_list[(3*c)-1] + 1
                    if positions_list[(3*c)-1] > max_y:
                        log.info('Your commands exceeds rectangle_size')
                        sys.exit()
                elif positions_list[3*c] == 'S':
                    positions_list[(3*c)-1] = positions_list[(3*c)-1] - 1
                    if positions_list[(3*c)-1] < 0:
                        log.info('Your commands exceeds rectangle_size')
                        sys.exit()
                elif positions_list[3*c] == 'E':
                    positions_list[(3*c)-2] = positions_list[(3*c)-2] + 1
                    if positions_list[(3*c)-2] > max_x:
                        log.info('Your commands exceeds rectangle_size')
                        sys.exit()
                elif positions_list[3*c] == 'W':
                    positions_list[(3*c)-2] = positions_list[(3*c)-2] - 1
                    if positions_list[(3*c)-1] < 0:
                        log.info('Your commands exceeds rectangle_size')
                        sys.exit()
                else:
                    log.info('Something weird happened. Verify input.')
            elif command == 'L':
                if positions_list[3*c] == 'N':
                    positions_list[3*c] = 'W'
                elif positions_list[3*c] == 'W':
                    positions_list[3*c] = 'S'
                elif positions_list[3*c] == 'S':
                    positions_list[3*c] = 'E'
                elif positions_list[3*c] == 'E':
                    positions_list[3*c] = 'N'
                else:
                    log.info('Something weird happened. Verify input.')
            elif command == 'R':
                if positions_list[3*c] == 'N':
                    positions_list[3*c] = 'E'
                elif positions_list[3*c] == 'E':
                    positions_list[3*c] = 'S'
                elif positions_list[3*c] == 'S':
                    positions_list[3*c] = 'W'
                elif positions_list[3*c] == 'W':
                    positions_list[3*c] = 'N'
                else:
                    log.info('Something weird happened. Verify input.')
            else:
                log.info('Something weird happened. Verify input.')
        c = c+1
    return positions_list


def main():
    lines = read_input()
    max_x, max_y = get_max_sizes(lines)
    print('Rectange size: (',max_x,',', max_y,')')
    positions_list, main_command_list = get_input_info(lines)
    print('\nInput file:')
    print(positions_list)
    print(main_command_list)
    positions_list = execute_commands(
        positions_list,main_command_list,max_x, max_y)
    print('\nFinished executing commands.')
    print(positions_list)
    
    #print(position[6]) # verify input length
    
    """Data Input validation."""
    #log.info('Empty line on input')
    #log.info('Not a valid input')

if __name__ == "__main__":
    main()