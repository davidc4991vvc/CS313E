#  File:                RPG.py
#  Description:         A role plaing game (RPG) that allows Fighters and Wizards to attack
#                       each other and fight to the death!
#  Student's Name:      Nicolas Key
#  Student's UT EID:    nak724
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        2/3/17
#  Date Last Modified:  2/5/17

class Weapon():

    def __init__(self, myWep):
        if(myWep == "dagger" or myWep == "staff" or myWep == "sword" or myWep == "none" or myWep == "axe"):
            self.weapon = myWep

            if(myWep == "dagger"):
                self.damage = 4
            elif(myWep == "axe" or myWep == "staff"):
                self.damage = 6
            elif(myWep == "sword"):
                self.damage = 10
            elif(myWep == "none"):
                self.damage = 1
        else:
            print("Not a valid weapon type")

    def __str__(self):
        return self.weapon
    

class Armor():

    def __init__(self, myArmor):
        if(myArmor == "leather" or myArmor == "chain" or myArmor == "plate" or myArmor == "none"):
            self.armor = myArmor
            if(myArmor == "plate"):
                self.AC = 2
            elif(myArmor == "chain"):
                self.AC = 5
            elif(myArmor == "leather"):
                self.AC = 2
            elif(myArmor == "none"):
                self.AC = 10
        else:
            print("Not a valid armor type")

    def __str__(self):
        return self.armor


class Spell():

    def __init__(self, spellName):
        if(spellName == "Fireball" or spellName == "Lightning Bolt" or spellName == "Heal"):
            self.spell = spellName
            if(spellName == "Fireball"):
                self.cost = 3
                self.effect = 5
            elif(spellName == "Lightning Bolt"):
                self.cost = 10
                self.effect = 10
            elif(spellName == "Heal"):
                self.cost = 6
                self.effect = -6
        else:
            self.spell = "Not valid"

    def __str__(self):
        return self.spell

    
class RPGCharacter():

    def __init__(self, name):
        self.health = self.maxHealth
        self.spellpoints = self.maxSpellPoints
        self.name = name
        self.weapon = Weapon("none")
        self.armor = Armor("none")
        
    def unwield(self):
        self.weapon = Weapon("none")
        print(self.name, "is no longer wielding anything.")

    def takeOffArmor(self):
        self.armor = Armor("none")
        print(self.name, "is no longer wearing anything.")

    def fight(self, opponent):
        print(self.name, "attacks", opponent.name, "with a(n)", self.weapon)
        opponent.health -= self.weapon.damage
        print(self.name, "does", self.weapon.damage, "damage to", opponent.name)
        print(opponent.name, "is now down to", opponent.health, "health")
        opponent.checkForDefeat()

    def checkForDefeat(self):
        if(self.health <= 0):
            print(self.name, "has been defeated!")

    def show(self):
        print("\n", self.name)
        print("    Current Health:", self.health)
        print("    Current Spell Points:", self.spellpoints)
        print("    Wielding:", self.weapon)
        print("    Wearing:", self.armor)
        print("    Armor Class:", self.armor.AC, "\n")
            

class Fighter(RPGCharacter):

    maxHealth = 40
    maxSpellPoints = 0

    def wield(self, weapon):
        self.weapon = weapon
        print(self.name, "is now wielding a(n)", self.weapon)

    def putOnArmor(self, armor):
        self.armor = armor
        print(self.name, "is now wearing", self.armor)

    def castSpell(self, SpellName, target):
        print("Yer not a Wizard,", self.name, "- You can't cast spells!")
    

class Wizard(RPGCharacter):

    maxHealth = 16
    maxSpellPoints = 20

    def wield(self, weapon):
        if(weapon.weapon == "dagger" or weapon.weapon == "staff" or weapon.weapon == "none"):
            self.weapon = weapon
            print(self.name, "is now wielding a(n)", self.weapon)
        else:
            print("Weapon is not allowed for this character class.")

    def putOnArmor(self, armor):
        if(armor == "none"):
            self.armor = armor
            print(self.name, "is now wearing", self.armor)
        else:
            print("Armor not allowed for this character class.")

    def castSpell(self, spellName, target):
        mySpell = Spell(spellName)
        if(mySpell.spell == "Not valid"):
            print("Unknown spell name. Spell failed.")
            return
        if(self.spellpoints < mySpell.cost):
            print("Insufficient spell points")
            return
        else:
            self.spellpoints -= mySpell.cost
        print(self.name, "casts", mySpell.spell, "at", target.name)
        target.health -= mySpell.effect
        if(mySpell.spell == "Heal"):
            overMax = 0
            pointsHeal = 6
            if(target.health > target.maxHealth):
                pointsHeal = pointsHeal - (target.health - target.maxHealth)
                target.health = target.maxHealth
            print(self.name, "heals", target.name, "for", pointsHeal, "health points")
            print(target.name, "is now at", target.health, "health")
        else:
            print(self.name, "does", mySpell.effect, "damage to", target.name)
            print(target.name, "is now down to", target.health, "health")
            target.checkForDefeat()
        



def main():

    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    
    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    gandalf.show()
    aragorn.show()


main()
