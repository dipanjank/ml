def longest_common_subsequence(seq1, seq2):
    """Find the longest common subsequence between seq1 and seq2."""
    n1, n2 = len(seq1), len(seq2)

    # Initialize a table of size n1 * n2
    seq_lengths = [[0] * n2 for _ in range(n1)]

    # First character match
    if seq1[0] == seq2[0]:
        seq_lengths[0][0] = 1

    # Initialize first column: we only have the first character of seq2
    # the value in the first column of seq_lengths is 0 until we find a matching character, then it's 1
    for i in range(1, n1):
        tmp = 1 if seq1[i] == seq2[0] else 0
        seq_lengths[i][0] = max(seq_lengths[i-1][0], tmp)

    # Initialize first row: we only have the first character of seq1
    for j in range(1, n2):
        tmp = 1 if seq2[j] == seq1[0] else 0
        seq_lengths[0][j] = max(seq_lengths[0][j-1], tmp)

    # Now fill in the rest of the table
    for i in range(1, n1):
        for j in range(1, n2):
            # We have 3 candidates:
            # 1. previous row previous column
            # 2. same column in previous row
            # 3. same row previous column
            # If seq1[i] == seq2[j] then we add 1 to candidate 1
            tmp = 1 if seq1[i] == seq2[j] else 0
            c1 = seq_lengths[i-1][j-1] + tmp

            # Max seq length up to the i-th row & j-th column is the max of the 3 candidates
            seq_lengths[i][j] = max(
                c1,
                seq_lengths[i][j-1],
                seq_lengths[i-1][j]
            )
    # Max seq length is the last element in the table
    return seq_lengths[n1-1][n2-1]


if __name__ == '__main__':
    s1 = ['B', 'C', 'D', 'A', 'A', 'C', 'D']
    s2 = ['A', 'C', 'D', 'B', 'A', 'C']
    result = longest_common_subsequence(s1, s2)
    print(result)

    s1 = ['A', 'C', 'A', 'D', 'B']
    s2 = ['C', 'B', 'D', 'A']
    result = longest_common_subsequence(s1, s2)
    print(result)
