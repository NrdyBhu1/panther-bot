from PIL import Image
import requests
from io import BytesIO
import pyjokes
import random

sitesList = [
    "https://longdogechallenge.com/",
    "http://heeeeeeeey.com/",
    "http://corndog.io/",
    "https://mondrianandme.com/",
    "https://puginarug.com",
    "https://alwaysjudgeabookbyitscover.com",
    "https://thatsthefinger.com/",
    "https://cant-not-tweet-this.com/",
    "https://weirdorconfusing.com/",
    "http://eelslap.com/",
    "http://www.staggeringbeauty.com/",
    "http://burymewithmymoney.com/",
    "https://smashthewalls.com/",
    "https://jacksonpollock.org/",
    "http://endless.horse/",
    "https://www.trypap.com/",
    "http://www.republiquedesmangues.fr/",
    "http://www.movenowthinklater.com/",
    "http://www.partridgegetslucky.com/",
    "http://www.rrrgggbbb.com/",
    "http://beesbeesbees.com/",
    "http://www.koalastothemax.com/",
    "http://www.everydayim.com/",
    "http://randomcolour.com/",
    "http://cat-bounce.com/",
    "http://chrismckenzie.com/",
    "https://thezen.zone/",
    "http://hasthelargehadroncolliderdestroyedtheworldyet.com/",
    "http://ninjaflex.com/",
    "http://ihasabucket.com/",
    "http://corndogoncorndog.com/",
    "http://www.hackertyper.com/",
    "https://pointerpointer.com",
    "http://imaninja.com/",
    "http://drawing.garden/",
    "http://www.ismycomputeron.com/",
    "http://www.nullingthevoid.com/",
    "http://www.muchbetterthanthis.com/",
    "http://www.yesnoif.com/",
    "http://lacquerlacquer.com",
    "http://potatoortomato.com/",
    "http://iamawesome.com/",
    "https://strobe.cool/",
    "http://www.pleaselike.com/",
    "http://crouton.net/",
    "http://corgiorgy.com/",
    "http://www.wutdafuk.com/",
    "http://unicodesnowmanforyou.com/",
    "http://chillestmonkey.com/",
    "http://scroll-o-meter.club/",
    "http://www.crossdivisions.com/",
    "http://tencents.info/",
    "https://boringboringboring.com/",
    "http://www.patience-is-a-virtue.org/",
    "http://pixelsfighting.com/",
    "http://isitwhite.com/",
    "https://existentialcrisis.com/",
    "http://onemillionlols.com/",
    "http://www.omfgdogs.com/",
    "http://oct82.com/",
    "http://chihuahuaspin.com/",
    "http://www.blankwindows.com/",
    "http://dogs.are.the.most.moe/",
    "http://tunnelsnakes.com/",
    "http://www.trashloop.com/",
    "http://www.ascii-middle-finger.com/",
    "http://spaceis.cool/",
    "http://www.donothingfor2minutes.com/",
    "http://buildshruggie.com/",
    "http://buzzybuzz.biz/",
    "http://yeahlemons.com/",
    "http://wowenwilsonquiz.com",
    "https://thepigeon.org/",
    "http://notdayoftheweek.com/",
    "http://www.amialright.com/",
    "http://nooooooooooooooo.com/",
    "https://greatbignothing.com/",
    "https://zoomquilt.org/",
    "https://dadlaughbutton.com/",
    "https://www.bouncingdvdlogo.com/",
    "https://remoji.com/",
    "http://papertoilet.com/"
]


def heck(avatar_url):
    bg = Image.open("img/hecker.png")
    avatar = Image.open(BytesIO(requests.get(avatar_url).content))
    avatar = avatar.resize((470, 470), Image.ANTIALIAS)
    bg.paste(avatar, (0, 135, 470+0, 470+135))
    return bg


def get_some_joke():
    return pyjokes.pyjokes.get_joke(language='en', category='all')


def rip(avatar_url):
    bg = Image.open("img/rip.png")
    avatar = Image.open(BytesIO(requests.get(avatar_url).content))
    avatar = avatar.resize((90, 90), Image.ANTIALIAS)
    bg.paste(avatar, (50, 90, 90+50, 90+90))
    return bg

def get_random_site():
    return random.choice(sitesList)