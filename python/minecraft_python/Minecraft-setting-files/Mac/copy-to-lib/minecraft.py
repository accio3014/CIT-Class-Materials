from mcpi.minecraft import Minecraft
import time

mw = Minecraft.create()

'''
major functions
'''

def setpos(x, y, z) :
   return mw.player.setTilePos(x, y, z)
   
def getpos() :
   return mw.player.getTilePos()

def setblock(x, y, z, blockid, sub = 0) :
   return mw.setBlock(x, y, z, blockid, sub)

def setblocks(x1, y1, z1, x2, y2, z2, blockid, sub = 0) :
   return mw.setBlocks(x1, y1, z1, x2, y2, z2, blockid, sub)

def getblock(x, y, z) :
   return mw.getBlock(x, y, z)

def getblockwithdata(x, y, z) :
   return mw.getBlockWithData(x, y, z)

def chat(say) :
   return mw.postToChat(say)

def setting(char, flag) :
   return mw.setting(char, flag)

def hit() :
   hits = []
   for hit in mw.events.pollBlockHits() :
      hits.append(hit.pos)
   return hits

def hitlastest() :
   hits = mw.events.pollBlockHits()
   if(hits) :
      return hits[0].pos
   
def hitfirst() :
   hits = mw.events.pollBlockHits()
   if(hits) :
      return hits[len(hits)-1].pos

def stop(sec) :
   return time.sleep(sec)

def getseconds() :
   return time.gmtime().tm_sec

'''
minor functions
'''

def setx(x) :
   pos = mw.player.getTilePos()
   return mw.player.setTilePos(x, pos.y, pos.z)

def sety(y) :
   pos = mw.player.getTilePos()
   return mw.player.setTilePos(pos.x, y, pos.z)

def setz(z) :
   pos = mw.player.getTilePos()
   return mw.player.setTilePos(pos.x, pos.y, z)

def getx() :
   return mw.player.getTilePos().x

def gety() :
   return mw.player.getTilePos().y

def getz() :
   return mw.player.getTilePos().z
