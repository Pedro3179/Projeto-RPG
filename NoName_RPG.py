import random

#### List of Races
races = ['Human', 'High Elf', 'Wood Elf', 'Dark Elf', 'Dwarf', 'Beastfolk', 'Orc', 'Goblin', 'Minotaur', 'Centaur', 'Faery']
chara_race = random.choice(races)

if chara_race == 'High Elf' or chara_race == 'Wood Elf' or chara_race == 'Dark Elf' or chara_race == 'Faery' :
    age = random.randint(18, 2000)
else :
    age = random.randint(18, 45)

#### Stats
while True :
    chara_str = random.randint(1, 5)
    chara_def = random.randint(1, 5)
    chara_dex = random.randint(1, 5)
    chara_int = random.randint(1, 5)
    chara_fth = random.randint(1, 5)
    chara_cha = random.randint(1, 5)
    chara_lck = random.randint(1, 5)
    total_stats = chara_str + chara_def + chara_dex + chara_int + chara_fth + chara_cha + chara_lck
    if not total_stats == 20 :
        continue
    else :
        break

# Somar os bônus de cada classe aos atributos sorteados com randint

jobs = ['Warrior', 'Mage', 'Archer']
chara_job = random.choice(jobs)

warrior_stats = {'bstr': 10, 'bdef': 1, 'bdex': 1, 'bint': 1, 'bfth': 1, 'bcha': 1, 'blck': 1}
mage_stats = {'bstr': 1, 'bdef': 1, 'bdex': 1, 'bint': 10, 'bfth': 1, 'bcha': 1, 'blck': 1}
archer_stats = {'bstr': 1, 'bdef': 1, 'bdex': 10, 'bint': 1, 'bfth': 1, 'bcha': 1, 'blck': 1}

if chara_job == 'Warrior' :
    job_stats = warrior_stats
elif chara_job == 'Mage' :
    job_stats = mage_stats
elif chara_job == 'Archer' :
    job_stats = archer_stats

job_stats = dict()

chara_str+=job_stats['bstr']
chara_def+=job_stats['bdef']
chara_dex+=job_stats['bdex']
chara_int+=job_stats['bint']
chara_fth+=job_stats['bfth']
chara_cha+=job_stats['bcha']
chara_lck+=job_stats['blck']


#### Character ####
print('Name: Generic Name') #### Sortear em uma lista de nomes. O nome deve ser baseado na raça do personagem.
print('Race: {}'.format(chara_race))
print('Job: {}'.format(chara_job))
print('Age: {}'.format(age))

print("""STR: {}
DEF: {}
DEX: {}
INT: {}
FTH: {}
CHA: {}
LCK: {}""".format(chara_str, chara_def, chara_dex, chara_int, chara_fth, chara_cha, chara_lck))

print('Debug Total Stats: {}'.format(total_stats))