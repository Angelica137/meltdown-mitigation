def is_criticality_balanced(temp: int, neutrons_emitted: int) -> bool:
    """
    Returns True if criticality is balanced
    """
    return temep < 800 and neutrons_emitted > 500 and temp*neutrons_emitted < 500000


def reactor_efficiency(voltage: int, current: int, max_power: int) -> str:
    """
    Returns traffic light indicator or efficiency
    Efficincy is measured as a percent and is caluclated
    (voltage * current/theoretical_max_power)*100
    """
    efficiency = (voltage*current/max_power)*100  # O(n^2)
    if efficiency < 30:    # O(1)
        return 'black'
    if efficiency < 60:
        return 'red'
    if efficiency < 80:
        return 'orange'
    return 'green'


def fail_safe(temp: int, neutrons_produced: int, threshold: int) -> str:
    """
    Determins if reactor is at, below or above the ideal criticalicty threshold
    """
    if threshold*0.1 <= temp*neutrons_produced <= threshold*0.1:
        return 'NORMAL'
    if temp*neutrons_produced < threshold*0.9:
        return 'LOW'
    if temp*neutrons_produced > threshold*0.9:
        return 'DANGER'
