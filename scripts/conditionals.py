def is_criticality_balanced(temep: int, neutrons_emitted: int) -> bool:
    """
    Returns True is criticality is balanced
    Criticality is balanced if 
    :param temperature: is less than 800; and
    :param neutrons_emitted: is greater than 500; and
    the product of both parameters is less than 500000
    """
    temep < 800 and neutrons_emitted > 500 and temep*neutrons_emitted < 500000
