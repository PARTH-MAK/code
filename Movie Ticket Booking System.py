from collections import deque

# Class to represent a Movie
class Movie:
    def __init__(self, title, available_tickets):
        self.title = title
        self.available_tickets = available_tickets

# Movie Ticket Booking System using OOP and DSA
class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = []  # List of movies
        self.booked_tickets = []  # Stack for booked tickets (LIFO)
        self.request_queue = deque()  # Queue for customer requests (FIFO)

    # Function to add a movie to the system
    def add_movie(self, title, available_tickets):
        self.movies.append(Movie(title, available_tickets))
        print(f"Movie '{title}' added with {available_tickets} tickets.")

    # Function to book a ticket for a given movie
    def book_ticket(self, movie_title):
        movie = self.search_movie(movie_title)
        if movie:
            if movie.available_tickets > 0:
                movie.available_tickets -= 1
                self.booked_tickets.append(movie_title)
                print(f"Ticket booked for {movie_title}.")
            else:
                print(f"No tickets available for {movie_title}.")
        else:
            print(f"Movie {movie_title} not found.")

    # Function to cancel the last booked ticket (LIFO)
    def cancel_ticket(self):
        if self.booked_tickets:
            movie_title = self.booked_tickets.pop()
            movie = self.search_movie(movie_title)
            if movie:
                movie.available_tickets += 1
                print(f"Ticket for {movie_title} canceled.")
        else:
            print("No tickets to cancel.")

    # Add a ticket request to the queue (FIFO)
    def request_ticket(self, movie_title):
        self.request_queue.append(movie_title)
        print(f"Request for {movie_title} added to the queue.")

    # Process requests in FIFO order
    def process_requests(self):
        while self.request_queue:
            movie_title = self.request_queue.popleft()
            self.book_ticket(movie_title)

    # Binary search for a movie by title (more efficient than linear search)
    def search_movie(self, title):
        # Ensure the movies are sorted by title for binary search
        self.sort_movies()
        left, right = 0, len(self.movies) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.movies[mid].title.lower() == title.lower():
                return self.movies[mid]
            elif self.movies[mid].title.lower() < title.lower():
                left = mid + 1
            else:
                right = mid - 1
        return None

    # Sort movies by title (uses DSA sorting algorithm)
    def sort_movies(self):
        self.movies.sort(key=lambda x: x.title)

    # Display all movies and their available tickets
    def display_movies(self):
        print("Available Movies:")
        for movie in self.movies:
            print(f"{movie.title} - Tickets Available: {movie.available_tickets}")

# User interaction function for the Movie Ticket Booking System
def user_interaction():
    system = MovieTicketBookingSystem()

    # Predefined movies added to the system
    system.add_movie("Avengers", 5)
    system.add_movie("Inception", 3)
    system.add_movie("Titanic", 0)

    while True:
        print("\nMovie Ticket Booking System")
        print("1. Display all movies")
        print("2. Book a ticket")
        print("3. Cancel last booked ticket")
        print("4. Add a ticket request")
        print("5. Process all requests")
        print("6. Search for a movie")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.display_movies()

        elif choice == "2":
            movie_title = input("Enter movie title to book: ")
            system.book_ticket(movie_title)

        elif choice == "3":
            system.cancel_ticket()

        elif choice == "4":
            movie_title = input("Enter movie title to request a ticket: ")
            system.request_ticket(movie_title)

        elif choice == "5":
            system.process_requests()

        elif choice == "6":
            movie_title = input("Enter movie title to search: ")
            movie = system.search_movie(movie_title)
            if movie:
                print(f"Found movie: {movie.title} - Tickets Available: {movie.available_tickets}")
            else:
                print("Movie not found.")

        elif choice == "7":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the user interaction function
if __name__ == "__main__":
    user_interaction()
