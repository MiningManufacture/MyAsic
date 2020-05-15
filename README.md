# MyAsic
Программа для мониторинга майнинг устройств MyAsic v.1.0 (beta)

Поддерживаемые устройства - все совместимые устройства Bitmain Antminer серии S и L

В данном релизе программа сканирует локальную сеть на наличие майнеров и получает информацию о хэшрейте через заданный
промежуток времени. Если хэшрейт майнера ниже заданного - устройство перезагружается. Сообщения посылаются в telegram
вашему боту.

Для начала работы у вас должен быть установлен Python3:

     Windows - загрузите актуальную версию с официального сайта https://www.python.org/downloads/windows/
 
          Для 64-рязрядной ОС https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe
          Для 32-рязрядной ОС https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
 
          Запустите установщик и следуйте инструкциям

    Linux - в терминале введите команду "sudo apt-get install python3" дождитесь окончания установки.

Скачайте программу на свой компьютер используя ссылку https://github.com/MiningManufacture/MyAsic/archive/master.zip
распакуйте архив у удобную вам папку

Если у вас Linux в терминале перейдите в папку куда будет распакована программа ( например  'cd \home\' ) затем 
введите 'git clone https://github.com/MiningManufacture/myasic.git'

Отредактируйте файл config.py в любом текстовом редакторе как в примере:

      #user settings####################################################

      #1) IP адрес вашего шлюза, асики будут найдены в этой же подсети

      ip_gateway = '192.168.0.1'

      #2) Для корректной работы телеграм бота необходим прокси сервер, если прокси не указан 
      ##  программа выберет любой доступный (пример ProxyServer = "http://117.54.239.18:8080")

      ProxyServer = ""

      #3) Токен для вашего телеграм бота, получить его можно у официального бота @BotFather, 
      ##  следуйте инструкциям (запуск /start, создание бота /newbot)
      ### Рекомендуем сделать бота приватным после создания 
      ###(/mybots -> выбираем бота -> Bot Settings -> Group Privacy)

      telegram_bot_id = '921875076:AAH3omROOvV8ehtDLcWiZEWAVmwT4-sQ900'

      #4) Если стоит 1 то в телегу поступают только сообщения об ошибках и перезагрузках, 
      ##  если 0 - хэшрейт по всем, если 2 то всё

      errors_only = 0

      #5) Введите логин от майнеров

      miner_login = 'root'

      #6) Введите пароль от майнеров

      miner_passw = 'root'

      #7) Укажите минимальный хэшрейт при котором асик отправляется на перезагрузку (по умолчанию 10Th\s)

      minimal_hashrate = 10000

      #8) Введите интервал сканирования в секундах (по умолчанию 1 час)

      interval_sec=3600

      #end of user settings#############################################

Запуск мониторинга:

     Windows - кнопка ПУСК - в поле "найти программы и файлы" введите команду 'python3 C:\MyAsic-master\myasic.py' 
     где MyAsic-master папка с распакованным архивом
     
     Linux - откройте терминал, перейдите в папку с программой ( например 'cd \home\myasic' ), введите 
     команду 'sudo python3 myasic.py' 

В следующих релизах будут добавлены новые функции:
- возможность перейти на веб интерфейс асика из телеграм сообщения
- сканирование на вирусы
- аналитика блокчейнов
- поддержка устройств других производителей

Если вам понравился проект и у вас есть пожелания по дальнейшему развитию свяжитесь со мной в telegram @Niko_Irk
Разработка MiningManufacture 2020
