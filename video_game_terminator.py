import os
import psutil
import time
import windows
illegal_software_list = ["MinecraftLauncher.exe", "FortniteLauncher.exe", "VALORANT-Win64-Shipping.exe", "RobloxPlayer.exe", "Escape Simulator.exe", "steam.exe", "Bluestacks.exe", "HD-Player.exe", "GenshinImpact.exe", "R5Apex.exe", "LeagueClient.exe", "eldenring.exe", "ModernWarfare.exe", "GTA5.exe", "csgo.exe", "RocketLeague.exe", "EpicGamesLauncher.exe", "RiotClientServices.exe", "RustCLient.exe", "dota2.exe", "Hearthstone.exe", "lostark.exe", "WoW.exe", "DeadByDaylight.exe", "FIFA22.exe", "Diablo III.exe", "Brawlhalla.exe", "NMS.exe", "TslGame.exe", "Overwatch Launcher.exe", "Overwatch.exe", "RainbowSix.exe", "ffxiv.exe", "nba2k22.exe", "worldoftanks.exe", "sc2.exe", "osu!.exe", "runescape.exe", "left4dead2.exe", "RDR2.exe"]

def eliminate_all_games(chrome_warned, discord_warned):
  
  
  if(not chrome_warned and ("chrome.exe" in (process.name() for process in psutil.process_iter()))):
    chrome_warned = True
    windows.chromeWarning()
    
  if(not discord_warned and ("Discord.exe" in (process.name() for process in psutil.process_iter()))):
    discord_warned = True
    windows.discordWarning()
    
  for i in illegal_software_list:
    #Credit: old stackoverflow post source code from Mark
    #https://stackoverflow.com/questions/7787120/check-if-a-process-is-running-or-not-on-windows
    if(i.lower() in (process.name().lower() for process in psutil.process_iter())):
      #Credit: old stackoverflow post source code from gh057 
      #https://stackoverflow.com/questions/5625524/how-to-close-a-program-using-python
      os.system("taskkill /F /IM " + i)
      windows.video_game_terminated()
  return (chrome_warned, discord_warned)

