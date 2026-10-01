import sched, time

s = sched.scheduler(time.time, time.sleep)


def say(text):
    print(f"[{time.strftime('%H:%M:%S')}] {text}")


start = time.time()
print("Старт. Отсчёт времени от t0 = 0\n")

# два события на один и тот же момент: start + 2
s.enterabs(start + 2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enterabs(start + 2, 0, say, ("Прошло 2 секунды (приоритет 0 — сработает ПЕРВЫМ)",))
s.enter(1, 1, say, ("Прошла 1 секунда",))
s.enterabs(start + 3, 1, say, ("Абсолютное время t0+3 с",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))

print("Очередь до run():", len(s.queue), "задач")
for ev in s.queue:                      # TODO
    print(ev.time - start, ev.priority, ev.argument[0])
print("run() блокирует поток, пока все задачи не выполнятся:\n")
s.run()
print("\nГотово. Пустая очередь?", s.empty())