# Лаба для Искандера
Я мог бы смотреть провожающую в последний путь Фрирен, но вместо этого делал лабу для одного гениального МИРЭА'шника....

## Начать работу
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
source ./venv/Scripts/activate
```
5. Можешь запустить проет вот так:
```
python main.py
```

