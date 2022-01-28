def is_criticality_balanced(temeprature: int, neutrons_emitted: int) -> bool:
    """
    Returns True is criticality is balanced
    Criticality is balanced if 
    :param temperature: is less than 800; and
    :param neutrons_emitted: is greater than 500; and
    the product of both parameters is less than 500000
    """
    temeprature < 800 and neutrons_emitted > 500 and temeprature*neutrons_emitted < 500000
