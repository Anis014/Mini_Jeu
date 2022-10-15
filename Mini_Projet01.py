import gaming_tools
from gaming_tools import *
import random
from random import randint
from kiwisolver import strength

#The following function allows you to create a new character :
def create_new_character(name_character,variety):
    """Specification of the function   
        create a new character

    parameters
    -----------
    name_character : the name of your character (str)
    variety : the variety of your character (str)

    return
    -----------
        return the character informations (str)


    note
    -----------
    only use "dwarf","elf","healer","wizard", or "necromancer" for the variety
    """
    if character_exists(name_character):
        print("This character already exist")
    

    if  not variety != ('dwarf','elf','healer','wizard','necromancer'):
        print('Variety not accepted')
    else:
            if variety=="dwarf":
                strength=random.randint(10,50)
                life=random.randint(10,50)
                reach="short"
            elif variety=="elf":
                strength=random.randint(15,25)
                life=random.randint(15,25)
                reach="long"
            elif variety=="healer" or variety=="necromancer":
                strength=random.randint(5,15)
                life=random.randint(5,15)
                reach="short"
            elif variety=="wizard":
                strength=random.randint(5,15)
                life=random.randint(5,15) 
                reach="long"
   
    add_new_character(name_character,variety,reach,strength,life)
    print('The character has been created successfully with this stats : Name: %s, Variety: %s, Reach: %s, Strength: %d, Life: %d' % (name_character,variety,reach,strength,life))
    set_team_money(get_team_money() + 50)
    print('Added 50 pieces to team money balance : ', get_team_money(),' gold coins')
  



#The following function allows you to create a new creature :
def create_new_creature():
    """
        Return the creature informations (str)
    """
    if is_there_a_creature():
        print('a creature already exist, kill it first !')
        return
        
    
    name_creature=get_random_creature_name()

    if randint(0, 1)==0:
        reach = 'short'
    else:
        reach ='long'
    
    strength=random.randint(1,10)*(1 + get_nb_defeated())
    life=random.randint(1,10)*(1 + get_nb_defeated())

    add_creature(name_creature,reach,strength,life)
    print('Creature %s created with reach: %s and strength: %d and life:  %d ' % (name_creature,reach,strength,life))



def attack(name_character,name_creature):
    """Specification of the function   

    This function allows to do the attack procedure

    parameters
    -----------
    name_character : the name of the character (str)
    name_creature : the name of the creature (str)

    """
    if  not character_exists(name_character):
        print('The character %s does not exist, please check this out!' % name_character)
        return
    if get_character_life(name_character) <= 0:
        print('The character %s is already dead'% name_character)
        return    
    if not creature_exists (name_creature):
        print('The creature %s does not exist, please check this out!' % name_creature)
        return


    character_reach = get_character_reach(name_character)
    character_life = get_character_life(name_character)
    character_strength = get_character_strength(name_character)

    creature_reach = get_creature_reach(name_creature)
    creature_life = get_creature_life(name_creature)
    creature_strength = get_creature_strength(name_creature)

    if character_reach == creature_reach :
        print('%s attacks %s' % (name_character,name_creature))
        if character_strength >= creature_life :
            print('Creature is dead')
            remove_creature(name_creature)
            set_nb_defeated(get_nb_defeated()+1)
            set_team_money(get_team_money() + 40 + 10 * get_nb_defeated())
            print('Your balance after recompense is :', get_team_money(),' gold coins')
            return
        else:
            set_creature_life(name_creature , get_creature_life(name_creature) - get_character_strength(name_character))
            print('The creature %s repost to %s' % name_creature,name_character)
            if get_character_life(name_character)-get_creature_strength(name_creature) >0 :
             set_character_life(name_character, get_character_life(name_character) - get_creature_strength(name_creature))
             print('You have %d HP of life left' % get_character_life(name_character))
             return 
            else:
                print('The character %s is dead' % name_character)
                character_exists(name_character)==False
                return

    if character_reach =='short' and creature_reach=='long':
        print('You can\'t attack beacause of reach')
        print('The creature repost')
        if (get_character_life(name_character)- get_creature_strength(name_creature) > 0) :
           set_character_life(name_character, get_character_life(name_character) - get_creature_strength(name_creature))
           print('You have %d HP of life left' % get_character_life(name_character))
           return 
        else:
                print('The character %s is dead' % name_character)
                set_character_life(name_character,0)
                character_exists(name_character)==False
                return

    if character_reach=='long' and creature_reach=='short':
        print('%s attacks %s' % (name_character,name_creature))
        if character_strength >= creature_life :
            print('Creature is dead')
            remove_creature(name_creature)
            set_nb_defeated(get_nb_defeated()+1)
            set_team_money(get_team_money() + 40 + 10 * get_nb_defeated())
            print('Your balance after recompense is :', get_team_money(),' gold coins')
            return
        else:
            set_creature_life(name_creature , get_creature_life(name_creature) - get_character_strength(name_character))
            print('There is still %d of life for the creature' % get_creature_life(name_creature))
            return





def evolution_character(name_character) :
    """Specification of the function 

    The following function allows you to upgrade a character for 4 gold coins:
      -he then has a 25% chance of having his strength increased by 4
      -and a 50% chance of having his life increased by 2

    parameters
     ------
     name_character : character name (str)
    
    """
    if not character_exists(name_character):
        print('The character %s does not exist, please check this out!' % name_character)
        return
    evolution_life=randint(1,2)
    evolution_strenght=randint(1,4)
    money=get_team_money()


    if money <4 :
        print('not enought money ( %d gold coin)') %get_team_money()
        return
    else:
        money=money - 4
        if evolution_life==1:
           set_character_life(name_character, get_character_life(name_character)+2)
           print('New life of %s : %d' %(name_character,get_character_life(name_character)))
        
        if evolution_strenght==1:
            set_character_strength(name_character,get_character_strength(name_character)+4) 
    
    set_team_money(money)
    print('Team money is now : ', get_team_money(),'gold coins')
    return





def healer (name_healer,name_target):
    """Specification of the function 

    allows the healer character to increase the life gauge of a different type of character
    by 10 points in exchange for 5 gold coins from the players' pool. 

    parameters
    ----------
    name_healer:name of the character healer (str)
    name_target:name of the character who needs 10 life (str)

    """
    life = get_character_life(name_target)

    if not character_exists(name_healer):
        print('The character %s does not exist, please check this out!' % name_healer)
        return

    if not character_exists(name_target):
        print('The character %s does not exist, please check this out!' % name_target)
        return

    if get_team_money() < 5:
        print ('You don\'t have enough coins')
        return
    else :
        print('%s casts a healing spell on %s ' % (name_healer,name_target))
        #set_character_life(name_healer, life + 10)
        set_character_life(name_target, get_character_life(name_target)+10)
        set_team_money(get_team_money() - 5)

        print('The life of %s he become : '%name_target, get_character_life(name_target)) 

        print('Team money is now : ', get_team_money(),' gold coins') 
        return





def wizard_spell (name_wizard, name_target_creature):
    """Specification of the function 

    parameters
    ----------
    name_wizard:name of the character wizard (str)
    name_target_creature:name of the creature being the target of the wizard (str)

    return
    ----------

    """
    if not character_exists(name_wizard):
        print('The character %s does not exist, please check this out!' % name_wizard)
        return
    if get_character_variety(name_wizard) != 'wizard':
        print('This feature is only available for the wizard')
        return

    if not creature_exists(name_target_creature):
        print('There isn\'t any creature to cast a spell on')
        return

    if get_team_money() < 20:
        print ('You don\'t have enough coins')
        return
    else: 
        print('You cast a spell on the creature')
        set_creature_life(name_target_creature, get_creature_life(name_target_creature)/2)
        set_team_money(get_team_money() - 20)
        print('The life of the creature he become : ', get_creature_life(name_target_creature)) 

        print('Team money is now : ', get_team_money(),' gold coins') 
        return





def revive(name_necromancer,name_character):
    """Specification of the function 

    Revives a dead character for 75 gold coins and gives him 10HP

    parameters
    ----------
    name_necromancer: name of the character who casts the reviving spell  (str)
    name_character_creature: name of the ally character who gets revived (str)

    """
    life = get_character_life(name_character)
    if not character_exists(name_necromancer):
        print('The character %s does not exist, please check this out!' % name_necromancer)
        return

    if get_character_life(name_character) > 0 : 
        print('You cannot revive somebody still alive or somebody who doesn\'t exist')
        return
    if get_character_variety(name_necromancer) != 'necromancer' :
        print('You cannot revive someone if you\'re not a necromancer')
        return
    if get_team_money() < 75:
        print ('You don\'t have enough coins')
        return
    else :
        
        set_character_life(name_character, 10)
        set_team_money(get_team_money() - 75)
        print('%s has been revived and your team has lost 75 gold coins. You have still  %i gold coins' % (name_character,get_team_money()))
        return
    

import gaming_tools
from gaming_tools import *
import random
from random import randint
from kiwisolver import strength

#The following function allows you to create a new character :
def create_new_character(name_character,variety):
    """Specification of the function   
        create a new character

    parameters
    -----------
    name_character : the name of your character (str)
    variety : the variety of your character (str)

    return
    -----------
        return the character informations (str)


    note
    -----------
    only use "dwarf","elf","healer","wizard", or "necromancer" for the variety
    """
    if character_exists(name_character):
        print("This character already exist")
    

    if  not variety != ('dwarf','elf','healer','wizard','necromancer'):
        print('Variety not accepted')
    else:
            if variety=="dwarf":
                strength=random.randint(10,50)
                life=random.randint(10,50)
                reach="short"
            elif variety=="elf":
                strength=random.randint(15,25)
                life=random.randint(15,25)
                reach="long"
            elif variety=="healer" or variety=="necromancer":
                strength=random.randint(5,15)
                life=random.randint(5,15)
                reach="short"
            elif variety=="wizard":
                strength=random.randint(5,15)
                life=random.randint(5,15) 
                reach="long"
   
    add_new_character(name_character,variety,reach,strength,life)
    print('The character has been created successfully with this stats : Name: %s, Variety: %s, Reach: %s, Strength: %d, Life: %d' % (name_character,variety,reach,strength,life))
    set_team_money(get_team_money() + 50)
    print('Added 50 pieces to team money balance : ', get_team_money(),' gold coins')
  



#The following function allows you to create a new creature :
def create_new_creature():
    """
        Return the creature informations (str)
    """
    if is_there_a_creature():
        print('a creature already exist, kill it first !')
        return
        
    
    name_creature=get_random_creature_name()

    if randint(0, 1)==0:
        reach = 'short'
    else:
        reach ='long'
    
    strength=random.randint(1,10)*(1 + get_nb_defeated())
    life=random.randint(1,10)*(1 + get_nb_defeated())

    add_creature(name_creature,reach,strength,life)
    print('Creature %s created with reach: %s and strength: %d and life:  %d ' % (name_creature,reach,strength,life))



def attack(name_character,name_creature):
    """Specification of the function   

    This function allows to do the attack procedure

    parameters
    -----------
    name_character : the name of the character (str)
    name_creature : the name of the creature (str)

    """
    if  not character_exists(name_character):
        print('The character %s does not exist, please check this out!' % name_character)
        return
    if get_character_life(name_character) <= 0:
        print('The character %s is already dead'% name_character)
        return    
    if not creature_exists (name_creature):
        print('The creature %s does not exist, please check this out!' % name_creature)
        return


    character_reach = get_character_reach(name_character)
    character_life = get_character_life(name_character)
    character_strength = get_character_strength(name_character)

    creature_reach = get_creature_reach(name_creature)
    creature_life = get_creature_life(name_creature)
    creature_strength = get_creature_strength(name_creature)

    if character_reach == creature_reach :
        print('%s attacks %s' % (name_character,name_creature))
        if character_strength >= creature_life :
            print('Creature is dead')
            remove_creature(name_creature)
            set_nb_defeated(get_nb_defeated()+1)
            set_team_money(get_team_money() + 40 + 10 * get_nb_defeated())
            print('Your balance after recompense is :', get_team_money(),' gold coins')
            return
        else:
            set_creature_life(name_creature , get_creature_life(name_creature) - get_character_strength(name_character))
            print('The creature %s repost to %s' % name_creature,name_character)
            if get_character_life(name_character)-get_creature_strength(name_creature) >0 :
             set_character_life(name_character, get_character_life(name_character) - get_creature_strength(name_creature))
             print('You have %d HP of life left' % get_character_life(name_character))
             return 
            else:
                print('The character %s is dead' % name_character)
                character_exists(name_character)==False
                return

    if character_reach =='short' and creature_reach=='long':
        print('You can\'t attack beacause of reach')
        print('The creature repost')
        if (get_character_life(name_character)- get_creature_strength(name_creature) > 0) :
           set_character_life(name_character, get_character_life(name_character) - get_creature_strength(name_creature))
           print('You have %d HP of life left' % get_character_life(name_character))
           return 
        else:
                print('The character %s is dead' % name_character)
                set_character_life(name_character,0)
                character_exists(name_character)==False
                return

    if character_reach=='long' and creature_reach=='short':
        print('%s attacks %s' % (name_character,name_creature))
        if character_strength >= creature_life :
            print('Creature is dead')
            remove_creature(name_creature)
            set_nb_defeated(get_nb_defeated()+1)
            set_team_money(get_team_money() + 40 + 10 * get_nb_defeated())
            print('Your balance after recompense is :', get_team_money(),' gold coins')
            return
        else:
            set_creature_life(name_creature , get_creature_life(name_creature) - get_character_strength(name_character))
            print('There is still %d of life for the creature' % get_creature_life(name_creature))
            return





def evolution_character(name_character) :
    """Specification of the function 

    The following function allows you to upgrade a character for 4 gold coins:
      -he then has a 25% chance of having his strength increased by 4
      -and a 50% chance of having his life increased by 2

    parameters
     ------
     name_character : character name (str)
    
    """
    if not character_exists(name_character):
        print('The character %s does not exist, please check this out!' % name_character)
        return
    evolution_life=randint(1,2)
    evolution_strenght=randint(1,4)
    money=get_team_money()


    if money <4 :
        print('not enought money ( %d gold coin)') %get_team_money()
        return
    else:
        money=money - 4
        if evolution_life==1:
           set_character_life(name_character, get_character_life(name_character)+2)
           print('New life of %s : %d' %(name_character,get_character_life(name_character)))
        
        if evolution_strenght==1:
            set_character_strength(name_character,get_character_strength(name_character)+4) 
    
    set_team_money(money)
    print('Team money is now : ', get_team_money(),'gold coins')
    return





def healer (name_healer,name_target):
    """Specification of the function 

    allows the healer character to increase the life gauge of a different type of character
    by 10 points in exchange for 5 gold coins from the players' pool. 

    parameters
    ----------
    name_healer:name of the character healer (str)
    name_target:name of the character who needs 10 life (str)

    """
    life = get_character_life(name_target)

    if not character_exists(name_healer):
        print('The character %s does not exist, please check this out!' % name_healer)
        return

    if not character_exists(name_target):
        print('The character %s does not exist, please check this out!' % name_target)
        return

    if get_team_money() < 5:
        print ('You don\'t have enough coins')
        return
    else :
        print('%s casts a healing spell on %s ' % (name_healer,name_target))
        #set_character_life(name_healer, life + 10)
        set_character_life(name_target, get_character_life(name_target)+10)
        set_team_money(get_team_money() - 5)

        print('The life of %s he become : '%name_target, get_character_life(name_target)) 

        print('Team money is now : ', get_team_money(),' gold coins') 
        return





def wizard_spell (name_wizard, name_target_creature):
    """Specification of the function 

    parameters
    ----------
    name_wizard:name of the character wizard (str)
    name_target_creature:name of the creature being the target of the wizard (str)

    return
    ----------

    """
    if not character_exists(name_wizard):
        print('The character %s does not exist, please check this out!' % name_wizard)
        return
    if get_character_variety(name_wizard) != 'wizard':
        print('This feature is only available for the wizard')
        return

    if not creature_exists(name_target_creature):
        print('There isn\'t any creature to cast a spell on')
        return

    if get_team_money() < 20:
        print ('You don\'t have enough coins')
        return
    else: 
        print('You cast a spell on the creature')
        set_creature_life(name_target_creature, get_creature_life(name_target_creature)/2)
        set_team_money(get_team_money() - 20)
        print('The life of the creature he become : ', get_creature_life(name_target_creature)) 

        print('Team money is now : ', get_team_money(),' gold coins') 
        return





def revive(name_necromancer,name_character):
    """Specification of the function 

    Revives a dead character for 75 gold coins and gives him 10HP

    parameters
    ----------
    name_necromancer: name of the character who casts the reviving spell  (str)
    name_character_creature: name of the ally character who gets revived (str)

    """
    life = get_character_life(name_character)
    if not character_exists(name_necromancer):
        print('The character %s does not exist, please check this out!' % name_necromancer)
        return

    if get_character_life(name_character) > 0 : 
        print('You cannot revive somebody still alive or somebody who doesn\'t exist')
        return
    if get_character_variety(name_necromancer) != 'necromancer' :
        print('You cannot revive someone if you\'re not a necromancer')
        return
    if get_team_money() < 75:
        print ('You don\'t have enough coins')
        return
    else :
        
        set_character_life(name_character, 10)
        set_team_money(get_team_money() - 75)
        print('%s has been revived and your team has lost 75 gold coins. You have still  %i gold coins' % (name_character,get_team_money()))
        return
    

            


def end_game():
    """Specification of the function 
    
    """
    print('Game ended with ',get_nb_defeated(),' creatures killed')
    reset_game()







def end_game():
    """Specification of the function 
    
    """
    print('Game ended with ',get_nb_defeated(),' creatures killed')
    reset_game()




