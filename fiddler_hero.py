#-*- coding: UTF-8 -*-
'''
fiddler爬取王者荣耀盒子app里英雄与装备信息
'''
from urllib.request import urlretrieve
import requests
import os

"""
函数说明:下载《英雄联盟盒子》中的英雄图片
Parameters:
    url - GET请求地址，通过Fiddler抓包获取
    header - headers信息
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_imgs_download(url, header):
    req = requests.get(url = url, headers = header).json()
    hero_num = len(req['list'])
    print('一共有%d个英雄' % hero_num)
    hero_images_path = 'hero_images'
    for each_hero in req['list']:
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'
        filename = hero_images_path + '/' + hero_name
        if hero_images_path not in os.listdir():
            os.makedirs(hero_images_path)
        urlretrieve(url = hero_photo_url, filename = filename)
"""
函数说明:打印所有英雄的名字和ID
Parameters:
    url - GET请求地址，通过Fiddler抓包获取
    header - headers信息
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_list(url, header):
	print('*' * 100)
	print('\t\t\t\t欢迎使用《王者荣耀》出装下助手！')
	print('*' * 100)
	req = requests.get(url = url, headers = header).json()
	flag = 0
	for each_hero in req['list']:
		flag += 1
		print('%s的ID为:%-7s' % (each_hero['name'], each_hero['hero_id']), end = '\t\t')
		if flag == 3:
			print('\n', end = '')
			flag = 0
            
"""
函数说明:根据equip_id查询武器名字和价格
Parameters:
    equip_id - 武器的ID
    weapon_info - 存储所有武器的字典
Returns:
    weapon_name - 武器的名字
    weapon_price - 武器的价格
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def seek_weapon(equip_id, weapon_info):
	for each_weapon in weapon_info:
		if each_weapon['equip_id'] == str(equip_id):
			weapon_name = each_weapon['name']
			weapon_price = each_weapon['price']
			return weapon_name, weapon_price
