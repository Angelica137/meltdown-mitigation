def is_criticality_balanced(temep: int, neutrons_emitted: int) -> bool:
    """
    Returns True if criticality is balanced
    """
    return temep < 800 and neutrons_emitted > 500 and temep*neutrons_emitted < 500000


def reactor_efficiency(voltage: int, current: int, max_power: int) -> str:
    """
    Returns traffic light indicator or efficiency
    Efficincy is measured as a percent and is caluclated
    (voltage * current/theoretical_max_power)*100
    """
    efficiency = (voltage*current/max_power)*100
    if efficiency < 60:
        return 'red'
    if efficiency < 80:
        return 'orange'
    if efficiency > 80:
        return 'green'
