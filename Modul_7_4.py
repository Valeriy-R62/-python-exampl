team1_num = 7  # Команда "Мастера кода"
team2_num = 8  # Команда "Волшебники данных"
print('В команде Мастера кода участников: %s, В команде Волшебники данных участников %s' % (team1_num, team2_num))
team1_num, team2_num = 7, 8
print("Итого сегодня в командах участников: %s и %s" % (team1_num, team2_num))
score_1, score_2 = 33, 37
print(' Команда Мастера кода решила задач: {}, Команда Волшебники данных решила задач: {}'.format(score_1, score_2))
team1_time, team2_time = 13695.6, 13616.3
print(" Команда Мастера кода решила задачи за: {},"
      " Команда Волшебники данных решила задачи за: {}".format(team1_time, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
x_1 = score_1 - score_2
x_2 = team1_time / score_1 - team2_time / score_2
if x_1 > 0 or x_1 == 0 and x_2 > 0:
    challenge_result = 'Победа команды Мастера кода!'
elif x_1 < 0 or x_1 == 0 and x_2 < 0:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    print('Ничья')
print(f'Результат битвы:{challenge_result}')
tasks_total = score_1 +  score_2
time_avg = (team1_time + team2_time)/tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')