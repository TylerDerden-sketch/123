demo_inventory = [
    {"inv_number": "INV-001", "type": "ПК", "name": "Asus ExpertCenter", "cabinet": "101", "status": "Исправно", "responsible": "Иванов И.И."},
    {"inv_number": "INV-002", "type": "Монитор", "name": "LG UltraFine 24", "cabinet": "101", "status": "Исправно", "responsible": "Иванов И.И."},
    {"inv_number": "INV-003", "type": "ПК", "name": "HP ProDesk", "cabinet": "102", "status": "Требует ремонта", "responsible": "Петров П.П."},
    {"inv_number": "INV-004", "type": "Принтер", "name": "HP LaserJet", "cabinet": "102", "status": "Исправно", "responsible": "Петров П.П."},
    {"inv_number": "INV-005", "type": "Монитор", "name": "Samsung Essential", "cabinet": "103", "status": "Списано", "responsible": "Сидоров С.С."}
]

def get_all_equipment(inventory_list):
    """Возвращает список всех устройств для вывода на экран."""
    if not inventory_list:
        return None
    return inventory_list
