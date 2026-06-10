def most_frequent_word_optimized(sentence):
    words = sentence.lower().split()
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1 # A cleaner way to build the dict
        
    # Use max() on the dictionary keys, looking at their values (counts) to find the max
    return max(word_counts, key=word_counts.get)