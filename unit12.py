# ## 딕셔너리

# # 딕셔너리 : 연관된 값을 묶어서 저장
# # 사전에서 단어를 찾듯이 값을 가져올 수 있다고해서 딕셔너리라고 부름
# lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# print(lux)

# # 키 이름이 중복되면?
# lux = {'health': 490, 'health': 800, 'mana':334, 'melee': 550, 'armor': 18.72}
# # 키가 중복되던 가장 뒤에 있는 값만 사용
# print(lux['health'])
# # 중복되는 키 저장 X
# print(lux)

# # 키 : 리스트, 딕셔너리 XX
# # 값 : 모든 자료형 가능
# # 빈 딕셔너리 : {} or dict()


# # 딕셔너리 만들기
# lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
# print(lux1)

# lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334 , 550, 18.72]))
# print(lux2)

# # 딕셔너리 키 접근
# print(lux2['health'])

# # 딕셔너리 키에 값 할당
# lux2['health'] = 2037
# print(lux2)

# # 딕셔너리에 키 있는지 확인할려면 in 연산자

# lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# print(len(lux))


# # 연습문제
# camille = {
#     'health': 575.6,
#     'health_regen': 1.7,
#     'mana': 338.8,
#     'mana_regen': 1.63,
#     'melee': 125,
#     'attack_damage': 60,
#     'attack_speed': 0.625,
#     'armor': 26,
#     'magic_resistance': 32.1,
#     'movement_speed': 340
# }
 
# print(                   )
# print(                   )

# # 출력
# # 575.6
# # 340

# print(camille['health'])
# print(camille['movement_speed'])



# 심사문제
key = input().split()
value = map(float, input().split())
dic = dict(zip(key, value))
print(dic)