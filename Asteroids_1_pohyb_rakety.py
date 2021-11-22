import math
import pyglet
from pyglet import gl
from pyglet.window import key

"---------Globalne konštanty a premenne----------"

"Window constants"
WIDTH = 1200
HEIGHT = 800

"Game constants"
#Todo 1: Vytvorte konštanty pre zrýchlenie rakety a rýchlosť otáčania a pokúste sa nájsť optimálne hodnoty


objects = []                    #ZOZNAM VŠETKÝCH AKTÍVNYCH OBJEKTOV V HRE
batch = pyglet.graphics.Batch() #ZOZNAM SPRITOV PRE ZJEDNODUŠENÉ VYKRESLENIE
pressed_keyboards = set()       #MNOŽINA ZMAČKNUTÝCH KLÁVES


"------------------- FUNKCIE __________________"

"""
Vycentruj ukotvenie obrázka na stred
"""
def set_anchor_of_image_to_center(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

"----------------VLASTNÉ TRIEDY----------------"

"""
Trieda Spaceship
Hlavný objekt hry, predstavuje hráča
"""
class Spaceship:

    "Konštruktor"
    def __init__(self, sprite):
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 1.57 # radiany -> hodnota 1.57 smeruje nahor

        self.sprite = pyglet.sprite.Sprite(sprite, batch=batch)
        self.sprite.x = WIDTH // 2
        self.sprite.y = HEIGHT // 2

    """
    Metóda pre kontrolu pozície či sa nachádzame na okraji
    """
    def checkBoundaries(self):
        #Todo 6: Skontrolujte či sa ne-nachádzate s loďou mimo okna ak áno loď by sa mala objaviť na druhej strane
        pass

    """
    Každý frame sa vykoná táto metóda to znamená v našom prípade:
    60 simkov * za sekundu
    Mechanic of spaceship - rotation, movement, controls
    """
    def tick(self, dt):
        # Todo 5: Dokončite metódu tick ktorá sa stará o ovládanie lodi

        "Zrýchlenie po kliknutí klávesy W. Výpočet novej rýchlosti"
        # Todo
            #self.x_speed = self.x_speed + dt * ACCELERATION * math.cos(self.rotation) #Výpočet ryhlosti v smere X
            #self.y_speed = self.y_speed + dt * ACCELERATION * math.sin(self.rotation) #Výpočet ryhlosti v smere Y

        "Spomalenie/spätný chod po kliknutí klávesy S"
        #Todo

        "Otočenie doľava - A"
        #Todo

        "Otočenie doprava - D"
        #Todo

        "Ručná brzda - SHIFT"
        #Todo

        "Posunutie vesmírnej lode na novú pozíciu"
        self.sprite.x += dt * self.x_speed
        self.sprite.y += dt * self.y_speed
        self.sprite.rotation = 90 - math.degrees(self.rotation)

        "Kontrola či sme prešli kraj"
        #Todo

"""
GAME WINDOW CLASS
"""
class Game:
    """
    Konstruktor
    """
    def __init__(self):
        self.window = None
        self.game_objects = []

    """
    Načítanie všetkých spritov
    """
    def load_resources(self):
        self.playerShip_image = pyglet.image.load('Assetss/PNG/playerShip1_blue.png')
        set_anchor_of_image_to_center(self.playerShip_image)
        self.background_image = pyglet.image.load('Assetss/Backgrounds/black.png')

    """
    Vytvorenie objektov pre začiatok hry
    """
    def init_objects(self):
        #Todo 5: Vytvorte objekt pre loď a pridajte ho do game_objects


        self.background = pyglet.sprite.Sprite(self.background_image)
        self.background.scale_x = 6
        self.background.scale_y = 4

    """
    Event metóda ktorá sa volá na udalosť on_draw stále dookola
    """
    def draw_game(self):
        # Vymaže aktualny obsah okna
        self.window.clear()
        # Vykreslenie pozadia
        self.background.draw()

        # Táto časť sa stará o to aby bol prechod cez okraje okna plynulý a nie skokový
        for x_offset in (-self.window.width, 0, self.window.width):
            for y_offset in (-self.window.height, 0, self.window.height):
                # Remember the current state
                gl.glPushMatrix()
                # Move everything drawn from now on by (x_offset, y_offset, 0)
                gl.glTranslatef(x_offset, y_offset, 0)

                # Draw !!! -> Toto vykreslí všetky naše sprites
                batch.draw()

                # Restore remembered state (this cancels the glTranslatef)
                gl.glPopMatrix()

    """
    Event metóda pre spracovanie klávesových vstupov
    """
    def key_press(self, symbol, modifikatory):
        # Todo 2: Vytvorte Event Handler pre zmáčknuté klávesy
        # Todo Tie ktoré hráč zmačkol sa uložia do množiny pressed_keyboards
        pass

    """
    Event metóda pre spracovanie klávesových výstupov
    """
    def key_release(self, symbol, modifikatory):
        # Todo 3: Vytvorte Event Handler pre klávesy ktoré už ďalej nie sú zmaćknuté
        # Todo Tieto klávesy odoberte z pressed_keyboards mnoźiny
        pass
    """
    Start game metóda 
    """
    def start(self):
        "Vytvorenie hlavneho okna"
        self.window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

        "Nastavenie udalosti (eventov)"
        self.window.push_handlers(
            on_draw=self.draw_game,
            on_key_press=self.key_press,
            on_key_release=self.key_release
        )

        "Load resources"
        self.load_resources()

        "Inicializacia objektov"
        self.init_objects()

        "Nastavenie timeru pre update všetkých objektov v intervale 1./60 = 60FPS"
        for object in self.game_objects:
            pyglet.clock.schedule_interval(object.tick, 1. / 60)
        pyglet.app.run()  # all is set, the game can start

"----------- StartGame -----------"
Game().start()



