import random
import math

def func(x):
  T = 8760;
  return ((x[0] > T and x[1] > T) or (x[2] > T and x[3] > T)) and (x[4] > T) and (x[5] > T) and (
          (x[6] > T and x[7] > T) or (x[8] > T and x[9] > T) or (x[10] > T and x[11] > T))

def work(L):
  N = 9538
  m = 3
  lambdaF = [40 * pow(10, -6), 10 * pow(10, -6), 80 * pow(10, -6)]

  # изначальная схема
  n = [4, 2, 6]
  d = 0

  # цикл по кол-ву итераций
  for k in range(0, N):
    x = []
    for i in range(0, m):
      t = []
      # для каждого элемента в нашей схеме
      for j in range(0, n[i]):
        # генерируем время отказа каждой его части
        alpha = random.random()
        t.append(-math.log(alpha) / lambdaF[i])
      for j in range(0, L[i]):
        # ДЛЯ КАЖДОЙ ЗАМЕНЫ КОТОРАЯ ПОТРЕБУЕТСЯ ПЕРВОЙ МЫ ТАКЖЕ ФОМРИРУЕМ ВРЕМЯ ОТКАЗА
        l = t.index(min(t))
        t[l] = t[l] - math.log(random.random()) / lambdaF[i]
      for j in range(0, n[i]):
        # полученные время отказа мы сохраняем в массив
        x.append(t[j])
    if not func(x):
        # ЕСЛИ У НАС ОТКАЗ - УВЕЛИЧИВАЕМ ЕГО СЧЕТЧИК
        d = d + 1
  # ВОЗВРАЩАЕМ РЕЗУЛЬТАТ КАК ВЕРОЯТНОСТЬ ОТКАЗА
  return 1 - d / N


P0 = 0.999
L = [0, 0, 0]
startCount = 4
finishCount = 9

for i in range (startCount, finishCount):
  L[0] = i
  for j in range(startCount, finishCount):
    L[1] = j
    for s in range(startCount, finishCount):
      L[2] = s
      # СЧИТАЕМ ВЕРОТНОСТЬ ОКАЗАЗА, ВЫВОДИМ С НАИЛУЧШЕЙ КОМБИНАЦИЕЙ
      P = work(L)
      if (P > P0):
        print("P = ", P, " L = ", L, " sum(L) = ", sum(L))


# P =  0.9990564059551269  L =  [6, 5, 8]  sum(L) =  19
# P =  0.9991612497378906  L =  [7, 7, 8]  sum(L) =  22
# P =  0.9993709373034179  L =  [8, 8, 8]  sum(L) =  24