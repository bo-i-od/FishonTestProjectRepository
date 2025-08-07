import numpy as np

def get_bonus(accumulated, thresholds, rates):
    for i, v in enumerate(thresholds):
        if accumulated < v:
            return rates[i]
    return rates[-1]

def simulate_slot(global_rate, slot_cost, slot_drop_rate, bonus_thresholds, bonus_rates, sim_times=200000):
    stamina_sum = 0
    for _ in range(sim_times):
        acc_stamina = 0
        while True:
            bonus = get_bonus(acc_stamina, bonus_thresholds, bonus_rates)
            p = global_rate * slot_drop_rate * bonus
            stamina_sum += slot_cost
            acc_stamina += slot_cost
            if p >= 1 or np.random.rand() < p:
                break
    avg_stamina = stamina_sum / sim_times
    return avg_stamina

global_rate = 1.5
slot_costs = [1,3,10,20,30,50,100,150,200,300,500,1000,2000]
slot_drop_rates = [0.02,0.02,0.1,0.1,0.1,0.1,0.15,0.2,0.2,0.2,0.35,0.35,0.35]
bonus_thresholds = [50,100,300,500,800,1000]
bonus_rates = [1.2,1.6,2,3,10,100]


for i, (cost, rate) in enumerate(zip(slot_costs, slot_drop_rates), start=1):
    avg = simulate_slot(global_rate, cost, rate, bonus_thresholds, bonus_rates)
    print(f"档位{i}: 每{cost}体力消耗，平均掉落一次需消耗体力：{avg:.2f}")