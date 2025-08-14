import random

#### List of Races
races = ['Human', 'High Elf', 'Wood Elf', 'Dark Elf', 'Dwarf', 'Beastfolk', 'Orc', 'Goblin', 'Minotaur', 'Centaur', 'Faery']
chara_race = random.choice(races)

if chara_race == 'High Elf' or chara_race == 'Wood Elf' or chara_race == 'Dark Elf' or chara_race == 'Faery' :
    age = random.randint(18, 2000)
else :
    age = random.randint(18, 45)

#### Stats - sorteia valores aleatórios p/ as stats e cria um dict
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

# Sorteia a classe

warrior_stats = {'Warrior': 0, 'str': 10, 'def': 1, 'dex': 1, 'int': 1, 'fth': 1, 'cha': 1, 'lck': 1}
mage_stats = {'Mage': 0, 'str': 1, 'def': 1, 'dex': 1, 'int': 10, 'fth': 1, 'cha': 1, 'lck': 1}
archer_stats = {'Archer': 0, 'str': 1, 'def': 1, 'dex': 10, 'int': 1, 'fth': 1, 'cha': 1, 'lck': 1}
jobs=warrior_stats, mage_stats, archer_stats
chara_job = random.choice(jobs) #Sorteei os dict de bonus da classe direto, com o primeiro item sendo o nome da classe.

#print('debug class:',list(chara_job.keys())[0]) # Retorna e dá print na primeira key do dict

for att_bonus,value in chara_job.items():
    attributes[att_bonus]=attributes.get(att_bonus,0)+value #Procura pelo att_bonus no dict de att e soma o valor dos dois
    print('debug', att_bonus, attributes[att_bonus])

#### Character ####
print('Name: Generic Name') #### Sortear em uma lista de nomes. O nome deve ser baseado na raça do personagem.
print('Race: {}'.format(chara_race))
print('Job: {}'.format(list(chara_job.keys())[0]))  # Dá print na primeira key do dict chara_job, que é a classe.
print('Age: {}'.format(age))
