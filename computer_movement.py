import math
import random
import gameCalculations
import time
import playerClasses
import projectileClasses
import warshipClonkses
import logHandler

# will be determined later on, AI creation might have to be done in game

groups_created = 0
active_entities = []

'''
    Function below creates the AI entity. The game will automatically determine if it is a jet or a boat.
    However, each AI will move at different times determined by the computer when the time for movement comes.

    There is really no set difficulty level in terms of how well it will play as well.
'''

def createEntities(count, ent_type = "Carrier"):
    global groups_created

    if ent_type == "Carrier":
        groups_created += 1

        for i in range(0, count):
            entity_name = "entity_" + str(groups_created) + "_" + str(i)

            ship_local = playerClasses.computerEntity(name=str(entity_name))
            ship_local.createShip("Carrier")
            ship_local.type = "sea"

            ship_local.last_move = int(time.time())
            ship_local.last_fired = int(time.time())

            active_entities.append(ship_local)

    if ent_type == "Fighter":
        groups_created += 1

        for i in range(0, count):
            entity_name = "entity_" + str(groups_created) + "_" + str(i)

            ship_local = playerClasses.computerEntity(name=str(entity_name))
            ship_local.createShip("Fighter")
            ship_local.type = "air"

            ship_local.last_move = int(time.time())
            ship_local.last_rotate = int(time.time())

            active_entities.append(ship_local)

createEntities(5)
createEntities(5, "Fighter")

for entity in active_entities:
    print(entity.AI)

'''
    Functions to manipulate when or where the AI will appear
    on or off the screen.
'''

def draw_entities(surface):
    for entity in active_entities:
        surface.blit(entity.ship.image, entity.ship.rect)

def move_entities(playerFired = False):
    if playerFired == True:
        for entity in active_entities:
            latest_attempt = time.time()
            last_move = entity.last_move #= latest_attempt (IGNORE!)

            rtrn = None

            if entity.reverse == True:
                if ((latest_attempt - last_move) > .5) and entity.type == "air":
                    if entity.move_direction == -1:
                        entity.move_direction = 1
                        entity.reverse = False
                    elif entity.move_direction == 1:
                        entity.reverse = False
                elif ((latest_attempt - last_move) > 5) and entity.type == "sea":
                    if entity.move_direction == -1:
                        entity.move_direction = 1
                        entity.reverse = False
                    elif entity.move_direction == 1:
                        entity.reverse = False

            if entity.move_direction == 1:
                gameCalculations.checkBorder(entity.ship, "Forward")
            elif entity.move_direction == -1:
                gameCalculations.checkBorder(entity.ship, "Backwards")

            logHandler.createLog(str(rtrn))

def rotate_entities():
    for entity in active_entities:
        latest_attempt = time.time()
        rand_limit = 0

        if entity.type == "air":
            rand_limit = random.randint(2, 6)
        elif entity.type == "sea":
            rand_limit = random.randint(6, 12)

        if (latest_attempt - entity.last_rotate) > rand_limit:
            rand_direction = random.randint(1, 2)

            entity.rotate_direction = rand_direction
            entity.last_rotate = latest_attempt

        if entity.rotate_direction == 1:
            gameCalculations.rotateChar(entity.ship, "Left")
        elif entity.rotate_direction == 2:
            gameCalculations.rotateChar(entity.ship, "Right")

def get_distance(entity_one, entity_two) -> float:
    e1_x = entity_one.ship.v2Pos.x
    e1_y = entity_one.ship.v2Pos.y

    e2_x = entity_two.ship.v2Pos.x
    e2_y = entity_two.ship.v2Pos.y

    y_distance = e2_y - e1_y
    x_distance = e2_x - e1_x

    total_distance = (x_distance)**2 + (y_distance)**2

    return total_distance

last_fired = time.time()

# Functions below simulate player input
def simulate_mouse(player, random_path: bool = False) -> tuple:
    global last_fired
    x = 0
    y = 0

    recent_click = time.time()
    
    combined_entities = [player] # Just updating our local list, ya know?

    if (recent_click - last_fired) > 2:
        last_fired = recent_click

        for entity in active_entities:
            combined_entities.append(entity)

        for entity in active_entities:
            closest_entity = None
            closest_distance = None

            for other in combined_entities:
                if other.username != entity.username:
                    if closest_entity == None:
                        closest_entity = other
                        closest_distance = get_distance(entity, other)
                    elif closest_entity != None:
                        if get_distance(entity, other) < closest_distance: # error likely to occur here but we will let it happen so we can see what we are working with lol
                            closest_entity = other
                            closest_distance = get_distance(entity, other)


            angle = gameCalculations.get_angle(
                    (entity.ship.v2Pos.x, entity.ship.v2Pos.y),
                    (closest_entity.ship.v2Pos.x, closest_entity.ship.v2Pos.y)
                )

            projectileClasses.mouseFired(angle, entity)

    if random_path == True:
        x = random.randint(0, 900)
        y = random.randint(0, 900)

    coordinate = (x, y)

    for entity in active_entities:
        pass

    return coordinate