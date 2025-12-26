class min_wordFilter:
    def __init__(self, text, min_len):
        self.word = text.split()
        self.min_len = min_len
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <  len(self.word):
            current_word = self.word[self.index]
            self.index += 1
            if len(current_word) >= self.min_len:
                return current_word
        raise StopIteration 
    
class max_wordFilter:
    def __init__(self, text, max_len):
        self.word = text.split()
        self.max_len = max_len
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index <  len(self.word):
            current_word = self.word[self.index]
            self.index += 1
            if len(current_word ) <= self.max_len:
                return current_word 
        raise StopIteration
    

    
