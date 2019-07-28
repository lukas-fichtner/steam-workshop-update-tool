import os
#Default Settings
steamCmdPath = 'C:\\Users\\Administrator\\Desktop\\steamcmd\\'
steamCmdExe = 'steamcmd.exe'
steamAppId = '221100'
finalModPath = 'C:\\Users\\Administrator\\Desktop\\ModUpdateTool\\'

#Login
steamUser = 'xedontv'
steamPass = ''
steamauth = ''

#Mods to Download
steamMods = [
	['1767379407','@EinsamimWaldServerMod'],
	['1623711988','@VanillaPlusPlusMap'],
	['1665663702','@MoreGuns'],
	['1612576045','@EasySigns'],
	['1560819773','@UnlimitedStamina'],
	['1559212036','@CF'],
	['1635058618','@DayZ-Expansion-Chat'],
	['1566911166','@MasssManyItemOverhaul'],
	['1574054508','@BuildAnywhere'],
	['1571965849','@DisableBaseDestruction'],
	['1667135157','@SimpleRoof'],
	['1646187754','@CodeLock'],
	['1582756848','@ZomBerryAdminTools'],
	['1725477270','@GraveCross'],
	['1680019590','@Server_Information_Panel'],
]
def fnc_modDownload(ModId, ModDir):
	steamModId = ModId
	finalModDir = ModDir
	cmdCommand = (steamCmdPath+steamCmdExe+' +login '+steamUser+' '+steamPass+' '+steamauth+' +"workshop_download_item '+steamAppId+' '+steamModId+'" validate +quit')
	symbolicLink = ('mklink /J "'+finalModPath+finalModDir+'" "'+steamCmdPath+'steamapps\\workshop\\content\\'+steamAppId+'\\'+steamModId+'"')
	print(
		'-- Verify final command --\n'
		'AppId: '+steamAppId+'\n'
		'ModId: '+steamModId+'\n'
		'Mod Directory: '+finalModDir+'\n'
		'SteamCmd command: '+cmdCommand+'\n'
		'Symbolic link command: '+symbolicLink+'\n'
		'--- End of verification ---\n'
	)
	#Ask if the Update should be started
	runCode = 'y'
	if runCode == 'y':
		os.system(cmdCommand)
		symLink = 'y'
		#Ask if a SymbolicLink should be created
		if symLink == 'y':
			os.system(symbolicLink)
			print('Symbolic link created \n')
		else:
			print('No symbolic link created \n')
	else:
		print('No Update')
for Mods in steamMods:
	fnc_modDownload(*Mods)
input('Hit a key to exit')