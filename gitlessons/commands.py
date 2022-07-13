GIT - это распределенная система контроля версий (СВК) 
это система для отслеживания и введения истории изменений ваших файлов или проектов

Репозиторий - это хранилище ваших файлов, которые вы отслеживаете при помощи ГИТа, и их изменений 

Комманды GIT: 
1. git init -  пишется первый и единственный раз в начале нового репозитория, команда создает новый гит репозиторий локально на вашем ПК , создаст она в той директрии , где вы запускаете эту команду.

2.  git add - когда мы создаем или изменяем файлы, то при помощи этой команды мы загружаем все изменения в промежуточное место

git add <file_name>
git add . - все в текущей директории
 
   git commit  - как только мы достигаем определенного момента разработки , то мы сохраняем и комментируем все наши изменения в репозитории. Фиксация изменений в РЕПО (репозиторий)
   git commit -m '<comment>'
   
  4. git remote add - это команда для того чтобы связать ваш локальный репозиторий с удаленном репозиторем  (репо в Гитхабе)
  git remote add <название подключения> <ссылка на репозиторий>
  
  git remote add origin <url>
  
  git push  - после коммита изменений при помощи этой команды отправляем наши изменения в файле на удаленный репо
  git push <origin> <название ветки>
  
  git push origin main
  
  ________________________________________
  
  
  1. git init 
  2. git branch -M main (rename main from master)
  3. git add . 
  4. git commit -m 'comment' (все добавлено в локальный репо)
  5. git remote add origin <url>
  6. git push origin main
  \\\\\\\\\
  git add .
  git commit -m 'comment'
  git push origin main
  
  
  
  
  
  
  
  
  
