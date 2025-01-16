"""Script to generate sample film data."""
import json
import os
import csv

SAMPLE_FILMS = [
    {
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "year": 1994,
        "plot": "Les destins de plusieurs personnages s'entremêlent dans une histoire non linéaire impliquant deux tueurs à gages philosophes, un boxeur, un gangster et sa femme.",
        "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis"],
        "genres": ["Crime", "Drame"],
        "reviews": [
            "Un chef-d'œuvre du cinéma moderne",
            "Révolutionnaire dans sa narration",
            "Dialogues mémorables"
        ]
    },
    {
        "title": "Amélie",
        "director": "Jean-Pierre Jeunet",
        "year": 2001,
        "plot": "Une jeune serveuse parisienne décide de changer la vie des gens qui l'entourent tout en découvrant l'amour.",
        "cast": ["Audrey Tautou", "Mathieu Kassovitz", "Rufus"],
        "genres": ["Comédie", "Romance"],
        "reviews": [
            "Une fable moderne enchanteresse",
            "Visuellement magnifique",
            "Performance inoubliable d'Audrey Tautou"
        ]
    },
    
    {
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "year": 2008,
        "plot": "Batman faces off against the Joker, a criminal mastermind who seeks to create chaos in Gotham City, while grappling with his own sense of justice.",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama"],
        "reviews": [
            "An intense, thought-provoking masterpiece.",
            "Heath Ledger's Joker is iconic.",
            "A film that transcends the superhero genre."
        ]
    },
    {
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "plot": "A thief who enters the dreams of others to steal secrets is given the chance to have his criminal record erased if he can successfully implant an idea into a target's subconscious.",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Tom Hardy"],
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "reviews": [
            "A mind-bending cinematic experience.",
            "Brilliant direction and concept by Christopher Nolan.",
            "The layers of dream within dream are intellectually stimulating."
        ]
    },
    {
        "title": "Titanic",
        "director": "James Cameron",
        "year": 1997,
        "plot": "The story of a young couple from different social backgrounds who fall in love aboard the doomed R.M.S. Titanic.",
        "cast": ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Danny Nucci"],
        "genres": ["Drama", "Romance"],
        "reviews": [
            "A timeless classic.",
            "The visuals of the sinking Titanic are breathtaking.",
            "A true epic blending historical tragedy with personal emotion."
        ]
    },
    {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994,
        "plot": "The story of a man wrongly convicted of murder who forms a close friendship with a fellow inmate, while maintaining his hope and will to escape.",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"],
        "reviews": [
            "One of the best films ever made.",
            "A deeply moving exploration of hope and friendship.",
            "Unforgettable performances from Robbins and Freeman."
        ]
    },
    {
        "title": "Avatar",
        "director": "James Cameron",
        "year": 2009,
        "plot": "On the lush alien world of Pandora, a paraplegic former soldier becomes part of an experiment where human consciousness is transferred to an avatar to interact with the native Na'vi.",
        "cast": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver", "Stephen Lang"],
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "reviews": [
            "Visually stunning and immersive.",
            "A great exploration of environmentalism and native cultures.",
            "The world of Pandora is beautifully brought to life."
        ]
    },
    {
        "title": "The Matrix",
        "director": "Lana Wachowski, Lilly Wachowski",
        "year": 1999,
        "plot": "A hacker discovers that the reality he lives in is a simulation controlled by intelligent machines that have enslaved humanity, and he joins a group of rebels to fight back.",
        "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving"],
        "genres": ["Action", "Sci-Fi"],
        "reviews": [
            "A groundbreaking film that explores the nature of reality.",
            "The bullet time sequences are iconic.",
            "A thought-provoking take on artificial intelligence and free will."
        ]
    },
    {
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972,
        "plot": "The story of the powerful Corleone family and the rise of Michael Corleone from reluctant outsider to ruthless head of the family.",
        "cast": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"],
        "reviews": [
            "A cinematic masterpiece.",
            "Marlon Brando's performance is legendary.",
            "A timeless film about family, loyalty, and betrayal."
        ]
    },

    {
        "title": "batman batman",
        "director": "joker joker joker",
        "year": 1972,
        "plot": "The story of the powerful Corleone family and the rise of Michael Corleone from reluctant outsider to ruthless head of the family.",
        "cast": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"],
        "reviews": [
            "A cinematic masterpiece.",
            "Marlon Brando's performance is legendary.",
            "A timeless film about family, loyalty, and betrayal."
        ]
    },
    
    {
        "title": "batman batman",
        "director": "nada",
        "year": 1972,
        "plot": "The story of the batman powerful Corleone family batman and the rise of Michael Corleone from reluctant outsider to ruthless head of the family.",
        "cast": ["Marlon Brando", "Al Pacino", "James Caan", "batman Keaton"],
        "genres": ["Crime", "Drama"],
        "reviews": [
            "A cinematic masterpiece.",
            "Marlon Brando's performance is batman.",
            "A timeless film about family, loyalty, and batman."
        ]
    }
]

def create_sample_data(data_dir: str):
    """Create sample film data files."""
    os.makedirs(data_dir, exist_ok=True)
    
    for i, film in enumerate(SAMPLE_FILMS):
        filename = f"film_{i+1}.json"
        filepath = os.path.join(data_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(film, f, ensure_ascii=False, indent=2)


def create_film_files_from_tsv(tsv_filepath: str, output_dir: str):
    """
    Create JSON film description files based on a TSV file input.
    
    Args:
        tsv_filepath (str): Path to the input TSV file.
        output_dir (str): Directory where JSON files will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    with open(tsv_filepath, 'r', encoding='utf-8') as tsv_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in reader:
            # Extract film details
            title = row['primaryTitle']
            film_data = {
                "title": title,
                "year": int(row['startYear']) if row['startYear'].isdigit() else None,
                "runtimeMinutes": int(row['runtimeMinutes']) if row['runtimeMinutes'].isdigit() else None,
                "overview": row.get('overview', ''),
                "language": row.get('original_language', ''),
                "release_date": row.get('release_date', ''),
                "keywords": row.get('keywords', '').split(',') if row.get('keywords') else [],
                "synopsis": row.get('synopsis', ''),
                "worldwide_gross": int(row['worldwide']) if row['worldwide'].isdigit() else None,
                "distributor": row.get('distributor', ''),
                "mpaa": row.get('mpaa', ''),
                "budget": row.get('budget', ''),
                "genres": row.get('genres', '').split(',') if row.get('genres') else [],
                "actors": row.get('actors', '').split(',') if row.get('actors') else [],
                "total_actor_tenure": float(row['total_actor_tenure']) if row['total_actor_tenure'] else None,
                "avg_actor_tenure": float(row['avg_actor_tenure']) if row['avg_actor_tenure'] else None
            }
            
            # Generate filename (sanitize title for filesystem compatibility)
            sanitized_title = "".join(c if c.isalnum() or c in " -_" else "_" for c in title)
            filename = f"{sanitized_title}.json"
            filepath = os.path.join(output_dir, filename)
            
            # Write JSON file
            with open(filepath, 'w', encoding='utf-8') as json_file:
                json.dump(film_data, json_file, ensure_ascii=False, indent=2)

# Example usage
tsv_filepath = "filtered_final_movies_3.tsv"  # Path to your TSV file