import random, re

print('''------------------------------------------------------------
      ----------------------------------------------------
          ---- Bem Vindo a Criador de Personagem! ----
      ----------------------------------------------------
------------------------------------------------------------ 
''')

# Ask for a valid character name
val=False

while val==False:
    chara_name=input('Enter the character name: ')
    if re.fullmatch(r'[A-Za-z0-9 ]+',chara_name):
        val=True

#### List of Races ####
races = ['Human', 'High Elf', 'Wood Elf', 'Dark Elf', 'Dwarf', 'Beastfolk', 'Orc', 'Goblin', 'Minotaur', 'Centaur', 'Faery']
chara_race = random.choice(races)

if chara_race == 'High Elf' or chara_race == 'Wood Elf' or chara_race == 'Dark Elf' or chara_race == 'Faery' :
    age = random.randint(18, 2000)
else :
    age = random.randint(18, 45)

#### Stats #### - Assign random values to the stat and create dictionaries
attributes=dict()
lst_attributes=['str','def','dex','int','fth','cha','lck']
while True:
    att_count=0
    count=0
    for att in lst_attributes:
        attributes[att]=random.randint(1, 5)
        count+=attributes[att]
        att_count+=1
 #       print('debug:',count)
    if att_count==7 and count==20:
        break
print('debug', attributes)

# Pick a class bonus dictionary randomly, with the first item of each dict being the name of the class
warrior_stats = {'Warrior': 0, 'str': 10, 'def': 1, 'dex': 1, 'int': 1, 'fth': 1, 'cha': 1, 'lck': 1}
mage_stats = {'Mage': 0, 'str': 1, 'def': 1, 'dex': 1, 'int': 10, 'fth': 1, 'cha': 1, 'lck': 1}
archer_stats = {'Archer': 0, 'str': 1, 'def': 1, 'dex': 10, 'int': 1, 'fth': 1, 'cha': 1, 'lck': 1}
jobs=warrior_stats, mage_stats, archer_stats
chara_job = random.choice(jobs)

# Search for the att_bonus in the attributes dictionary and sum both values
for att_bonus,value in chara_job.items():
    attributes[att_bonus]=attributes.get(att_bonus,0)+value
    print('debug', att_bonus, attributes[att_bonus])

#### Character ####
print('Name: {}'.format(chara_name))
print('Race: {}'.format(chara_race))
print('Job: {}'.format(list(chara_job.keys())[0])) # Print the first key in the chara_job dict, which is class.
print('Age: {}'.format(age))
