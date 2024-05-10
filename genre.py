
"""
Este código implementa una clase enum llamada GENRE que se utiliza para almacenar el género de una canción. 
La clase enum define cuatro posibles valores para los géneros de las canciones: ROCK, POP, EDM y COUNTRY. 
Además, se proporciona una función principal (main) para probar la clase GENRE mediante casos de prueba.

La clase GENRE proporciona una forma eficiente de manejar los géneros de las canciones, ya que garantiza que 
solo se puedan usar valores específicos predefinidos (ROCK, POP, EDM, COUNTRY).

Los casos de prueba en la función main comprueban si los valores de los géneros (ROCK, POP, EDM, COUNTRY) 
se han definido correctamente como instancias de la clase GENRE. Si todas las comprobaciones son exitosas, 
se imprime "Test PASS" para cada género, de lo contrario, se imprime "Test FAIL".

Este código es una parte esencial del sistema, ya que proporciona una base sólida para clasificar las canciones 
según su género y garantiza la integridad de los datos relacionados con los géneros de las canciones.
"""
# Source packages.
from enum import Enum

class GENRE(Enum):
    """
    Class GENRE.

    This class is used to store the genre of a song.

    Syntax
    ------
        genre = GENRE()

    Parameters
    ----------
        Null .
    
    Returns
    -------
        The new genre.
    
    Example
    -------
        genre = GENRE()
    """

    ROCK = 1
    POP = 2
    EDM = 3
    COUNTRY = 4



def main():
    """Function main of the module.

    The function main of this module is used to test the Class GENRE.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Check Class GENRE - Name.")
    print("=================================================================.")

    if isinstance(GENRE.ROCK, GENRE):
        print("Test PASS. The enum for ROCK has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.POP, GENRE):
        print("Test PASS. The enum for POP has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.EDM, GENRE):
        print("Test PASS. The enum for EDM has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.COUNTRY, GENRE):
        print("Test PASS. The enum for COUNTRY has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
