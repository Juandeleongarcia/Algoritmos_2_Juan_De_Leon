"""
Este código implementa una clase Song que representa una canción con los siguientes atributos: id, name, artist, duration, release_date y genres.
El constructor de la clase Song verifica el tipo y el valor de cada parámetro y lanza excepciones si no se cumplen los requisitos.

La clase Song también proporciona métodos getters y setters para acceder y modificar los atributos de la canción, así como métodos para agregar un género a la canción, 
comparar dos canciones basadas en su identificador único y representar una canción como una cadena de caracteres.

Se proporcionan casos de prueba en la función main para verificar el correcto funcionamiento de la clase Song. 
Estos casos de prueba prueban la creación de una canción, la obtención de sus atributos, la adición de un género, la comparación de canciones y la representación 
de la canción como una cadena de caracteres.

Este código es esencial para la gestión de canciones en la aplicación, ya que proporciona una forma de almacenar, manipular y representar información sobre las canciones.
"""
# Importar los módulos necesarios para la ejecución del programa.
from enum import Enum
from datetime import date

class Genre(Enum):
    ROCK = 1
    POP = 2
    EDM = 3
    COUNTRY = 4

class Song():
    """Constructor of the class.

    The constructor of the class Song is used to create a new song.

    Syntax
    ------
      song = Song(id, name, artist, duration, release_date, genres)

    Parameters
    ----------
      id : int
        The unique identifier of the song.
      name : str
        The name of the song.
      artist : str
        The artist of the song.
      duration : int
        The duration of the song in seconds.
      release_date : date
        The release date of the song.
      genres : list
        The genres of the song.

    Returns
    -------
      The new song.

    Example
    -------
      song = Song(1, "calorro", "estopa", 189, date.today(), [Genre.POP])
    """
     ## Constructor de la clase Song
    def __init__(self, id, name, artist, duration, release_date, genres):
        ## Verificar el tipo y valor de cada parámetro y lanzar excepciones si no se cumplen los requisitos
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID must be a non-negative integer.")
        self.id = id

        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        self.name = name

        if not isinstance(artist, str) or not artist:
            raise ValueError("Artist must be a non-empty string.")
        self.artist = artist

        if not isinstance(duration, int) or duration <= 10:
            raise ValueError("Duration must be an integer greater than 10.")
        self.duration = duration

        if not isinstance(release_date, date) or release_date > date.today():
            raise ValueError("Release date must be a valid date in the past.")
        self.release_date = release_date

        if not isinstance(genres, list):
            raise ValueError("Genres must be provided as a list.")
        for genre in genres:
            if not isinstance(genre, Genre):
                raise ValueError("Genres must be instances of Genre.")
        self.genres = genres

    ## Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def get_release_date(self):
        return self.release_date

    def get_genres(self):
        return self.genres

    ## Método para agregar un género a la canción
    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    ## Método para verificar si dos canciones son iguales basadas en el identificador único
    def __eq__(self, other):
        return isinstance(other, Song) and self.id == other.id

    ## Método para representar la canción como una cadena de caracteres
    def __str__(self):
        return f"{self.artist} tocando {self.name} durante {self.duration} segundos."



def main():
    """Function main of the module.

    The function main of this module is used to test the Class Song.

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
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [Genre.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [Genre.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [Genre.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))

    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(Genre.ROCK)
    genres = song2.get_genres()
    if genres == [Genre.POP, Genre.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [Genre.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
  

# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()