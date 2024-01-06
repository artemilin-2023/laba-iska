# Лаба для Искандера
Я мог бы смотреть провожающую в последний путь Фрирен, но вместо этого делал лабу для одного гениального МИРЭА'шника....
### Навигация:
  - [Начать работу](#начать-работу)
    - [Windows](#windows)
    - [Termux (android device)](#termux-android-device)

## Начать работу
### Windows
Крч, открываешь cmd от имени администратора, затем:
1. Скачиваешь инструменты
```
winget install Git.Git
winget install Python.Python.3.10
```
Теперь открываешь PowerShell от имени администратора  
2. Клонируешь репозиторий (предварительно меняешь дирректорию на ту, куда хочешь скачать проект)
```
git clone https://github.com/artemilin-2023/laba-iska.git
cd ./laba-iska
```
3. Качаешь переменное окружение
```
pip install virtualenv
```
4. Создаешь его и активируешь
```
virtualenv venv
Set-ExecutionPolicy Unrestricted -Force
./venv/Scripts/activate
```
6. Устанавливаешь зависимости
```
pip install -r requirement.txt
```
6. Можешь запустить проет вот так:
```
python main.py
```

### Termux (android device)
Эта вкладка мне чисто по приколу
1. Скачиваешь инструменты
```
pkg update && pkg -y upgrade
pkg install git
pkg install python && pkg install python2 && pkg install python3
```
2. Клонируешь репозиторий (предварительно меняешь дирректорию на ту, куда хочешь скачать проект)
```
git clone https://github.com/artemilin-2023/laba-iska.git
cd ./laba-iska
```
3. Качаешь переменное окружение
```
pip install virtualenv
```
4. Создаешь его и активируешь
```
virtualenv venv
source ./venv/bin/activate
```
6. Устанавливаешь зависимости
```
pip install -r requirement.txt
```
6. Можешь запустить проет вот так:
```
python main.py
```

