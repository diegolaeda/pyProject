import random


def generate_kick(attack, defence):
    if(attack <= defence):
        print("Error! So much defence!")
        return 0
    
    first_attack = random.randint(1, attack)
    second_attack = random.randint(1, attack)
    third_attack = random.randint(1, attack)
    
    if(first_attack < second_attack):
        first_attack = second_attack
    if(first_attack < third_attack):
        first_attack = third_attack
        
    first_defence = random.randint(1, defence)        
    second_defence = random.randint(1, defence)
    third_defence = random.randint(1, defence)
    
    if(first_defence > second_defence):
        first_defence = second_defence
    if(first_defence > third_defence):
        first_defence = third_defence
        
    if(first_attack < first_defence):
        return 0
    
    damage = first_attack - first_defence + 1
    return damage


def main():
    print ("Привет, Python!")
    
    test_attack = 10
    test_defence = 4
    kick_damage = generate_kick(test_attack, test_defence)
    
    print("Атака: ", test_attack, " // Защита: ", test_defence)
    print("Удар на ", kick_damage, " урона.")
    
    test_attack = 10
    test_defence = 12
    kick_damage = generate_kick(test_attack, test_defence)
    
    print("Атака: ", test_attack, " // Защита: ", test_defence)
    print("Удар на ", kick_damage, " урона.")
    
    test_attack = 10
    test_defence = 9
    kick_damage = generate_kick(test_attack, test_defence)
    
    print("Атака: ", test_attack, " // Защита: ", test_defence)
    print("Удар на ", kick_damage, " урона.")
    
main()