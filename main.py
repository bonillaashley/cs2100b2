"""
TODO: A very useful temperature-conversion app.
"""

THRESHOLD_TEMP_F= 68 

def is_cold_f(temp_f: float) -> bool: 
    """determines if the supplied 
    temperature in F is below
    our agreed-upon temp
    
    parameters 
    ==========
    temp_f: float 
        supplied temperature in F 

    Returns 
    =======
    bool 
        True means below the 
        agreed upon threshold
    
    """
    
    
    return temp_f < THRESHOLD_TEMP_F 

def greet_person()-> None: 
     """gets the name of a person
       from the keyboard
       and greets them 
     """      

    your_name: str = input("what is your name? ")
    print(f"howdy, {your_name}")


def main() -> None:
    pass
if __ name__== "__main__": 
    main ()
