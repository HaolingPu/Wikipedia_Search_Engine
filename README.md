# Wikipedia Search Engine

A scalable search engine similar to Google or Bing 🔥

## 🎯 Project Overview

This project implements a full-stack search engine that indexes and searches through Wikipedia pages. It demonstrates core information retrieval concepts including tf-idf scoring, PageRank integration, and parallel data processing with MapReduce.

## ✨ Features

- **Scalable Indexing**: MapReduce pipeline for processing large document collections
- **Intelligent Ranking**: Combines tf-idf and PageRank for relevant search results
- **Segmented Architecture**: Distributed inverted index across multiple servers
- **User-Adjustable Scoring**: Interactive slider for PageRank weight customization
- **Parallel Processing**: Concurrent REST API calls for fast query response
- **Clean Interface**: Google-like search interface with result summaries

## 🏗️ Architecture

The system consists of three main components:

### 1. Inverted Index Pipeline
- Processes Wikipedia HTML documents using MapReduce
- Extracts and cleans text content (removes stop words, normalizes case)
- Calculates tf-idf scores and document normalization factors
- Outputs segmented inverted index files

### 2. Index Server (REST API)
- Three Flask servers running on ports 9000-9002
- Each serves one segment of the inverted index
- Provides `/api/v1/hits/` endpoint for query processing
- Returns JSON with document IDs and relevance scores

### 3. Search Server (Web Interface)
- Flask web application on port 8000
- User-facing search interface
- Makes parallel requests to all Index servers
- Merges and ranks results from multiple segments
- Displays top 10 results with titles, URLs, and summaries

## 🔍 Search Algorithm

The ranking formula combines two factors:

```
Score(q, d, w) = w × PageRank(d) + (1-w) × cosSim(q, d)
```

Where:
- `w`: User-adjustable PageRank weight (0-1)
- `PageRank(d)`: Link-based importance score
- `cosSim(q, d)`: Cosine similarity between query and document tf-idf vectors

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Data Processing**: MapReduce (Michigan Hadoop - Madoop)
- **Database**: SQLite3
- **HTML Parsing**: BeautifulSoup4
- **HTTP Requests**: Requests library
- **Concurrency**: Python threading
- **Frontend**: HTML, CSS, Jinja2 templates

## 📁 Project Structure

```
p5-search-engine/
├── bin/
│   ├── index           # Index server control script
│   ├── search          # Search server control script
│   ├── searchdb        # Database generation script
│   └── install         # Installation script
├── inverted_index/
│   ├── map*.py         # MapReduce mapper programs
│   ├── reduce*.py      # MapReduce reducer programs
│   ├── partition.py    # Custom partitioner
│   └── pipeline.sh     # MapReduce pipeline orchestration
├── index_server/
│   └── index/
│       ├── api/        # REST API endpoints
│       └── inverted_index/  # Segmented index files
├── search_server/
│   └── search/
│       ├── views/      # Route handlers
│       ├── templates/  # HTML templates
│       └── static/     # CSS stylesheets
└── tests/              # Unit tests
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual environment support

### Installation

1. Clone the repository
```bash
git clone https://github.com/HaolingPu/Search_Engine.git
cd Search_Engine
```

2. Run the installation script
```bash
./bin/install
```

This will:
- Create a Python virtual environment
- Install all dependencies
- Set up both Index and Search server packages

### Building the Inverted Index

1. Unpack the Wikipedia crawl data
```bash
cd inverted_index
tar -xvJf crawl.tar.xz
```

2. Run the MapReduce pipeline
```bash
./pipeline.sh crawl
```

3. Copy output to Index server
```bash
cp output/part-00000 ../index_server/index/inverted_index/inverted_index_0.txt
cp output/part-00001 ../index_server/index/inverted_index/inverted_index_1.txt
cp output/part-00002 ../index_server/index/inverted_index/inverted_index_2.txt
```

### Initializing the Search Database

```bash
./bin/searchdb
```

This creates `var/search.sqlite3` with document metadata (titles, URLs, summaries).

### Running the Servers

1. Start the Index servers
```bash
./bin/index start
```

2. Start the Search server
```bash
./bin/search start
```

3. Open your browser to `http://localhost:8000`

### Managing Servers

```bash
# Check server status
./bin/index status
./bin/search status

# Stop servers
./bin/index stop
./bin/search stop

# Restart servers
./bin/index restart
./bin/search restart
```

## 🧪 Testing

Run all tests:
```bash
pytest -v
```

Run specific test suites:
```bash
pytest -v tests/test_pipeline_public.py
pytest -v tests/test_index_server_public.py
pytest -v tests/test_search_server_public.py
```

Style checks:
```bash
pytest -v tests/test_style.py
```

## 📊 Performance Characteristics

- **Index Size**: ~200MB for subset of Wikipedia
- **Query Response Time**: <500ms for typical queries
- **Concurrent Requests**: Parallel processing across 3 index segments
- **Scalability**: Architecture supports additional segments with minimal changes

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

- **Information Retrieval**: tf-idf, PageRank, cosine similarity
- **Distributed Systems**: Service-oriented architecture, REST APIs
- **Parallel Processing**: MapReduce paradigm, concurrent programming
- **Web Development**: Flask, dynamic pages, database integration
- **Software Engineering**: Testing, code quality, documentation

## 📝 Technical Highlights

### MapReduce Pipeline Design
- Multi-stage pipeline with up to 9 jobs
- Custom partitioning for document segmentation
- Efficient group-by operations using sort

### Index Server Optimization
- In-memory inverted index for fast lookups
- Pre-computed normalization factors
- Efficient data structures for tf-idf calculations

### Search Server Features
- Thread pool for parallel API requests
- Heap-based merging of sorted results
- Query string cleaning and normalization

## 🔒 Academic Integrity

This project was completed as part of EECS 485 at the University of Michigan. The code represents my own work and understanding of search engine concepts.

**Note**: If you are currently taking EECS 485, please adhere to the course's academic integrity policies. This repository is intended as a portfolio piece and learning reference.

## 📚 Resources

- [Project Specification](https://eecs485staff.github.io/p5-search-engine/)
- [MapReduce Tutorial](https://github.com/eecs485staff/madoop)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [BeautifulSoup Documentation](https://beautiful-soup-4.readthedocs.io/)

## 📧 Contact

Haoling Pu - [GitHub](https://github.com/HaolingPu)

---

**Built with 🔍 at the University of Michigan**
