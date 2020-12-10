from textgenrnn import textgenrnn


textgen = textgenrnn()

textgen.train_from_file('datasets/akten-2016.txt', num_epochs=1)
textgen.generate()



