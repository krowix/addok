from pathlib import Path

DB_SETTINGS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

# Max number of results to be retrieved from db and scored.
BUCKET_LIMIT = 100

# Above this treshold, terms are considered commons.
COMMON_THRESHOLD = 10000

RESOURCES_ROOT = Path(__file__).parent.parent.parent.joinpath('resources')
SYNONYMS_PATH = 'synonyms.txt'

# Pipeline stream to be used.
PIPELINE = [
    'addok.textutils.default.pipeline.tokenize',
    'addok.textutils.default.pipeline.normalize',
    'addok.textutils.default.pipeline.synonymize',
    'addok.textutils.fr.stemmize',
]
