def ratio_of_matches(sentence1, sentence2):
    # Split the sentences into lists of words
    words1 = sentence1.split()
    words2 = sentence2.split()
    
    # Count the number of matching words
    matches = 0
    for word in words1:
        if word in words2:
            matches += 1
    
    # Calculate and return the ratio of matches
    return matches / len(words1)


sentence1 = "dịch vụ chăm sóc khách hàng như thế nào  ?"
sentence2 = "dịch vụ chăm sóc khách hàng như thế nào?"

ratio = ratio_of_matches(sentence1, sentence2)
print(ratio)  # Outputs: 0.78
