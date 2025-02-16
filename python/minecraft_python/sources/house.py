# house.py
from minecraft import *
from turtlem import turtle

# 플레이어의 현재 위치를 얻음
pos = getpos()
x = pos.x
y = pos.y
z = pos.z

# 집의 크기 및 높이 설정
width = 20
height = 10
depth = 12

# 블럭 id 설정
wall_block_id = 1  # Stone
floor_block_id = 5  # Wooden Planks
roof_block_id = 17  # Oak Wood
window_block_id = 102  # Glass Pane
door_block_id = 64  # Wooden Door
stair_block_id = 53  # Oak Wood Stairs

# 바닥 만들기
setblocks(x, y - 1, z, x + width, y - 1, z + depth, floor_block_id)

# 벽 만들기
setblocks(x, y, z, x, y + height, z + depth, wall_block_id)
setblocks(x + width, y, z, x + width, y + height, z + depth, wall_block_id)
setblocks(x, y, z + depth, x + width, y + height, z + depth, wall_block_id)

# 지붕 만들기
setblocks(x - 1, y + height, z - 1, x + width + 1, y + height, z + depth + 1, roof_block_id)

# 창문 만들기
for i in range(2, width - 2, 4):
    setblocks(x + i, y + 2, z, x + i + 2, y + 5, z, window_block_id)

# 문 만들기
setblock(x + width // 2, y, z, door_block_id)

# 벽면에 계단 추가
for i in range(height):
    setblocks(x - 1, y + i, z, x, y + i + 1, z + depth, stair_block_id)
    setblocks(x + width, y + i, z, x + width + 1, y + i + 1, z + depth, stair_block_id)
    setblocks(x, y + i, z - 1, x + width, y + i + 1, z, stair_block_id)
    setblocks(x, y + i, z + depth, x + width, y + i + 1, z + depth + 1, stair_block_id)
