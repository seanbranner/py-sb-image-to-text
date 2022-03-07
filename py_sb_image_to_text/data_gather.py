from imagesearch import *
import cv2
import numpy as np
import pyautogui as ptg 
import time
import xlsxwriter
import sys
import pytesseract
from PIL import Image, ImageEnhance, ImageOps, ImageGrab, ImageStat
pytesseract.pytesseract.tesseract_cmd = 'D:\\ProgramFiles\\Python\\Python37-32\\Lib\\Tesseract-OCR\\tesseract'
screenWidth, screenHeight = ptg.size()

def findSquare():
	cap = cv2.VideoCapture(1)
	
	while True:
		_, frame = cap.read()
		
		cv2.imshow("Frame", frame)
		
		key = cv2.waitKey(1)
		if key -- 27:
			break
		
	cap.release()
	cv2.destroyAllWindows()

def create_excel(xlsEntries, xlName):
	# Create a workbook and add a worksheet.
	workbook = xlsxwriter.Workbook(xlName)
	worksheet = workbook.add_worksheet()

	row = 0
	col = 0
	# Iterate over the data and write it out row by row.
	for Name, Faction, Skill_1, Skill_2, Skill_3, Aura, Rarity, Type, Element, HP, ATK, DEF, SPD, C_RATE, C_DMG, RESIST, ACC in (xlsEntries):
		worksheet.write(row, col,     Name)
		worksheet.write(row, col + 1, Faction)
		worksheet.write(row, col + 2, Skill_1)
		worksheet.write(row, col + 3, Skill_2)
		worksheet.write(row, col + 4, Skill_3)
		worksheet.write(row, col + 5, Aura)
		worksheet.write(row, col + 6, Rarity)
		worksheet.write(row, col + 7, Type)
		worksheet.write(row, col + 8, Element)
		worksheet.write(row, col + 9, HP)
		worksheet.write(row, col + 10, ATK)
		worksheet.write(row, col + 11, DEF)
		worksheet.write(row, col + 12, SPD)
		worksheet.write(row, col + 13, C_RATE)
		worksheet.write(row, col + 14, C_DMG)
		worksheet.write(row, col + 15, RESIST)
		worksheet.write(row, col + 16, ACC)
		row += 1

	workbook.close()

def open_noxVm():
	ptg.hotkey('win','down')
	ptg.hotkey('win')
	ptg.hotkey('n','o','x')
	ptg.hotkey('enter')

def click_raid_app():
	pos = imagesearch_loop("raid_app.JPG", 0.5)
	print("image found ", pos[0], pos[1])
	ptg.moveTo(pos[0]+10,pos[1]+10)
	ptg.click(clicks=1, button='left')

def click_fullScreen():#Move to fullscreen button, push it
	pos = imagesearch("nox_dragBar.JPG")
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		ptg.moveTo(pos[0]+140, pos[1]+15)
		ptg.click(clicks=1, button='left')

def click_index_button():#Move to Index button, push it
	pos = imagesearch("button_alert_index.JPG")
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		ptg.moveTo(pos[0]+50, pos[1]+50)
		ptg.click(clicks=1, button='left')

def drag_bottom_to_top():#Drag from bottom of screen to top
	ptg.moveTo(930, 996)
	ptg.dragTo(928, 205, 3, button='left') 
	
def click_exit():
	pos = imagesearch("button_exit.JPG")
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		ptg.moveTo(pos[0]+39, pos[1]+33)
		ptg.click(clicks=1, button='left')

def click_banner(bannerName):
	time.sleep(1)
	if bannerName =='banner lords':
		pos = imagesearch("banner_banner_lords.JPG")
	if bannerName =='high elves':
		pos = imagesearch("banner_high_elves.JPG")
	if bannerName =='the sacred order':
		pos = imagesearch("banner_the_sacred_order.JPG")
	if bannerName =='barbarians':
		pos = imagesearch("banner_barbarians.JPG")
	if bannerName =='orgyn tribes':
		pos = imagesearch("banner_orgyn_tribes.JPG")
	if bannerName =='lizardmen':
		pos = imagesearch("banner_lizardmen.JPG")
	if bannerName =='skinwalkers':
		pos = imagesearch("banner_skinwalkers.JPG")
	if bannerName =='orcs':
		pos = imagesearch("banner_orcs.JPG")
	if bannerName =='demonspawn':
		pos = imagesearch("banner_demonspawn.JPG")
	if bannerName =='undead hordes':
		pos = imagesearch("banner_undead_hordes.JPG")
	if bannerName =='dark elves':
		pos = imagesearch("banner_dark_elves.JPG")
	if bannerName =='knight revenant':
		pos = imagesearch("banner_knight_revenant.JPG")
		
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		ptg.moveTo(pos[0]+39, pos[1]+33)
		ptg.click(clicks=1, button='left')

def find_totalStats():
		starPos = imagesearch("word_total_stats.JPG")
		if starPos[0] != -1:
			print("position : ", starPos[0], starPos[1])
		else:
			print("Not There")

def find_element():
	element = ''
	pos = imagesearch("element_void.JPG")
	if pos[0] != -1:
		element = 'Void'
	else:
		print("image not found")
	pos = imagesearch("element_death.JPG")
	if pos[0] != -1:
		element = 'Death'
	else:
		print("image not found")	
	pos = imagesearch("element_lightning.JPG")
	if pos[0] != -1:
		element = 'Lightning'
	else:
		print("image not found")	
	pos = imagesearch("element_magic.JPG")
	if pos[0] != -1:
		element = 'Magic'
	else:
		print("image not found")

	return element
	
def screenCapNox(fullPathAndFileName):
	img = ImageGrab.grab(bbox=(47, 32, 1832, 1037))
	img.save(fullPathAndFileName)

def findBrightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

def invertImage(img):
	size = width, height= img.size
	if (img.mode == 'RGBA'):
		img.load()
		r,g,b,a = img.split( )
		img= img.merge ( 'RGB' , (r,g,b))
	img = ImageOps.invert( img )
	return img

def imgBlackAndWhite(img):
	en=ImageEnhance.Color(img)
	img = en.enhance(0.0)
	return img

def brightenImage(img):
	en=ImageEnhance.Brightness(img)
	img = en.enhance(1.99)
	return img

def getLiveBioName():
	img = ImageGrab.grab(bbox=(47, 32, 1654, 95))
	img = invertImage(img)
	imageText = pytesseract.image_to_string(img)
	if 'lvl' in imageText:
		imageText = imageText.replace('lvl','Lvl')
	imageText = imageText[2:imageText.find('Lvl')]
	return imageText.strip()

def getLiveBannerName():
	img = ImageGrab.grab(bbox=(47, 259, 377, 310))
	img = invertImage(img)
	imageText = pytesseract.image_to_string(img)
	return imageText.strip()

def getLiveType(x,y):
	img = ImageGrab.grab(bbox=(x-50, y+100, x+140, y+155))
	img = invertImage(img)
	#img = imgBlackAndWhite(img)
	#img.show()
	imageText = pytesseract.image_to_string(img)
	return imageText.strip()

def getStats():
	img = ImageGrab.grab(bbox=(1705, 627, 1818, 1000))
	img = invertImage(img)
	img = imgBlackAndWhite(img)
	imageText = pytesseract.image_to_string(img)
	imageText = imageText.split('\n')
	return imageText[0],imageText[1],imageText[2],imageText[3],imageText[4],imageText[5],imageText[6],'0'

def findBioBanner():
	banner = ''
	pos = imagesearch("banner_bio_high_elves.JPG")
	if pos[0] != -1:
		banner = 'High Elves'
	pos = imagesearch("banner_bio_banner_lords.JPG")
	if pos[0] != -1:
		banner = 'Banner Lords'
	pos = imagesearch("banner_bio_the_sacred_order.JPG")
	if pos[0] != -1:
		banner = 'The Sacred Order'
	pos = imagesearch("banner_bio_knight_revenant.JPG")
	if pos[0] != -1:
		banner = 'Knight Revenant'
	pos = imagesearch("banner_bio_dark_elves.JPG")
	if pos[0] != -1:
		banner = 'Dark Elves'
	pos = imagesearch("banner_bio_undead_hordes.JPG")
	if pos[0] != -1:
		banner = 'Undead Hordes'
	pos = imagesearch("banner_bio_demonspawn.JPG")
	if pos[0] != -1:
		banner = 'Demonspawn'
	pos = imagesearch("banner_bio_orcs.JPG")
	if pos[0] != -1:
		banner = 'Orcs'
	pos = imagesearch("banner_bio_skinwalkers.JPG")
	if pos[0] != -1:
		banner = 'Skinwalkers'
	pos = imagesearch("banner_bio_lizardmen.JPG")
	if pos[0] != -1:
		banner = 'Lizardmen'
	pos = imagesearch("banner_bio_barberians.JPG")
	if pos[0] != -1:
		banner = 'Barbarians'
	pos = imagesearch("banner_bio_ogryn_tribes.JPG")
	if pos[0] != -1:
		banner = 'Orgyn Tribes'
	return banner

def findSkillDesc():
	time.sleep(1)
	pos = imagesearch('word_level1.JPG')
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		img = ImageGrab.grab(bbox=(537, 128, 1345, 1029))
		img = invertImage(img)
		imageText = pytesseract.image_to_string(img)
	else:
		print("Skill Description Not Found")
		return 

	return imageText

def findAuraDesc():
	pos = imagesearch('word_aura.JPG')
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		img = ImageGrab.grab(bbox=(537, 128, 1345, 1029))
		img = invertImage(img)
		imageText = pytesseract.image_to_string(img)
	else:
		print("Skill Description Not Found")
		return	

	return imageText		

def getSkills():
	charSkills = []
	pos = imagesearch("word_skills.JPG")

	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
	else:
		print("Not There")

	ptg.moveTo(pos[0]+(1510-pos[0]), pos[1]+(288-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	
	ptg.moveTo(pos[0]+(1700-pos[0]), pos[1]+(288-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	
	ptg.moveTo(pos[0]+(1510-pos[0]), pos[1]+(460-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	
	ptg.moveTo(pos[0]+(1700-pos[0]), pos[1]+(460-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	auraDesc = findAuraDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	if  auraDesc != None:
		charSkills.append(auraDesc)
	
	ptg.moveTo(pos[0]+(1600-pos[0]), pos[1]+(460-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	
	ptg.moveTo(pos[0]+(1510-pos[0]), pos[1]+(377-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	
	ptg.moveTo(pos[0]+(1700-pos[0]), pos[1]+(377-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)
	
	ptg.moveTo(pos[0]+(1600-pos[0]), pos[1]+(377-pos[1]))
	ptg.click(clicks=1, button='left')
	skillDesc = findSkillDesc()
	if  skillDesc != None:
		charSkills.append(skillDesc)

	try:
		skill_1 = charSkills[0]
	except:
		skill_1 = None
	try:
		skill_2 = charSkills[1]
	except:
		skill_2 = None
	try:
		skill_3 = charSkills[2]
	except:
		skill_3 = None
	try:
		skill_4 = charSkills[3]
	except:
		skill_4 = None	

	return skill_1, skill_2, skill_3, skill_4

def saveMugShot(x,y,charName):
	img = ImageGrab.grab(bbox=(x, y, x+132, y+172))
	img.save("D:\\Documents\\Scripts\\project-raid\\raid_image_data_mine\\mugShots\\"+charName+"_Mug.JPG")
	if findBrightness("D:\\Documents\\Scripts\\project-raid\\raid_image_data_mine\\mugShots\\"+charName+"_Mug.JPG") < 80:
		img = brightenImage(img)
		img.show()
		img.save("D:\\Documents\\Scripts\\project-raid\\raid_image_data_mine\\mugShots\\"+charName+"_Mug.JPG")

def click_mugshotword():
	pos = imagesearcharea("word_hp.JPG",1323,393,1473,641)

	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
#position :  756 374
#Point(x=714, y=177)
#Point(x=859, y=366)		
		saveMugShot(pos[0]-35+1323,pos[1]-189+393,"example")

excelArray = [
	['Name','Faction','Skill_1','Skill_2','Skill_3','Skill_4','Rarity','Type','Element','HP','ATK','DEF','SPD','C_RATE','C_DMG','RESIST','ACC']]
	
def click_index_rarity_word(rarityName):
	time.sleep(1)
	pos = imagesearch("word_index_rarity_"+rarityName+".JPG")
	img = Image.open("word_index_rarity_"+rarityName+".JPG")
	width, height = img.size
	print (width/2)
	print(height/2)

	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		ptg.moveTo(pos[0]+71, pos[1]+15)
		ptg.dragTo(953, 170, .5, button='left')
		ptg.dragTo(953, 175, .5, button='left')
		time.sleep(1)
	else:
		print("Rarity Not Found")
		return

	###################################Under Construction ######################
	#Click each mugshot and do things
	pos = imagesearch("word_index_rarity_"+rarityName+".JPG")
	xcor = pos[0]+(width/2)-825
	ycor = pos[1]+(height/2)+320
	mugx = pos[0] - 780
	mugy = pos[1] + 320
	while xcor < 1834:
		characterArray = ['','','','','','','','','','','','','','','','','']
		type = getLiveType(xcor,ycor)
		ptg.moveTo(xcor, ycor)
		ptg.click(clicks=1, button='left')#Champ bio location D:\Documents\Scripts\project-raid\raid_image_data_mine\champion_bios
		time.sleep(1)
		starPos = imagesearch("word_total_stats.JPG")
		if starPos[0] != -1:#If on bio screen
			charName = getLiveBioName()
			skill_1,skill_2,skill_3,skill_4 = getSkills()
			hp,atk,dfns,spd,c_rate,c_dmg,resist,acc = getStats()
			print("position : ", starPos[0], starPos[1])
			screenCapNox('D:\\Documents\\Scripts\\project-raid\\raid_image_data_mine\\champion_bios\\'+charName+'_bio.JPG')
			characterArray[0] = str(charName)			
			characterArray[1] = findBioBanner()
			characterArray[2] = skill_1
			characterArray[3] = skill_2
			characterArray[4] = skill_3
			characterArray[5] = skill_4
			characterArray[6] = str(rarityName)
			characterArray[7] = type
			characterArray[8] = find_element()
			characterArray[9] = hp
			characterArray[10] = atk
			characterArray[11] = dfns
			characterArray[12] = spd
			characterArray[13] = c_rate
			characterArray[14] = c_dmg
			characterArray[15] = resist
			characterArray[16] = acc
			excelArray.append(characterArray)
			click_exit()
			time.sleep(1)

			saveMugShot(mugx,mugy,charName)
			mugx = mugx + 153
		else:
			print("image not found")
			break
		xcor = xcor + 155	
	xcor = None
	
	pos = imagesearch("word_index_rarity_"+rarityName+".JPG")
	xcor = pos[0]+(width/2)-825
	ycor = pos[1]+(height/2)+141
	mugx = pos[0] - 780
	mugy = pos[1] + 69
	while xcor < 1834:
		characterArray = ['','','','','','','','','','','','','','','','','']
		type = getLiveType(xcor,ycor)
		ptg.moveTo(xcor, ycor)
		ptg.click(clicks=1, button='left')#Champ bio location D:\Documents\Scripts\project-raid\raid_image_data_mine\champion_bios
		time.sleep(1)
		starPos = imagesearch("word_total_stats.JPG")
		if starPos[0] != -1:#If on bio screen
			charName = getLiveBioName()
			skill_1,skill_2,skill_3,skill_4 = getSkills()
			hp,atk,dfns,spd,c_rate,c_dmg,resist,acc = getStats()
			print("position : ", starPos[0], starPos[1])
			screenCapNox('D:\\Documents\\Scripts\\project-raid\\raid_image_data_mine\\champion_bios\\'+charName+'_bio.JPG')
			characterArray[0] = str(charName)			
			characterArray[1] = findBioBanner()
			characterArray[2] = skill_1
			characterArray[3] = skill_2
			characterArray[4] = skill_3
			characterArray[5] = skill_4
			characterArray[6] = str(rarityName)
			characterArray[7] = type
			characterArray[8] = find_element()
			characterArray[9] = hp
			characterArray[10] = atk
			characterArray[11] = dfns
			characterArray[12] = spd
			characterArray[13] = c_rate
			characterArray[14] = c_dmg
			characterArray[15] = resist
			characterArray[16] = acc
			excelArray.append(characterArray)
			click_exit()
			time.sleep(1)
			
			saveMugShot(mugx,mugy,charName)
			mugx = mugx + 153
		else:
			print("image not found")
			break
		xcor = xcor + 155
	xcor = None

if __name__ == '__main__':

	#click_mugshotword()
	findSquare()
	"""ptg.hotkey('win','down')
	click_banner('banner lords')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	click_banner('high elves')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()


	click_banner('the sacred order')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()"""
	
	
	#click_banner('barbarians')
	#click_index_rarity_word('legendary')
	#click_index_rarity_word('epic')
	"""click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	
	click_banner('orgyn tribes')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	click_banner('lizardmen')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()


	click_banner('skinwalkers')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()


	click_banner('orcs')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	drag_bottom_to_top()

	click_banner('demonspawn')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	click_banner('undead hordes')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	click_banner('dark elves')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()

	click_banner('knight revenant')
	click_index_rarity_word('legendary')
	click_index_rarity_word('epic')
	click_index_rarity_word('rare')
	click_index_rarity_word('uncommon')
	click_index_rarity_word('common')
	click_exit()"""

	#create_excel(excelArray, 'D:\\Documents\\Scripts\\project-raid\\raid_image_data_mine\\RaidCharStats.xlsx')
