#!/usr/bin/python3
"""
    Script used to scrap the Dota Buff website to retrieve counters of some hero.
    Created: Oct, 21 2020.
"""
import sys
import requests
import time
from bs4 import BeautifulSoup

heroes = ["abaddon",
"alchemist",
"ancient-apparition",
"anti-mage",
"arc-warden",
"axe",
"bane",
"batrider",
"beastmaster",
"bloodseeker",
"bounty-hunter",
"brewmaster",
"bristleback",
"broodmother",
"centaur-warrunner",
"chaos-knight",
"chen",
"clinkz",
"clockwerk",
"crystal-maiden",
"dark-seer",
"dark-willow",
"dawnbreaker",
"dazzle",
"death-prophet",
"disruptor",
"doom",
"dragon-knight",
"drow-ranger",
"earth-spirit",
"earthshaker",
"elder-titan",
"ember-spirit",
"enchantress",
"enigma",
"faceless-void",
"grimstroke",
"gyrocopter",
"hoodwink",
"huskar",
"invoker",
"io",
"jakiro",
"juggernaut",
"keeper-of-the-light",
"kunkka",
"legion-commander",
"leshrac",
"lich",
"lifestealer",
"lina",
"lion",
"lone-druid",
"luna",
"lycan",
"magnus",
"marci",
"mars",
"medusa",
"meepo",
"mirana",
"monkey-king",
"morphling",
"naga-siren",
"natures-prophet",
"necrophos",
"night-stalker",
"nyx-assassin",
"ogre-magi",
"omniknight",
"oracle",
"outworld-devourer",
"pangolier",
"phantom-assassin",
"phantom-lancer",
"phoenix",
"primal-beast",
"puck",
"pudge",
"pugna",
"queen-of-pain",
"razor",
"riki",
"rubick",
"sand-king",
"shadow-demon",
"shadow-fiend",
"shadow-shaman",
"silencer",
"skywrath-mage",
"slardar",
"slark",
"snapfire",
"sniper",
"spectre",
"spirit-breaker",
"storm-spirit",
"sven",
"techies",
"templar-assassin",
"terrorblade",
"tidehunter",
"timbersaw",
"tinker",
"tiny",
"treant-protector",
"troll-warlord",
"tusk",
"underlord",
"undying",
"ursa",
"vengeful-spirit",
"venomancer",
"viper",
"visage",
"void-spirit",
"warlock",
"weaver",
"windranger",
"winter-wyvern",
"witch-doctor",
"wraith-king",
"zeus"]

counters = []

def dotaBuffScrapping(hero):
    # Set the URL you want to webscrape from
    url = "https://www.dotabuff.com/heroes/" + hero + "/counters"

    # Connect to the URL. User agent is to prevent the browser to give the 429 response (too many requests)
    response = requests.get(url, headers = {'User-agent': 'your bot 0.1'})

    # Give some time to load the page
    time.sleep(1)

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all barcodes on the page
    heroesOfTr = soup.find_all("tr", limit=11)
    heroesOfTr.reverse()
    heroesOfTr = heroesOfTr[:5]
    heroesOfTr.reverse()

    if heroesOfTr is not None:
        temp = []
        for hero in heroesOfTr:
            value = hero.find("td").find("a").find("img")['alt']
            if value == "Nature's Prophet":
                value = "Natures Prophet"
            temp.append(value)
        
        counters.append(temp)

def savefile():
    save_text = open("countersByHero", 'w')
    save_text.write(",".join(str(x) for x in counters))
    save_text.close()

def doLoopThroughHeroes():    
    for hero in heroes:
        print(f"Parsing {hero}...")
        dotaBuffScrapping(hero)
        time.sleep(1)
    savefile()

def herofinder(myhero):
    for hero in heroes:
        if hero == myhero:
            dotaBuffScrapping(hero)
            time.sleep(1)
            savefile()
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) == 1:
        doLoopThroughHeroes()
        print("DotaBuffScrapping Done! Open countersByHero file to check out the results")

    elif len(sys.argv) == 2:
        h = sys.argv[1]
        if herofinder(h):
                    print(f"DotaBuffScrapping Done! Open countersByHero file to check {h}'s counters")
        else:
            print("Error: Hero Not Found")

    else:
        print("Error: unknown hero")
