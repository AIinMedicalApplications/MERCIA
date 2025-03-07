#  \file    MERCIA_local_4.py
#  \author  saalfeldlab@gmail.com.de
from mevis import *

def init(*args):
  # init the Macro Module -> set all bypasses to "no bypass"
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(1)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(1)
  pass

def SelectTabTitleFunction():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(3)
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(1)
  pass

def SelectTab1Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(0)
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(1)
  pass

def SelectTab2Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(1)
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(0)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(1)
  pass

def SelectTabWEMCutFunction():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(2)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(0)
  pass
 
def SelectTab3Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(3)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(0)
  ctx.field("BypassAfterCropWEMMacro.noBypass").setBoolValue(1)
  pass

def SelectTab4Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(4)
  ctx.field("BypassAfterCropWEMMacro.noBypass").setBoolValue(0)
  pass

