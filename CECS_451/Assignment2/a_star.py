import re
        

big_map = open("E:\\Code\\CECS_451\\Assignment2\\map.txt")

contents = big_map.read()
cities = {}
split = contents.splitlines()#each line is a part
for i in range(len(split)):#20
    temp_routes = {}
    dah = split[i].split('-')#splits the city name and the connecting cities
    t = dah[1].split(',')#splits the right side of the string
    for j in range(len(t)):
        counter = 0
        z = t[j].replace("(","").replace(")", "")
        alpha = re.compile("([a-zA-Z]+)([0-9]+)") 
        splitter = alpha.match(z).groups()
        temp_routes[splitter[counter]] = splitter[counter+1]
    cities[dah[0]] = temp_routes
########## Creates map dictionary ############################


distance = open("E:\\Code\\CECS_451\\Assignment2\\distances.txt")
contents = distance.read()
split = contents.splitlines()
path = {}
for i in range(len(split)):
    city = split[i].split('-')
    path[city[0]] = city[1]
############# creates distances dictionary #####################

def checkCity_exist(cities):
    if cities in path.keys():
        return True
    return False

def get_small(city, visited):
    #print("Visited list: ", visited)
    s = list(cities.get(city)) #gets the city names that are connected to prev city
    #print("list: ",s)
    neighbor_fn = []
    for i in range(len(s)):
        gn = int(cities[city][s[i]])      # s.index() | use to get min num
        hn = int (path.get(s[i]))
        fn = gn + hn
        neighbor_fn.append(fn)
    #print("Neighbors: ", neighbor_fn)
    mini = s[neighbor_fn.index(min(neighbor_fn))] #find the lowest num and gets index
    #print("min1: ", mini)
    if(mini in visited): #checks to see if this city has been visited before
        s.pop(neighbor_fn.index(min(neighbor_fn)))
        neighbor_fn.pop(neighbor_fn.index(min(neighbor_fn)))
        mini = s[neighbor_fn.index(min(neighbor_fn))]
    #print("min2: ", mini)
    return mini
########## function to calculate #################################

def a_star(start, end):
    visited = [] #visited these cities | closed
    looking = [] #lowest fn cities     | open
    looking.append(start)
    if(start == end):
        return start
    while len(looking) > 0:
        for i in range(len(looking)):
            next_pos = get_small(looking[i], visited)
            if (next_pos == end):
                popper = looking.pop()
                looking.append(next_pos)
                visited.append(popper)
                visited.append(next_pos)
                return visited #returns the list to traverse
            popper = looking.pop()
            looking.append(next_pos)
            visited.append(popper)
            # print("popped: ", popper)
            # print("looking: ", looking)
            #print("visited: ", visited)
    return visited
########### a star algo ###########################################


def get_nums(city):
    
    return 0

def search(route):
    total = 0
    for i in range(len(route)):
        first = cities.get(route[i])
        if(route[i] == "Bucharest"):
            #print("Total: ", total)
            return total
        pos = int(first[route[i+1]])
        total = total + pos
       # print("Pos: ", pos)
    return total

def main():
    keep_going = True
    end_tile = "Bucharest"
    user = input("Enter a City Name: ")
    while keep_going:
        if(checkCity_exist(user)):
            keep_going = False
        else:
            print("Invalid City name")
            user = input("Enter a City Name: ")
    aether = a_star(user, end_tile)
    #print(aether)
    total_num = search(aether)
    print("From city: ", user, "\nTo city: " , end_tile, "\nBest Route: ", end=" ")

    for i in range(len(aether)):
        if(i == len(aether)-1):
            print(aether[i])
        else:
            print(aether[i], end =" - ")
    print("Total distance: ",total_num)
main()



