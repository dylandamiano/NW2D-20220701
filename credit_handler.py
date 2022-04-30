import gameSettings
import time
import pygame


starting_credits = 10000
current_credits = starting_credits

last_update = time.time()

recent_purchases = []
destroyed_ships = 0

def update_credits() -> None:

    """
       Updates how many credits that the player will have remaining.
    """

    time_credits()
    entity_credits()
    purchase_item()

    #print(current_credits)

def time_credits() -> None:

    """
        Issues 10 credits/second to the player sprite. Can be varied but 10 credits is the
        current recommendation as everything is mostly priced with this in mind.
    """

    global last_update
    global current_credits

    if (time.time() - last_update) >= 1:
        last_update = time.time()
        current_credits += 10

def entity_credits() -> None:

    """
        When a ship is destroyed by friendly forces, the player will be issued
        50 credits for every ship that was destroyed.
    """

    global current_credits
    global destroyed_ships

    current_credits += 50 * destroyed_ships
    destroyed_ships = 0


def purchase_check(plr_credits: int, item_credits: int):
    global current_credits

    if plr_credits > item_credits:
        current_credits -= item_credits
        return True

def purchase_item(item: str = None) -> None:

    """
        Will handle item purchased, still in the works.

        Jets: 500
        Carrier: 2000
        Destroyer: 3000
        Heal: 1000
        Battlegroup: 8500
        Clear: 50000
    """

    # Could be done better, I just don't feel like writing a loop that involves a dictionary, because I said so

    if item == "Jets":
        if purchase_check(current_credits, 500) ==  True:
            return True
    elif item == "Carrier":
        if purchase_check(current_credits, 2000) ==  True:
            return True
    elif item == "Destroyer":
        if purchase_check(current_credits, 3000) ==  True:
            return True
    elif item == "Heal":
        if purchase_check(current_credits, 1000) ==  True:
            return True
    elif item == "Battlegroup":
        if purchase_check(current_credits, 8500) ==  True:
            return True
    elif item == "Clear":
        if purchase_check(current_credits, 50000) ==  True:
            return True
    else:
        pass

def display_credits(surface):
    font = pygame.font.SysFont("Segoe UI Bold", 32)

    text = pygame.font.Font.render(font, str(current_credits) + " credits", 1, (0,0,0))
    surface.blit(text, (411.4, 273.6))