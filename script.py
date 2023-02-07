def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'name' : 'gautam singh',
        'id' : '10285896',
        'toppings' : [
                        'SAUSAGE',
                        'PEPPERONI',
                        'PINEAPPLE'

        ],
        'movies' : [ 
             {
                'title' : 'mr. and mrs. 420',
                'genre' : 'comedy'

             },
             
             {
                'title' : 'incidious',
                'genre' : 'horror'
                
             }
                
    
        ]
    }


    about_me['movies'].append({'The Lord of the Rings', 'conjuring'})
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('bacon', 'hot pepper'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    return
# TODO: Step 3 - Add another movie to the data structure
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):

    student_name = about_me['name'].title()
    student_id = about_me['id'].capitalize()
    print(f"\nMy name is {student_name}, but you can call me MR.{about_me['name'].split()[0]}.")
    print(f'My student ID is {student_id}.')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    
    about_me['toppings'].extend(toppings)
    about_me['toppings'].sort()
    for i, p in enumerate(about_me['toppings']):
      about_me['toppings'][i] = p.capitalize()  
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    
      print(f'\nMy favourite pizza toppings are:')
      for t in about_me['toppings']:
        print(f'-{t.capitalize()}')
        return
    
# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print(f"I like to watch ", end='') 
    for i, movies in enumerate(about_me['movies']):

        title = [m['title'] for m in about_me['movies']]  
        print(', '.join(title), end='.\n')     
        return

    

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()
