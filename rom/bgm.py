

class BGM:
	base_address = 0x39A7

	index = 0
	bgm_id = 0

	

#bgm data classes

class SpringBGM(BGM):
	index = 0
	bgm_id = 1

class SummerBGM(BGM):
	index = 1
	bgm_id = 2

class FallBGM(BGM):
	index = 2
	bgm_id = 7

class WinterBGM(BGM):
	index = 3
	bgm_id = 4

class SpringTownBGM(BGM):
	index = 4
	bgm_id = 5

class SummerTownBGM(BGM):
	index = 5
	bgm_id = 5

class FallTownBGM(BGM):
	index = 6
	bgm_id = 5

class WinterTownBGM(BGM):
	index = 7
	bgm_id = 5

class SpringMountainBGM(BGM):
	index = 8
	bgm_id = 6

class SummerMountainBGM(BGM):
	index = 9
	bgm_id = 6

class FallMountainBGM(BGM):
	index = 10
	bgm_id = 6

class WinterMountainBGM(BGM):
	index = 11
	bgm_id = 6

#harvest fests not accurate
class HarvestFestBGM(BGM):
	index = 12
	bgm_id = 3

class HarvestFest2BGM(BGM):
	index = 13
	bgm_id = 3

class HarvestFest3BGM(BGM):
	index = 14
	bgm_id = 3

class HarvestFest4BGM(BGM):
	index = 15
	bgm_id = 3

class StarryNightBGM(BGM):

