
import random


class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        lowest_attack_val = self.attack_strength // 2
        attack_value = random.randint(lowest_attack_val, self.attack_strength)
        return attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Hero:

    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        total_defense = 0

        if self.health == 0:
            return 0

        for armor in self.armors:
            armor_defense = armor.defend()
            total_defense += armor_defense

        return total_defense

    def take_damage(self, damage_amt):
        self.health -= damage_amt

        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        self.kills += num_kills


    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

#run attack on every ability
    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            if ability.attack() == None:
                return 0
            attack_damage = ability.attack()
            total_attack += attack_damage
        return total_attack

class Weapon(Ability):

    def attack(self):
        return random.randint(0, self.attack_strength)


class Armor:

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):

        if self.heroes == []:
            return 0

        for Hero in self.heroes:
            if Hero.name == name:
                self.heroes.remove(Hero)
            else:
                return 0

    def find_hero(self, name):

        if self.heroes == []:
            return 0

        for Hero in self.heroes:
            if Hero.name == name:
                return Hero
            else:
                return 0
            # Hero.name not in self.heroes:

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def deal_damage(self, damage):

        hero_damage = damage//len(self.heroes)
        num_hero_dead = 0

        for hero in self.heroes:
            hero.health -= hero_damage
            if hero.health <= 0:
                num_hero_dead += 1

        return num_hero_dead

        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

    def defend(self, damage_amt):

        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()

        if damage_amt > total_defense:
            damage = damage_amt - total_defense
            return self.deal_damage(damage)

    """
    This method should calculate our team's total defense.
    Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

    Return number of heroes killed in attack.
        """

    def attack(self, other_team):


        team_attack_strength = 0
        hero_kills = 0

        for hero in self.heroes:
            team_attack_strength += hero.attack()

        hero_kills = other_team.defend(team_attack_strength)

        for hero in other_team.heroes:
            hero.deaths = hero_kills

        for hero in self.heroes:
            hero.add_kill(hero_kills)

        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """


    def revive_heroes(self, health=100):

        for hero in self.heroes:
            hero.health = hero.start_health
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):

        for hero in self.heroes:
            print("{}:{}".format(self.kills, self.deaths))

        """
        This method should print the ratio of kills/deathss for each member of the team to the screen.

        This data must be output to the terminal.
        """

    def update_kills(self):

        for hero in self.heroes:
            if hero.health <= 0:
                hero.kills += 1

        """
        This method should update each hero when there is a team kill.
        """

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None


    def build_team_one(self):
        return create_team()

        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        return create_team()
        """
        This method should allow user to build team two.
        """

    def team_battle(self):

        #TODO Make users choose a random number to choose who goes first. Could be every round.
        battling = True
        while battling == True:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)

            winning_team = ""

            team_one_isdead = False
            team_two_isdead = False

            team_one_deaths = 0
            team_two_deaths = 0

            for hero in team_one.heroes:
                if hero.health <= 0:
                    team_one_deaths += 1

            for hero in team_two.heroes:
                if hero.health <= 0:
                    team_two_deaths += 1

            if team_one_deaths == len(self.team_one.heroes):
                team_one_isdead = True
                winning_team = self.team_two.name

            if team_two_deaths == len(self.team_one.heroes):
                team_two_isdead = True
                winning_team = self.team_one.name

            if team_one_isdead == True or team_two_isdead == True:
                battling = False

        print("Congrats to {} for killing all of their opponents!".format(winning_team))


        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):

        print("Team One Statistics")
        print(self.team_one.stats())

        print("Team Two Statistics")
        print(self.team_two.stats())


        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

    def is_team_dead(self, team):
        heroes_dead = 0

        for hero in self.heroes:
            if hero.health <= 0:
                heroes_dead += 1

        if heroes_dead == len(team.heroes):
            return True
        else:
            return False



    def create_team(self):

        team_name = input("What will be the name of your team?")
        team = Team(team_name)
        print("Lets start adding heroes to {}!".format(team_name))

        building_team = True
        while building_team:

            hero_name = input("Hero's name: ")
            new_hero = Hero(hero_name)
            print("What abilities do you want {} to have?".format(new_hero.name))
            #while loop to enter in as many abilities as wanted
            building_abilities = True
            while building_abilities:
                ability_name = input("Name of ability: ")
                ability_attack_strength = input("What attack strength should {} have?".format(ability_name))
                new_ability = Ability(ability_name, ability_attack_strength)
                new_hero.add_ability(new_ability)
                abilities_finished = input("Add more abilities for {}? Enter (Y/N): ".format(new_hero.name))
                if abilities_finished == "y" or "Y" or "Yes":
                    building_abilities = False
                else:
                    continue
            print("Now let's give {} some armor".format(new_hero.name))

            building_armor = True
            while building_armor:
                armor_name = input("Name of armor: ")
                armor_defense = input("Defense score: ")
                new_armor = Armor(armor_name, armor_defense)
                new_hero.add_armor(new_armor)
                building_armor_finished = input("Add more armor for {}? Enter (Y/N): ".format(new_hero.name))
                if building_armor_finished == "y" or "Y" or "Yes":
                    building_armor = False
                else:
                    continue
            team.add_hero(new_hero)

        building_team_finished = input("Are you done building {}? Enter (Y/N): ".format(team.name))
        if building_team_finished == "y" or "Y" or "Yes":
            building_team = False

        return team
