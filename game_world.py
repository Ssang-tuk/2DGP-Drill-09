# 게임 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.

# layer 0: Background Objects
# layer 1: Foreground Objects

world = [[], []]

def add_object(o, depth = 0):
    world[depth].append(o)

# 게임 월드에 객체 리스트를 추가하는 함수
def add_objects(ol, depth = 0):
    world[depth] += ol

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('월드에 존재하지 않는 객체를 삭제하려 함.!.!')