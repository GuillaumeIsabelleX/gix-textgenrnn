from textgenrnn import textgenrnn

textgen.train_from_file('akten-2016.txt', num_epochs=1)
textgen.generate()

