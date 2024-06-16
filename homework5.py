# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = 1, 'Hello', True, [1, 2, 3]

immutable_tuple = tuple(immutable_var)
mutable_list = list(immutable_var)

print(immutable_tuple[1])
print(mutable_list[3][1])

print('Immutable tuple:', immutable_tuple)
print('Mutable list:', mutable_list)
print('Immutable tuple:', type(immutable_tuple), ',', 'Mutable list:', type(mutable_list))

# Объясните, почему нельзя изменить значения элементов кортежа.
# Кортежи задумывались как неизменяемые списки, поэтому изменение элементов невозможно. Кортежи являются упорядоченными
# и неизменяемыми,предназначены для хранения неизменяемых структур данных.
