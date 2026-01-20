# 마인크래프트 내에서 광물 블록 등 필수 블록을 제외한 다른 모든 블록을
# 특정 블록으로 변경하는 코드, 게임 모드와 유사한 프로그램
# 네더, 엔더 월드의 경우 변경 X

from mcpi.minecraft import *
from mcpi.block import *
import time

mc = Minecraft.create()

RADIUS = 20
TARGET_BLOCK = 20       # 이 부분만 수정

EXCLUDE_BLOCKS = {
    0,7,14,15,16,21,47,49,56,57,73,79,88,89,103,129,
    133,153,169,173,174,213,54,58,30,61,50,65,32,84,
    85,111,106,116,120,130,145,165,355,426,23,25,29,
    33,46,69,76,77,96,123,131,143,152,158,218,324,
    330,331,27,28,66,157,328,333,342,343,407,408,
    138,9,10,90,119
}

# 플레이어가 설치한 블록 좌표
player_blocks = set()
# 이전 상태 기억
last_blocks = {}

while True:
    pos = mc.player.getTilePos()
    px, py, pz = pos.x, pos.y, pos.z

    blocks = list(mc.getBlocks(
        px-RADIUS, py-RADIUS, pz-RADIUS,
        px+RADIUS, py+RADIUS, pz+RADIUS
    ))

    idx = 0
    to_change = []

    for y in range(py-RADIUS, py+RADIUS+1):
        for x in range(px-RADIUS, px+RADIUS+1):
            for z in range(pz-RADIUS, pz+RADIUS+1):
                block_id = blocks[idx]
                idx += 1
                coord = (x, y, z)

                prev = last_blocks.get(coord, block_id)

                if prev == 0 and block_id != 0 and y >= py - 2:
                    player_blocks.add(coord)

                last_blocks[coord] = block_id

                if coord in player_blocks:
                    continue
                if block_id in EXCLUDE_BLOCKS:
                    continue
                if block_id == TARGET_BLOCK:
                    continue

                to_change.append(coord)

    initialized = True

    for x, y, z in to_change:
        mc.setBlock(x, y, z, TARGET_BLOCK)

    time.sleep(0.3)