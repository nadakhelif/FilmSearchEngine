# SearchEngine

A powerful and flexible search engine for querying film data with support for two distinct search types: Boolean Search and Vectorial Search.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Search Types](#search-types)
  - [Boolean Search](#boolean-search)
  - [Vectorial Search](#vectorial-search)
- [Usage](#usage)
- [Installation](#installation)


## Overview
This project implements a search engine that allows users to query a dataset of films using two search strategies:
- **Boolean Search**: Uses logical operators (AND, OR, NOT) to combine keywords and perform set-based filtering.
- **Vectorial Search**: Uses the vector space model and cosine similarity to rank films based on their relevance to a query.

## Features
- **Boolean Search**: Allows users to search using logical operators like `AND`, `OR`, and `NOT` to combine multiple terms and refine the results.
- **Vectorial Search**: Calculates similarity between documents and the query using the vector space model, returning ranked results.
- **Customizable Search Interface**: Implemented with a clean and simple GUI using PyQt5, where users can choose between Boolean or Vectorial search types.

## Search Types

### Boolean Search

The **Boolean Search** method allows users to perform queries using logical operators: `AND`, `OR`, and `NOT`. This search type processes the query as a set of documents containing the specified terms and applies logical operators to refine the results.

#### Example Queries:
- **`batman AND joker`**: Returns films that contain both "batman" and "joker".
- **`batman OR joker`**: Returns films that contain either "batman" or "joker".
- **`batman NOT joker`**: Returns films that contain "batman" but **not** "joker".

Parentheses can also be used to group terms and control the order of operations:
- **`(batman OR joker) AND superhero`**: Returns films that contain either "batman" or "joker" **and** also contain "superhero".

### Vectorial Search

The **Vectorial Search** method uses the **vector space model** to represent both the query and the documents as vectors in a multi-dimensional space. It calculates the **cosine similarity** between the query vector and the document vectors to rank documents based on their relevance to the query.

This approach is more flexible than Boolean search and is better suited for retrieving the most relevant results based on the context of the search terms.

#### Example:
- **Query**: `"batman joker superhero"`
- The engine calculates how close each document is to the query in terms of cosine similarity, and returns the most relevant films, ranked by score.

## Usage

To perform a search:
1. Enter a search query in the input field.
2. Choose a search type (`Boolean` or `Vectorial`) from the dropdown.
3. Press **"Rechercher"** to get the results.

The results will be displayed in a list with the film titles and their associated relevance score (for vectorial search).


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SearchEngine.git
   cd SearchEngine
   pip install -r requirements.txt 
   
2. Run the application:
   ```bash
    python app.py



