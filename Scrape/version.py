import importlib.metadata


try:
	__version__ = importlib.metadata.version('scrape')
except importlib.metadata.PackageNotFoundError:
	__version__ = None
