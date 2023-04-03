from pygame import Surface, Rect
import pygame
from lib.misc import *
from lib.objects import Camera, GameObject, Enemy
import random


def check_out_of_bound(boundary, obj):
    r = obj.boundary
    b = boundary
    return (r.top < b.top,
            r.left < b.left,
            r.bottom > b.bottom,
            r.right > b.right)


def chance(c):
    """in percentage"""
    return random.randint(0, 100) < c


def randist(center, d_range, world_dim):
    """
    :param center: tuple of obj pos
    :param d_range: min and max dis from obj
    :param world_dim: tuple of world dimension
    :return: tuple x and y of new pos
    """
    while True:
        out = random.randint(0, world_dim[0]), random.randint(0, world_dim[1])
        if d_range[0] <= magnitude(subTuple(center, out)) <= d_range[1]:
            return out


class GameWorld:
    """
    __game_objects__ is a 2D dictionary. First is obj.tag for quick lookup. This layer should be O(1) since we
    don't actually have a lot of tag. Second is the actual obj name. This will be O(n)
    """

    def __init__(self, dimensions: Rect, tiledim: tuple, screen: Surface, mouseArea: tuple, camera: Camera) -> None:
        self.__dim__ = dimensions
        self.__tiledim__ = tiledim
        self.__camera__ = camera
        self.__camera__.set_world(self)
        self.__game_objects__ = {}
        self.__screen__ = screen
        self.__mouse_area__ = mouseArea
        self.__addlist__ = []
        self.__garbage__ = []
        self.tileMap = {}
        self.debug_title_map = False
        self.collided_pairs = {}
        self.border_behavior = self.border_default
        self.no_collide_tags =["particles"]
        self.__max_count__ = {}
        self.__max_count__ = {"enemy": 100}  # limited 100 enemy so I can be lazy
        self.player = None  # for enemy tracking purpose. Player is a little special

    def __update_tile_map__(self):
        self.tileMap.clear()
        for key in self.__game_objects__:
            if key not in self.no_collide_tags:
                for object_name in self.__game_objects__[key]:
                    obj = self.__game_objects__[key][object_name]
                    boundary = obj.boundary
                    topLeft, bottomRight = [floorElementDiv(i, self.__tiledim__) for i in
                                            [boundary.topleft, boundary.bottomright]]
                    for tup in [(i, j) for i in range(topLeft[0], bottomRight[0] + 1) for j in
                                range(topLeft[1], bottomRight[1] + 1)]:
                        self.tileMap[tup] = [obj] + self.tileMap.get(tup, [])

    def __get_collided_pairs__(self):
        self.collided_pairs.clear()
        for tile in self.tileMap:
            for object in self.tileMap[tile]:
                for other_object in self.tileMap[tile]:
                    if object != other_object and object.checkCollision(other_object):
                        if object.name < other_object.name:
                            self.collided_pairs[object.name + "x" + other_object.name] = [object, other_object]

    def __garbage_collection__(self):
        while len(self.__garbage__):
            obj = self.__garbage__.pop()
            if self.__game_objects__.get(obj.tag, {}).get(obj.name):
                del self.__game_objects__[obj.tag][obj.name]

    def get_scaled_mouse_pos(self):
        return mulElements(self.__screen__.get_size(), elementDiv(pygame.mouse.get_pos(), self.__mouse_area__))

    def border_default(self, dt, key, object: GameObject):
        r = object.boundary
        if key == "player_bullet":
            # remove bullet when leave game world
            bb = self.__dim__.copy()
            bb.inflate_ip(r.size)
            bounds = check_out_of_bound(bb, object)
            if True in bounds:
                object.destroy()
        elif key == "camera":
            b = self.__dim__
            bounds = check_out_of_bound(b, object)
            if bounds[0]:
                object.pos = (object.pos[0], object.pos[1] + b.top - r.top)
                object.vel = (object.vel[0], 0)
            if bounds[1]:
                object.pos = (object.pos[0] + b.left - r.left, object.pos[1])
                object.vel = (0, object.vel[1])
            if bounds[2]:
                object.pos = (object.pos[0], object.pos[1] + b.bottom - r.bottom)
                object.vel = (object.vel[0], 0)
            if bounds[3]:
                object.pos = (object.pos[0] + b.right - r.right, object.pos[1])
                object.vel = (0, object.vel[1])
        else:
            b = self.__dim__
            bounds = check_out_of_bound(b, object)

            if bounds[0]:
                object.pos = (object.pos[0], object.pos[1] + b.top - r.top)
                object.vel = (object.vel[0], -object.vel[1])
            if bounds[1]:
                object.pos = (object.pos[0] + b.left - r.left, object.pos[1])
                object.vel = (-object.vel[0], object.vel[1])
            if bounds[2]:
                object.pos = (object.pos[0], object.pos[1] + b.bottom - r.bottom)
                object.vel = (object.vel[0], -object.vel[1])
            if bounds[3]:
                object.pos = (object.pos[0] + b.right - r.right, object.pos[1])
                object.vel = (-object.vel[0], object.vel[1])
        object.boundCenterToPos()

    def add_game_object(self, key: str, obj: GameObject):
        obj.tag = key
        if self.__game_objects__.get(key):
            self.__game_objects__[key][obj.name] = obj
        else:
            self.__game_objects__[key] = {obj.name: obj}

    def delete_game_object(self, obj: GameObject):
        self.__garbage__.append(obj)

    def delete_if_dead(self, obj):
        if obj and not obj.liveflag:
            self.delete_game_object(obj)

    def set_tracked_object(self, key, follow_distance):
        for object_name in self.__game_objects__[key]:
            self.__camera__.follow_config(self.__game_objects__[key][object_name], follow_distance)

    # args will be functions which we want to apply to every object, but we don't want in our object classes
    def update(self, dt: float, *args):
        self.__camera__.update(dt)
        mousePos = self.get_scaled_mouse_pos()

        for key in self.__game_objects__:
            for object_key in self.__game_objects__[key]:
                obj = self.__game_objects__[key][object_key]
                # some object update return new objs such as enemy bullet
                mulreturn = obj.update(dt, mousepos=mousePos, camera=self.__camera__)
                if isinstance(mulreturn, list):
                    self.__addlist__.append(mulreturn)
                self.border_behavior(dt=dt, key=key, object=obj)

                for fun in args:
                    fun(world=self, dt=dt, key=key, object=obj)
                self.delete_if_dead(obj)

        self.__garbage_collection__()
        self.__update_tile_map__()
        self.__get_collided_pairs__()
        
        for i in self.__addlist__:
            for j in i:
                self.add_game_object(j[0], j[1])
        self.__addlist__.clear()

        for pair in self.collided_pairs:
            obj_a, obj_b = self.collided_pairs[pair]
            obj_a.collisionEffect(self, dt, obj_b)
            obj_b.collisionEffect(self, dt, obj_a)

    def render(self, *args):
        if self.debug_title_map:
            self.render_tile_map()
        
        for key in self.__game_objects__:
            for obj_key in self.__game_objects__[key]:
                obj = self.__game_objects__[key][obj_key]
                obj.render(self.__screen__, self.__camera__)

                for fun in args:
                    fun(self=self, screen=self.__screen__, key=key, object=obj)

    def render_tile_map(self):
        for tile in self.tileMap:
            self.__screen__.fill((tile[0] * 4 % 200 + 55, 55, tile[1] * 4 % 200 + 55),
                                 Rect(subTuple(mulElements(tile, self.__tiledim__), self.__camera__.boundary.topleft),
                                      self.__tiledim__))

    def spawnObj(self, prop, num_range, obj_class, tag):
        """
        build on top of adding object but allow number and probability and random location spawn
        """
        if chance(prop):
            if not self.__game_objects__.get(tag):  # add empty tag if not exit
                self.__game_objects__.update({tag: {}})
            for _ in range(random.randint(*num_range)):
                while True:
                    # make sure to generate new obj with different name
                    nametest = tag + str(random.randint(0, 1000))
                    if nametest not in self.__game_objects__[tag]:
                        new_obj = obj_class(nametest, randist(self.player.pos, (300, 1200), self.__dim__.size), (48, 48))
                        if issubclass(obj_class, Enemy):  # this setting allow me to set tracking on player
                            new_obj.setTarget(self.player)
                        self.add_game_object(tag, new_obj)
                        break
