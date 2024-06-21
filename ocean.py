class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_name

    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'#Formatar de um jeito amigavel 
    
    def __repr__(self):
        return f'Ocean (\'{self.name}\', {self.age})' #formatar de um jeito tecnico para o progamador
    
obj = Ocean('Golfinho', 15)

print("__str__() string: ", obj.__str__())#jeito errado de fazer a chamada
print("str() string: ", str(obj))#maneira correta de fazer a chamada

print("__repr__() string: ", obj.__repr__())#jeito errado de fazer a chamada
print("repr() string: ", repr(obj))#maneira correta de fazer a chamada

""" E nois
"""
''''No início, o Universo foi criado. Isso irritou profundamente muitas pessoas e, no geral, foi encarado como uma péssima ideia. '''