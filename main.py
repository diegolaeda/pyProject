from battle import *


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