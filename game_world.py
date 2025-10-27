# 게임 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.

world = []

def add_object(o):
    world.append(o)

def update():
    for o in world: o.update()

def render():
    for o in world: o.draw()

def remove_object(o):
    world.remove(o)