def align_dna_sequences(seq1, seq2):
    m, n = len(seq1), len(seq2)
    
    # Initialize the dynamic programming table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table iteratively
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j * 3  # Insertion
            elif j == 0:
                dp[i][j] = i * 3  # Deletion
            else:
                # Calculate the cost for each operation
                insertion = dp[i][j - 1] + 3
                deletion = dp[i - 1][j] + 3
                substitution = dp[i - 1][j - 1] + (3 if seq1[i - 1] != seq2[j - 1] else 0)
                
                # Choose the minimum cost
                dp[i][j] = min(insertion, deletion, substitution)
    
    return dp[m][n]  # Minimum cost for aligning sequences