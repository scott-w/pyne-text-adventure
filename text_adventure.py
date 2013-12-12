import json


def load_map(filename):
    """Load the map for filename.
    Returns the map.
    """
    with open(filename) as f:
        j = json.load(f)

    return j


def get_directions(room):
    """Get the directions that you can travel in from room.
    """
    return [key for key in room if key != 'description']


def get_actions(the_map):
    """Get the list of actions that we can perform.
    """
    actions = the_map['_null']
    return actions.keys()


def do_action(the_map, action):
    """Return the text of the action to perform.
    """
    actions = the_map['_null']
    return actions.get(action, '')


def get_description(room):
    """Get the description for the room.
    """
    return room['description']


def move_direction(the_map, room, direction):
    """Move in direction from room.
    Returns room_name, room.
    """
    go = room[direction]
    return go, the_map[go]


def get_input(room, the_map):
    """Read stdin and see if it's a valid action.
    """
    stdin = ''
    while stdin not in get_directions(room):
        stdin = raw_input('Enter a direction: ')

        if stdin in get_actions(the_map):
            print do_action(the_map, stdin)

    return stdin


def game_loop():
    """Keep playing until we reach _end room.
    """
    current_room = '_first'
    the_map = load_map('our_map.json')

    while current_room != '_end':
        room = the_map[current_room]

        print room['description']

        print 'You can move: {}'.format(
            ', '.join(get_directions(room)))
        direction = get_input(room, the_map)
        current_room, room = move_direction(the_map, room, direction)

    print room['description']


game_loop()
