import matplotlib.pyplot as plt
c1_year = 60000                                               #Стоимость 1С в год
internet_year = 12000                                         #Стоимость интернета в год
number_of_students = 20                                       #Количество студентов в группе
bachelor_groups = 4                                           #Количество групп бакалавриата
graduate_groups = 2                                           #Количество групп магистратуры
building_area = 1600                                          #Площадь здания
communal_expenses = building_area * 100                       #Комунальные расходы в год (в среднем 100 руб за кв)
chancellery = 60000                                           #Расходы на канцелярию за 10 месяцев (с учетом бумаги)
siz = 10000                                                   #Септики и маски на 10 месяцев
technology_update = 350000                                    #Стоимость обновления оборудования раз в 5 лет (расходы разделены на год)
#Предметы - Название[Часы лекций, практик]
#1 курс
foreign_language_1 = [0, 64]                                  #Иностранный язык
infor_and_prog = [96, 64]                                     #Информатика и программирование
higher_math_1 = [96, 96]                                      #Высшая математика
discrete_math = [64, 64]                                      #Дискретная математика
robot_programming = [16, 32]                                  #Программирование роботов
pchmi = [16, 16]                                              #Проектирование человеко-машинного интерфейса
computer_math_systems = [16, 16]                              #Системы компьютерной математики
visual_prog_technologies = [16, 32]                           #Технологии визуального программирования
#2 курс
java = [32, 16]                                               #Java
asd = [64, 64]                                                #Алгоритмы и структуры данных
сomputing_systems_architecture = [48, 16]                     #Архитектура вычислительных систем
introduction_to_iot = [16, 32]                                #Введение в интернет вещей
higher_math_2 = [32, 32]                                      #Высшая математика
documenting_software = [16, 32]                               #Документирование ПО
foreign_language_2 = [0, 64]                                  #Иностранный язык
Mathematical_logic_and_theory_of_algorithms = [32, 32]        #Математическая логика и теория алгоритмов
computer_graphics = [32, 32]                                  #Компьютерная графика
software_engineering = [32, 0]                                #Конструирование программного обеспечения
optimization_methods_2 = [32, 16]                             #Методы оптимизации
os = [48, 16]                                                 #Операционные системы
database_technologies = [32, 32]                              #Технологии баз данных
iot_technologies = [16, 32]                                   #Технологии Интернета вещей
#3 курс
parallel_programming = [32, 32]                               #Параллельное программирование
internet_technologies = [16, 16]                              #Технологии сети Интернет
requirements_development_and_analysis = [16, 16]              #Разработка и анализ требований
telecommunication_systems_management = [16, 16]               #Управление системами телекоммуникаций
image_processing = [32, 16]                                   #Обработка изображений
introduction_to_software_engineering = [32, 0]                #Введение в программную инженерию
optimization_methods_3 = [16, 16]                             #Методы оптимизации
computer_networks = [16, 16]                                  #Компьютерные сети
numerical_methods = [32, 32]                                  #Численные методы
prof_cpp = [16, 16]                                           #Профессиональный C++
software_testing = [16, 16]                                   #Тестирование программного обеспечения
programming_tools = [32, 0]                                   #Инструменты программирования
dev_java_network_app = [16, 16]                               #Разработка сетевых приложений на Java
mobile_systems_programming = [32, 16]                         #Программирование мобильных систем
physics = [32, 16]                                            #Физика
familiarization_practice_3 = [48, 0]                          #Ознакомительная практика
technological_practice = [48, 0]                              #Технологическая практика
big_data_engineering = [16, 16]                               #инженерия больших данных
#4 курс
theory_of_automata_and_formal_languages = [32, 32]            #Теория автоматов и формальных языков
economics_of_software_engineering = [32, 16]                  #Экономика программной инженерии
socio_ethical_issues_of_information_technology = [16, 16]     #Социально-этические вопросы информационных технологий
information_tеchnology_security_fundamentals = [24, 0]        #Основы безопасности информационных технологий
operations_research = [48, 24]                                #Исследование операций
systems_theory_and_systems_analysis = [24, 0]                 #Теория систем и системный анализ
software_project_management = [16, 32]                        #Управление программными проектами
distributed_processing_technology = [24, 12]                  #Технология распределённой обработки
design_and_architecture_of_software_systems = [16, 16]        #Проектирование и архитектура программных систем
programming_on_new_architectures = [16, 32]                   #Программирование на новых архитектурах
fundamentals_of_computer_vision = [16, 16]                    #Основы компьютерного зрения
cloud_computing = [12, 12]                                    #Облачные вычисления
research_work_4 = [180, 0]                                    #Научно-исследовательская работа
undergraduate_practice = [180, 0]                             #Преддипломная практика
#5 курс
english_5 = [0, 32]                                           #Английский язык
legal_and_economic_aspects_of_it = [16, 16]                   #Правовые и экономические аспекты ИТ
it_company_economic_statistics = [0, 32]                      #Экономическая статистика ИТ компании
modern_databases = [16, 32]                                   #Современные базы данных
decision_choice_models = [0, 32]                              #Модели выбора решений
it_project_management = [32, 0]                               #Управление ИТ-проектами
analysis_and_software_design = [16, 16]                       #Анализ и проектирование ПО
requirements_analysis = [16, 16]                              #Анализ требований
parallel_numerical_methods = [32, 32]                         #Параллельные численные методы
software_design_patterns = [16, 16]                           #Шаблоны проектирования ПО
modern_computer_graphics = [16, 32]                           #Современная компьютерная графика
iot = [16, 16]                                                #Интернет вещей
big_data = [16, 16]                                           #Большие данные
performance_analysis_and_software_optimization = [16, 16]     #Анализ производительности и оптимизация ПО
programming_in_scripting_languages = [16, 16]                 #Программирование на скриптовых языках
fundamentals_of_robotics = [16, 16]                           #Основы робототехники
familiarization_practice_5 = [20, 0]                          #Ознакомительная практика
research_work_5 = [20, 0]                                     #Научно-исследовательская работа
#6 курс

#ЗП сотрудников
methodist_1 = 35000                                           #Методист
methodist_2 = 36000                                           #Старший методист

accountant_1 = 40000                                          #Бухгалтер
accountant_2 = 45000                                          #Главный бухгалтер

system_administrator = 45000                                  #Системный администратор

сleaner = 20000                                               #Уборщик
cloakroom_attendant = 20000                                   #Гардеробщик
#Функция расчета ЗП преподавателей
#Годовой оклад + нагрузка, деленая на 12 месяцев

def salary_of_employees(lectures, practices, number_of_groups):
    return (192000 + ((lectures * 300) + (practices * 420)) * number_of_groups) /12
#Расчет ЗП преподавателей бакалавриата

teacher_1 = salary_of_employees(infor_and_prog[0] + robot_programming[0] + computer_math_systems[0], 
                                infor_and_prog[1] + robot_programming[1] + computer_math_systems[1], 4)

teacher_2 = salary_of_employees(higher_math_1[0] + higher_math_2[0] +  discrete_math[0] + 
                                Mathematical_logic_and_theory_of_algorithms[0], 0, 8)

teacher_3 = salary_of_employees( 0, foreign_language_1[1] + foreign_language_2[1], 8)
teacher_4 = salary_of_employees(visual_prog_technologies[0] + pchmi[0], visual_prog_technologies[1] + pchmi[1], 4)
teacher_5 = salary_of_employees(java[0] +  asd[0] + сomputing_systems_architecture[0],
                                java[1] +  asd[1] + сomputing_systems_architecture[1], 4)

teacher_6 = salary_of_employees(introduction_to_iot[0] + documenting_software[0] + software_engineering[0], 
                                documenting_software[1] + introduction_to_iot[1], 4)

teacher_7 = salary_of_employees(0, higher_math_1[1] +  discrete_math[1] +
                                Mathematical_logic_and_theory_of_algorithms[1], 8)
                                
teacher_8 = salary_of_employees(computer_graphics[0] + image_processing[0], 
                                computer_graphics[1] + image_processing[1], 4) 

teacher_9 = salary_of_employees(optimization_methods_2[0] + optimization_methods_3[0], 
                                Mathematical_logic_and_theory_of_algorithms[1] + optimization_methods_2[1] + 
                                optimization_methods_3[1], 4)

teacher_10 = salary_of_employees(database_technologies[0] + os[0] + iot_technologies[0], 
                                 database_technologies[1] + os[1] + iot_technologies[1], 4)
                                
teacher_11 = salary_of_employees(parallel_programming[0] + internet_technologies[0] + computer_networks[0], 
                                 computer_networks[1] + parallel_programming[1] + internet_technologies[1], 4)

teacher_12 = salary_of_employees(requirements_development_and_analysis[0] + telecommunication_systems_management[0] +
                                 introduction_to_software_engineering[0],
                                 requirements_development_and_analysis[1] + telecommunication_systems_management[1], 4)

teacher_13 = salary_of_employees(numerical_methods[0], numerical_methods[1], 4)
teacher_14 = salary_of_employees(prof_cpp[0] + software_testing[0] + programming_tools[0], 
                                 prof_cpp[1] + software_testing[1], 4)

teacher_15 = salary_of_employees(dev_java_network_app[0] + mobile_systems_programming[0] + big_data_engineering[0],
                                 dev_java_network_app[1] + mobile_systems_programming[1] + big_data_engineering[1], 4)

teacher_16 = salary_of_employees(familiarization_practice_3[0] + technological_practice[0], 0, 4)
teacher_17 = salary_of_employees(physics[0], physics[1], 8)

teacher_18 = salary_of_employees(theory_of_automata_and_formal_languages[0] + economics_of_software_engineering[0] +
                                 socio_ethical_issues_of_information_technology[0], theory_of_automata_and_formal_languages[1] + economics_of_software_engineering[0] +
                                 socio_ethical_issues_of_information_technology[1] + economics_of_software_engineering[1], 4)

teacher_19 = salary_of_employees(information_tеchnology_security_fundamentals[0] + operations_research[0] +
                                 systems_theory_and_systems_analysis[0], operations_research[1], 4)

teacher_20 = salary_of_employees(software_project_management[0] + distributed_processing_technology[0] + cloud_computing[0],
                                 software_project_management[1] + distributed_processing_technology[1] + cloud_computing[1], 4)

teacher_21 = salary_of_employees(research_work_4[0] + undergraduate_practice[0], 0, 4)
teacher_22 = salary_of_employees(fundamentals_of_computer_vision[0] + programming_on_new_architectures[0] + 
                                 design_and_architecture_of_software_systems[0],
                                 fundamentals_of_computer_vision[1] + programming_on_new_architectures[1] +
                                 design_and_architecture_of_software_systems[1], 4)

#Преподаватели магистратуры
teacher_24 = salary_of_employees(legal_and_economic_aspects_of_it[0] + it_company_economic_statistics[0],
                                 legal_and_economic_aspects_of_it[1] + it_company_economic_statistics[1], 2)

teacher_25 = salary_of_employees(modern_databases[0] + it_project_management[0], 
                                 modern_databases[1] + decision_choice_models[1], 2)

teacher_26 = salary_of_employees(analysis_and_software_design[0] + requirements_analysis[0] + parallel_numerical_methods[0],
                                 analysis_and_software_design[1] + requirements_analysis[1] + parallel_numerical_methods[1], 2)

teacher_27 = salary_of_employees(software_design_patterns[0] + modern_computer_graphics[0] + iot[0],
                                 software_design_patterns[1] + modern_computer_graphics[1] + iot[1], 2)

teacher_28 = salary_of_employees(big_data[0] + performance_analysis_and_software_optimization[0] + research_work_5[0],
                                 big_data[1] + performance_analysis_and_software_optimization[1], 2)

teacher_29 = salary_of_employees(programming_in_scripting_languages[0] + fundamentals_of_robotics[0] + familiarization_practice_5[0],
                                 programming_in_scripting_languages[1] + fundamentals_of_robotics[1], 2)

def taxes (zp):
    return zp - (zp * 0.13)
x = [taxes(teacher_1), taxes(teacher_2), taxes(teacher_3), taxes(teacher_4), taxes(teacher_5), taxes(teacher_6), 
     taxes(teacher_7), taxes(teacher_8), taxes(teacher_9), taxes(teacher_10), taxes(teacher_11), taxes(teacher_12),
     taxes(teacher_13), taxes(teacher_14), taxes(teacher_15), taxes(teacher_16), taxes(teacher_17), taxes(teacher_18), 
     taxes(teacher_19), taxes(teacher_20), taxes(teacher_21), taxes(teacher_22), taxes(teacher_24), 
     taxes(teacher_25), taxes(teacher_26), taxes(teacher_27), taxes(teacher_28), taxes(teacher_29)]


print("ЗП преподавателей:")
plt.plot(x)
plt.show()
#ЗП преподавателей:

#Расчет общих затрат в год при очном обучении

total_costs_offline = c1_year + internet_year + communal_expenses + chancellery + siz + technology_update + (methodist_1*12) + \
        (methodist_2 * 12) + (accountant_1 * 12) + (accountant_2 * 12) + (system_administrator * 12) + (сleaner * 12) + \
        (cloakroom_attendant * 12)

print ("Затраты в год при очном обучении: ", total_costs_offline)

total_coast_offline_std = total_costs_offline / ((bachelor_groups + graduate_groups) * number_of_students)
print("Распределение общих затрат на всех студентов: ", total_coast_offline_std)
#Расчет общих затрат в год при очном обучении
total_coast_online = c1_year + internet_year + (methodist_1 * 12) + \
        (methodist_2 * 12) + (accountant_1 * 12) + (accountant_2 * 12) + (system_administrator * 12)

print ("Затраты в год при дистанционном обучении: ", total_coast_online)

total_coast_online_std = total_coast_online / ((bachelor_groups + graduate_groups) * number_of_students)
print("Распределение общих затрат на всех студентов: ", total_coast_online_std)
#Затраты на выплаты ЗП преподавателем бакалавриата (включая налоги)
costs_of_salary_bachelor = (teacher_1 + teacher_2 + teacher_3 + teacher_4 + teacher_5 + teacher_6 + teacher_7 + teacher_8 + \
                        teacher_9 + teacher_10 + teacher_11 + teacher_12 + teacher_13 + teacher_14 + teacher_15 + \
                        teacher_16 + teacher_17 + teacher_18 + teacher_19 + teacher_20 + teacher_21 + teacher_22) * 12

print("Затраты на выплаты ЗП преподавателем бакалавриата: ", costs_of_salary_bachelor)

costs_of_salary_bachelor_std = costs_of_salary_bachelor / (bachelor_groups * number_of_students)
print("Распределение на студентов бакалавриата: ", costs_of_salary_bachelor_std)
#Затраты на выплаты ЗП преподавателем магистратуры (включая налоги)
costs_of_salary_of_magistracy = (teacher_24 + teacher_25 + teacher_26 + teacher_27 + teacher_28 + teacher_29) * 12

print("Затраты на выплаты ЗП преподавателем магистратуры: ", costs_of_salary_of_magistracy)

costs_of_salary_of_magistracy_std = costs_of_salary_of_magistracy / (graduate_groups * number_of_students)
print("Распределение на студентов магистратуры: ", costs_of_salary_of_magistracy_std)
#Распределение суммартных затрат на студента очного обучения (бакалавриат) 
bak = total_coast_offline_std + costs_of_salary_bachelor_std
print("Распределение суммартных затрат на студента очного обучения (бакалавриат, учебный год): ", bak)
#Распределение суммартных затрат на студента очного обучения (магистратура) 
mag = total_coast_offline_std + costs_of_salary_of_magistracy_std
print("Распределение суммартных затрат на студента очного обучения (магистратура, учебный год): ", mag)
#Распределение суммартных затрат на студента дистанционного обучения (бакалавриат) 
bak_online = total_coast_online_std + costs_of_salary_bachelor_std
print("Распределение суммартных затрат на студента дистанционного обучения (бакалавриат, учебный год): ", bak_online)
#Распределение суммартных затрат на студента очного обучения (магистратура) 
mag_online = total_coast_online_std + costs_of_salary_of_magistracy_std
print("Распределение суммартных затрат на студента очного обучения (магистратура, учебный год): ", mag_online)
print("Сравнение цен очного и дистанционного обучения в год")
x = [1, 3, 5, 7]
z1 = [bak, bak_online, mag, mag_online]

plt.bar(x, z1)

#Цена за полное обучение с учетом инфляции (7%)

bak_online_1 = bak_online                                 #1 год
bak_online_2 = bak_online_1 + (bak_online_1 * 0.07)       #2 год
bak_online_3 = bak_online_2 + (bak_online_2 * 0.07)       #3 год
bak_online_4 = bak_online_3 + (bak_online_3 * 0.07)       #4 год
mag_online_5 = mag_online                                 #5 год

bak_offline_1 = bak
bak_offline_2 = bak_offline_1 + (bak_offline_1 * 0.07)
bak_offline_3 = bak_offline_2 + (bak_offline_2 * 0.07)
bak_offline_4 = bak_offline_3 + (bak_offline_3 * 0.07)

mag_offline_5 = mag
#Изменение цены обучения из-за инфляции
print("Изменение цены обучения из-за инфляции \n")

x = [bak_online_1, bak_online_2, bak_online_3, bak_online_4]
print("Бакалавриат в дистанционном формате:")
plt.plot(x)
plt.show()

x = [bak_offline_1, bak_offline_2, bak_offline_3, bak_offline_4]
print("Бакалавриат в очном формате:")
plt.plot(x)
plt.show()