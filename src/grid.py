import random

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg
    wall2 = "\033[36m■\033[0m"  # Tecken för vägg innanför spelplanen

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # H. Använd for-loopar för att skapa flera, sammanhängande väggar på kartan. Se till att det inte skapas några rum som man inte kan komma in i.
        """Skapa väggar innanför spelplanen"""
        """Skapar H formade väggar"""
        # vertikala väggar
        for i in range(1,int(self.height / 3)):
            self.set((int(self.width / 6) - 3), i, self.wall2)
            self.set((int(self.width / 6) + 3), i, self.wall2)
        # horizontal vägg
        for j in range(int(self.width / 3) - 7, self.width -28 ):
            self.set(j, int(self.height / 3) -2, self.wall2)

        """Skapar E formade väggar"""
        # vertikala väggar
        for i in range(int(self.height / 2) - 1, self.height - 4):
            self.set(10, i, self.wall2)
        # horisontala väggar
        for j in range(12, int(self.width / 2), 2):
            self.set(j, int(self.height / 2) - 1, self.wall2)
            self.set(j, self.height - 5, self.wall2)

        for j in range(13, int(self.width / 2)- 3 ):
            self.set(j, int(self.height / 2) , self.wall2)

        """Skapar J formade väggar"""
        # vertikal vägg (ett steg från höger vägg)
        for i in range(self.height - 6, self.height - 2):
            self.set(self.width - 4, i, self.wall2)

        # horisontell vägg längst ner (böjer åt vänster)
        for j in range(self.width - 10, self.width - 3, 2):
            self.set(j, self.height - 3, self.wall2)



    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty