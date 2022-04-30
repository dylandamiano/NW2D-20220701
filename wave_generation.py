import computer_movement
import time

wave_count = 0
time_since_wave = 0

update_tick = time.time()

interwave_count = 0

entities_remain = 0
wave_active = True

def update_wave():

    """
        The wave update function intertwines all of the functions from this file.
        First, the whole process starts with checking if a wave is active or has the sufficient
        properties to be active. If the wave is active, we're going to let it run its course whereas
        if the wave is NOT active, then we're going to summon a new one after around 15 seconds.

        As the wave progresses, we're going to check to see how many entities are currently on the map,
        and the responses from the game will be handled accordingly.

        At the end of a wave, a new one will obviously be summoned.
    """

    global update_tick
    global time_since_wave

    update_entity_count()

    if (time.time() - update_tick) >= 1:
        update_tick = time.time()
        time_since_wave += 1

    if entities_remain == 0:
        summon_wave()
        print("Awaiting spawn...")


def summon_wave():

    """
        Summons a wave at the beginning of the game or once the previous one is over after x amount
        of time.
    """

    global wave_count
    global time_since_wave
    global interwave_count

    computer_movement.x_offset = 0
    computer_movement.y_offset = 0

    if interwave_count < 5:
        interwave_count += 1

    if interwave_count >= 5:
        time_since_wave = 0
        wave_count += 1
        interwave_count = 0

        if (wave_count % 1) == 0:
            for x in range (0, wave_count):
                computer_movement.createEntities(1, "Fighter")

def check_wave():

    """
        Checks to see if a wave is currently active
        or if a wave can no longer be active because it doesn't
        meet a minimum requirement.
    """

    if (entities_remain == 0) and (wave_active == True):
        pass
    elif (interwave_count == 0) and (wave_active == False):
        pass

def update_entity_count():

    """
        Simply updates how many entities are currently on the map.
    """

    global entities_remain

    entities_remain = len(computer_movement.active_entities) - computer_movement.friendly_count