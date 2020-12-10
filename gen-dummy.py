from textgenrnn import textgenrnn


textgen = textgenrnn('weights/hacker_news.hdf5')
textgen.generate(3, temperature=1.0)
