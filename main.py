import sys
from inventory import demo_inventory, get_all_equipment

def show_menu():
    print("\n" + "="*50)
    print(" СИСТЕМА УЧЁТА ИНВЕНТАРЯ КОМПЬЮТЕРНЫХ КЛАССОВ ")
    print("="*50)
    print("1. Показать всё оборудование")
    print("2. Добавить новое оборудование (Спринт 2)")
    print("3. Поиск оборудования (Спринт 2)")
    print("4. Перемещение оборудования (Спринт 3)")
    print("5. Изменение статуса оборудования (Спринт 3)")
    print("6. Удаление оборудования (Спринт 3)")
    print("0. Выход из программы")
    print("="*50)

def display_equipment_table(data):
    """Вывод оборудования в текстовом виде (CLI таблица)"""
    if data is None:
        print("\n[Уведомление]: База данных оборудования пуста.")
        return

    header = f"{'Инв. №':<10} | {'Тип':<10} | {'Наименование':<20} | {'Кабинет':<8} | {'Статус':<17} | {'Ответственный':<15}"
    print("\n" + header)
    print("-" * len(header))
    
    for item in data:
        print(f"{item['inv_number']:<10} | {item['type']:<10} | {item['name']:<20} | {item['cabinet']:<8} | {item['status']:<17} | {item['responsible']:<15}")

def main():
    current_inventory = demo_inventory

    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            equipment = get_all_equipment(current_inventory)
            display_equipment_table(equipment)
        elif choice in ["2", "3", "4", "5", "6"]:
            print(f"\n[Инфо]: Этот компонент находится в разработке согласно плану спринтов.")
            input("Нажмите Enter, чтобы вернуться в меню...")
        elif choice == "0":
            print("\nПрограмма завершена.")
            sys.exit()
        else:
            print("\n[Ошибка]: Неверный пункт меню. Выберите от 0 до 6.")
            input("Нажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()
