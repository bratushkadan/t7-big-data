# ПР2

## Зависимости

Подготовка к установке зависимостей
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Первичная установка зависимостей:

```bash
pip3 install scikit-learn
pip3 freeze > requirements.txt
```

Установка зависимостей из requirements.txt
```bash
pip3 install -r requirements.txt
```

## Задание

### Датасет для t1-5

Взял датасет отсюда: https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html.

*Titanic Passengers*
Instances: 887
Features:
- Pclass - int
- Survived - int (0/1)
- Name - string
- Sex - string (male/female)
- Age - int
- Siblings/Spouses Aboard - int
- Parents/Children Aboard - int
- Fare - float

### Датасет для t6

https://archive.ics.uci.edu/dataset/292/wholesale+customers

1)	FRESH: annual spending (m.u.) on fresh products (Continuous);

2)	MILK: annual spending (m.u.) on milk products (Continuous);

3)	GROCERY: annual spending (m.u.)on grocery products (Continuous);

4)	FROZEN: annual spending (m.u.)on frozen products (Continuous)

5)	DETERGENTS_PAPER: annual spending (m.u.) on detergents and paper products (Continuous) 

6)	DELICATESSEN: annual spending (m.u.)on and delicatessen products (Continuous); 

7)	CHANNEL: customersâ€™ Channel - Horeca (Hotel/Restaurant/CafÃ©) or Retail channel (Nominal)

8)	REGION: customersâ€™ Region â€“ Lisnon, Oporto or Other (Nominal)

Descriptive Statistics:
(Minimum, Maximum, Mean, Std. Deviation)

FRESH (	3, 112151, 12000.30, 12647.329)

MILK	(55, 73498, 5796.27, 7380.377)

GROCERY	(3, 92780, 7951.28, 9503.163)

FROZEN	(25, 60869, 3071.93, 4854.673)

DETERGENTS_PAPER (3, 40827, 2881.49, 4767.854)

DELICATESSEN (3, 47943, 1524.87, 2820.106)



REGION	Frequency

Lisbon	77

Oporto	47

Other Region	316

Total	440



CHANNEL	Frequency

Horeca	298

Retail	142

Total	440


### Запуск

1-4:
```bash
python3 t1-4.py
```

5:
```bash
python3 t5.py
```
