"""
Gerando dados fakers com a lib 
python faker

ideal para gerar dados para testes.

Dependencias:
>> pip install faker

Executando:
$ python faker-1.py:

"""
from faker import Faker
from faker.providers.address.pt_BR import Provider
fake = Faker('pt_BR')
fake.add_provider(Provider)

print(fake.name())
print(fake.estado_nome())
print(fake.estado_sigla())
