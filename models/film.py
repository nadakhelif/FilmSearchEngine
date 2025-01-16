from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Film:
    title: Optional[str] = None
    year: Optional[int] = None
    runtimeMinutes: Optional[int] = None
    overview: Optional[str] = None
    language: Optional[str] = None
    release_date: Optional[str] = None
    keywords: Optional[List[str]] = None
    synopsis: Optional[str] = None
    worldwide_gross: Optional[int] = None
    distributor: Optional[str] = None
    mpaa: Optional[str] = None
    budget: Optional[str] = None
    genres: Optional[List[str]] = None
    actors: Optional[List[str]] = None
    total_actor_tenure: Optional[float] = None
    avg_actor_tenure: Optional[float] = None
    director: Optional[str] = None  # Director is optional and defaults to None
    plot: Optional[str] = None 
    cast: Optional[List[str]] = None
    reviews: Optional[List[str]] = None

    def to_text(self) -> str:
        """Convert film data to indexable text."""
        return f"""
        Title: {self.title if self.title else 'Not Available'}
        Year: {self.year if self.year else 'Not Available'}
        Runtime: {self.runtimeMinutes if self.runtimeMinutes else 'Not Available'} minutes
        Language: {self.language if self.language else 'Not Available'}
        Release Date: {self.release_date if self.release_date else 'Not Available'}
        
        Overview:
        {self.overview if self.overview else 'Not Available'}
        
        Synopsis:
        {self.synopsis if self.synopsis else 'Not Available'}
        
        Keywords:
        {', '.join(self.keywords) if self.keywords else 'Not Available'}
        
        Genres:
        {', '.join(self.genres) if self.genres else 'Not Available'}
        
        Actors:
        {', '.join(self.actors) if self.actors else 'Not Available'}
        
        Distributor: {self.distributor if self.distributor else 'Not Available'}
        MPAA: {self.mpaa if self.mpaa else 'Not Available'}
        Budget: {self.budget if self.budget else 'Not Available'}
        Worldwide Gross: {self.worldwide_gross if self.worldwide_gross else 'Not Available'}
        Total Actor Tenure: {self.total_actor_tenure if self.total_actor_tenure else 'Not Available'}
        Average Actor Tenure: {self.avg_actor_tenure if self.avg_actor_tenure else 'Not Available'}
        Director: {self.director if self.director else 'Not Available'}
        Plot: {self.plot if self.plot else 'Not Available'}
        Cast: {', '.join(self.cast) if self.cast else 'Not Available'}
        Reviews: {', '.join(self.reviews) if self.reviews else 'Not Available'}
        """
