from dataclasses import dataclass
from typing import List

@dataclass
class Film:
    title: str
    director: str
    year: int
    plot: str
    cast: List[str]
    genres: List[str]
    reviews: List[str]
    
    def to_text(self) -> str:
        """Convert film data to indexable text."""
        return f"""
        {self.title}
        Réalisé par {self.director}
        Année: {self.year}
        
        Synopsis:
        {self.plot}
        
        Casting:
        {', '.join(self.cast)}
        
        Genres:
        {', '.join(self.genres)}
        
        Critiques:
        {' '.join(self.reviews)}
        """